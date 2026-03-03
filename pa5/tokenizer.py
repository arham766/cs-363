from charstream import CharStream
from tokenstream import TokenStream
from tokens import Token, TokenType

class Tokenizer:
    def __init__(self, charstream: CharStream):
        self.cs = charstream

    def tokenize(self) -> TokenStream:
        ts = TokenStream()
        
        while not self.cs.eof():
            char = self.cs.peek()

            if char.isspace():
                self.cs.advance()
                continue
            
            if char == 'p':
                self.cs.advance()
                ts.append(Token(TokenType.PRINT, "p", name="p"))
                continue

            if char == 'i':
                self.cs.advance()
                ts.append(Token(TokenType.INTDEC, "i", name="i"))
                continue
                
            if char.isalpha():
                self.cs.advance()
                ts.append(Token(TokenType.VARREF, char, name=char))
                continue

            if char.isdigit():
                num_str = ""
                while not self.cs.eof() and self.cs.peek().isdigit():
                    num_str += self.cs.read()
                ts.append(Token(TokenType.INTLIT, num_str, intvalue=int(num_str)))
                continue

            if char == '+':
                self.cs.advance()
                ts.append(Token(TokenType.PLUS, "+"))
                continue
            
            if char == '-':
                self.cs.advance()
                ts.append(Token(TokenType.MINUS, "-"))
                continue
                
            if char == '*':
                self.cs.advance()
                ts.append(Token(TokenType.TIMES, "*"))
                continue
                
            if char == '/':
                self.cs.advance()
                ts.append(Token(TokenType.DIVIDE, "/"))
                continue
            
            if char == '^':
                self.cs.advance()
                ts.append(Token(TokenType.EXPONENT, "^"))
                continue
                
            if char == '=':
                self.cs.advance()
                ts.append(Token(TokenType.ASSIGN, "="))
                continue

            if char == '(':
                self.cs.advance()
                ts.append(Token(TokenType.LPAREN, "("))
                continue

            if char == ')':
                self.cs.advance()
                ts.append(Token(TokenType.RPAREN, ")"))
                continue

            raise Exception(f"Unexpected character: {char}")

        return ts