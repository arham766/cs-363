class CharStream:
    def __init__(self, source:str):
        self.source = source
        self.pos = 0
        self.sourcelen = len(source)

    def eof(self) -> bool:
        return self.pos >= self.sourcelen

    def peek(self) -> str:
        if self.eof():
            return ''
        else:
            return self.source[self.pos]

    def advance(self) -> None:
        if not self.eof():
            self.pos += 1

    def read(self) -> str:
        if self.eof():
            return ''
        else:
            c = self.source[self.pos]
            self.advance()
            return c
