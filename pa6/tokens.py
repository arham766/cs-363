from enum import Enum

class TokenType(Enum):
    PRINT = 0
    INTDEC = 1
    INTLIT = 2
    VARREF = 3
    ASSIGN = 4
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    EXPONENT = '^'
    LPAREN = 10
    RPAREN = 11
    EOF = 12
    EOTS = 13
    FLOATDEC = 14
    FLOATLIT = 15
    STRDEC = 16
    STRLIT = 17



class Token:

    def __init__(
        self, 
        tokentype: TokenType, 
        lexeme: str,
        *,  
        name: str | None = None,
        intvalue: int | None = None,
        floatvalue: float | None = None,
        strvalue: str | None = None,
    ):

        self.tokentype = tokentype
        self.lexeme = lexeme
        self.name = name
        self.intvalue = intvalue
        self.floatvalue = floatvalue
        self.strvalue = strvalue

    def __str__(self):
        namepart = f"; name: {self.name}" if self.name is not None else ""
        intvalpart = f"; intval: {str(self.intvalue)}" if self.intvalue is not None else ""
        floatvalpart = f"; floatval: {str(self.floatvalue)}" if self.floatvalue is not None else ""
        strvalpart = f"; strval: {self.strvalue}" if self.strvalue is not None else ""

        return f"[Token type: {self.tokentype}; lexeme: {self.lexeme}{namepart}{intvalpart}{floatvalpart}{strvalpart}]"

    def __repr__(self):
        return self.__str__()
    
