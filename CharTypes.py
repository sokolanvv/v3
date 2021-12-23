from enum import Enum

class CharType(Enum):
  unknown = 0
  #Start LettersAndUnderscore
  af = 1
  e = 2
  j = 3
  x = 37
  b = 38
  o = 39
  restL = 4
  underscore = 36
  #End LettersAndUnderscore
  #Start Numbers
  C0 = 40
  C1 = 5
  C27 = 6
  C89 = 7
  #End Numbers
  ws = 8
  #Start Operators
  plus = 9
  minus = 10
  mult = 11
  div = 12
  remainder = 13
  matrixMult = 14
  less = 15
  more = 16
  amp = 17
  pipe = 18
  xor = 19
  bnot = 20
  equal = 21
  bang = 22
  #End Operators
  com = 23
  newline = 24
  #Start DelimitersPCB
  pOpen = 25
  pClose = 26
  bOpen = 27
  bClose = 28
  cOpen = 29
  cClose = 30
  #End DelimitersPCB
  #Start RestDelimiters
  comma = 31
  colon = 32
  dot = 33
  semicolon = 34
  #End RestDelimiters
  backslash = 35
  #Start String literal delimiters
  squote = 41
  dquote = 42