from enum import Enum

class State(Enum):
  nostate = 0
  identifier = 1
  sL = 10
  bL = 20
  diL = 31
  diLU = 311
  biL = 32
  biLU = 321
  oiL = 33
  hiL = 34
  zero = 350
  zerosU = 351
  zeros = 352
  fL = 41
  fLU = 411
  fLNU = 412
  efL = 420
  efsL = 421
  efsLU = 422
  efnL = 423
  efnLU = 424
  ifL = 43
  op = 50
  lim = 60
  pOpen = 61
  pClose = 62
  bOpen = 63
  bClose = 64
  cOpen = 65
  cClose = 66
  dot = 67
  comment = 70
  newline = 80
  elj = 90
  err = 666