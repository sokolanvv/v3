from typing import List
from Token import Token

class Stack:
  stack = []

  def __init__(self, initList=[]) -> None:
    self.stack = initList

  @classmethod
  def fromValue(cls, initValue) -> object:
    return cls([ initValue ])

  def push(self, value, line) -> list:
    current = self.peek()
    res = []
    if current < value:
      self.stack.append(value)
      res.append(Token(line, 0, "INDENT"))
    elif current > value:
      while current > value:
        self.pop()
        current = self.peek()
        res.append(Token(line, 0, "DEDENT"))
      if current != value:
        raise Exception("Unindented amount does not match indent")

    return res

  def pop(self) -> object:
    return self.stack.pop()

  def peek(self) -> object:
    return self.stack[len(self.stack) - 1]

  def clear(self, line) -> list:
    current = self.peek()
    res = []

    while current != 0:
      self.pop()
      current = self.peek()
      res.append(Token(line+1, 0, "DEDENT"))
    
    return res

  def toList(self) -> list:
    return self.stack