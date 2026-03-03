from tokens import Token, TokenType
from tokenstream import *
from acdcast import *

class ParseError(Exception):
    pass 

def parse(ts: TokenStream) -> ASTNode:
    t = ts.peek()

    if t.tokentype == TokenType.PRINT:
        ts.read()
        v = expect(ts, TokenType.VARREF)
        node = PrintNode(v.lexeme)
        expect(ts, TokenType.EOF)
        return node

    if t.tokentype == TokenType.INTDEC:
        ts.read()
        v = expect(ts, TokenType.VARREF)
        node = IntDclNode(v.lexeme)
        expect(ts, TokenType.EOF)
        return node

    if t.tokentype == TokenType.VARREF:
        lhs = ts.read()
        expect(ts, TokenType.ASSIGN)
        rhs = parse_expression(ts)
        if lhs.lexeme is None:
            raise ParseError("Malformed VARREF token on LHS")
        node = AssignNode(lhs.lexeme, rhs)
        expect(ts, TokenType.EOF)
        return node

    raise ParseError(
        f"Expected TokenType.PRINT, TokenType.INTDCL/INTDEC, or TokenType.VARREF; got {t.tokentype}"
    )

def parse_expression(ts: TokenStream) -> ASTNode:
    opstack = []
    valstack = []

    precedence = {
        TokenType.EXPONENT: 3,
        TokenType.TIMES: 2,
        TokenType.DIVIDE: 2,
        TokenType.PLUS: 1,
        TokenType.MINUS: 1,
    }

    leftassoc = {
        TokenType.EXPONENT: False,
        TokenType.TIMES: True,
        TokenType.DIVIDE: True,
        TokenType.PLUS: True,
        TokenType.MINUS: True,
    }

    operatortypes = {
        TokenType.PLUS,
        TokenType.MINUS,
        TokenType.TIMES,
        TokenType.DIVIDE,
        TokenType.EXPONENT,
    }
    
    expect_operand = True

    while ts.peek().tokentype != TokenType.EOF:
        tok = ts.peek()

        if tok.tokentype == TokenType.INTLIT:
            if not expect_operand:
                 raise ParseError("Expected operator or rparen after int literal")
            tok = ts.read()
            if tok.intvalue is None:
                raise ParseError("Malformed INTLIT token")
            valstack.append(IntLitNode(tok.intvalue))
            expect_operand = False
            continue

        if tok.tokentype == TokenType.VARREF:
            if not expect_operand:
                 raise ParseError("Expected operator or rparen after var ref")
            tok = ts.read()
            valstack.append(VarRefNode(tok.lexeme))
            expect_operand = False
            continue

        if tok.tokentype == TokenType.LPAREN:
             if not expect_operand:
                  raise ParseError("Expected operator")
             ts.read()
             opstack.append(tok)
             expect_operand = True
             continue

        if tok.tokentype == TokenType.RPAREN:
            if expect_operand:
                if len(opstack) > 0 and opstack[-1].tokentype == TokenType.LPAREN:
                     raise ParseError("Expected lparen, intlit, or varref after lparen")
                else:
                     raise ParseError("Expected operand or lparen after operator")
            ts.read()
            expect_operand = False
            
            while True:
                if len(opstack) == 0:
                    raise ParseError("Mismatched parentheses")
                if opstack[-1].tokentype == TokenType.LPAREN:
                    opstack.pop()
                    break
                reduce(opstack, valstack)
            continue

        if tok.tokentype in operatortypes:
            if expect_operand:
                if len(opstack) == 0:
                     raise ParseError(f"Expected two operands for operator {tok.tokentype}")
                elif opstack[-1].tokentype == TokenType.LPAREN:
                     raise ParseError("Expected lparen, intlit, or varref after lparen")
                else:
                     raise ParseError("Expected operand or lparen after operator")
            
            incoming = ts.read()
            expect_operand = True

            while len(opstack) > 0 and opstack[-1].tokentype in operatortypes:
                top = opstack[-1]
                top_prec = precedence[top.tokentype]
                inc_prec = precedence[incoming.tokentype]

                if leftassoc[incoming.tokentype]:
                    if top_prec >= inc_prec:
                        reduce(opstack, valstack)
                    else:
                        break
                else:
                    if top_prec > inc_prec:
                        reduce(opstack, valstack)
                    else:
                        break

            opstack.append(incoming)
            continue

        raise ParseError(f"Unexpected token in expression: {tok}")

    if expect_operand:
         raise ParseError("Expected operand or lparen after operator")

    while len(opstack) > 0:
        if opstack[-1].tokentype == TokenType.LPAREN:
            raise ParseError("Mismatched parentheses")
        reduce(opstack, valstack)

    if len(valstack) != 1:
        raise ParseError("Expression did not reduce to one AST")

    return valstack.pop()

def reduce(opstack: list, valstack: list) -> None:
    if len(opstack) == 0:
        raise ParseError("No operator to reduce")
    if len(valstack) < 2:
        raise ParseError("Not enough operands to reduce")
        
    op = opstack.pop()
    right = valstack.pop()
    left = valstack.pop()
    
    node = BinOpNode(op.tokentype, left, right)
    valstack.append(node)

def expect(ts: TokenStream, expectedtype: TokenType) -> Token:
    tok = ts.peek()
    if tok.tokentype == expectedtype:
        return ts.read()
    else:
        raise ParseError(f"Expected {expectedtype} but found {tok.tokentype}")