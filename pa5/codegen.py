from acdcast import *

class InstructionList:
    def __init__(self):
        self.instructions = []

    def append(self, instruction: str):
        self.instructions.append(instruction)

    def extend(self, newinstructions: "InstructionList"):
        self.instructions.extend(newinstructions.instructions)

    def __iter__(self):
        return iter(self.instructions)

def codegenerator(program: list[ASTNode]) -> InstructionList:
    code = InstructionList()
    for statement in program:
        newcode = stmtcodegen(statement)
        code.extend(newcode)
    return code
    
def stmtcodegen(statement: ASTNode) -> InstructionList:
    code = InstructionList()

    if isinstance(statement, IntDclNode):
        pass

    elif isinstance(statement, IntLitNode):
        code.append(str(statement.value))

    elif isinstance(statement, VarRefNode):
        code.append(f"l{statement.varname}")
    
    elif isinstance(statement, PrintNode):
        code.append(f"l{statement.varname}")
        code.append("p")
    
    elif isinstance(statement, AssignNode):
        code.extend(stmtcodegen(statement.expr))
        code.append(f"s{statement.varname}")

    elif isinstance(statement, BinOpNode):
        from tokens import TokenType
        op = statement.optype
        
        if op == TokenType.EXPONENT and isinstance(statement.right, IntLitNode):
            n = statement.right.value
            if n > 0:
                code.extend(stmtcodegen(statement.left))
                for _ in range(n - 1):
                    code.append("d")
                for _ in range(n - 1):
                    code.append("*")
                return code
            
        code.extend(stmtcodegen(statement.left))
        code.extend(stmtcodegen(statement.right))
        
        if op == TokenType.PLUS:
            code.append("+")
        elif op == TokenType.MINUS:
            code.append("-")
        elif op == TokenType.TIMES:
            code.append("*")
        elif op == TokenType.DIVIDE:
            code.append("/")
        elif op == TokenType.EXPONENT:
            code.append("^")
        else:
            raise NotImplementedError(f"Unknown operator {op}")

    return code
