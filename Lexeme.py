class Lexeme:

  def __init__(self, line, col, type, inter, raw) -> None:
    self.line = line
    self.column = col - len(raw)
    self.type = type
    self.interprited = inter
    self.raw = raw

  def toString(self) -> str:
    sp = 8 - len(self.type)
    return f"{self.line}\t{self.column}\t{self.type}{' '*sp}\t{self.interprited}\t{self.raw}"