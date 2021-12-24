from States import State
from CharTypes import CharType
from TypeMachine import getType

Operators = [
  CharType.plus, CharType.minus, CharType.mult, CharType.div, CharType.remainder,
  CharType.matrixMult, CharType.less, CharType.more, CharType.amp, CharType.pipe,
  CharType.xor, CharType.bnot
]

Letters = [
  CharType.af, CharType.e, CharType.j, CharType.restL,
  CharType.b, CharType.x, CharType.o
]

Numbers = [ CharType.C0, CharType.C1, CharType.C27, CharType.C89 ]

DelimitersPCB = [
  CharType.pOpen, CharType.pClose, CharType.bOpen, CharType.bClose,
  CharType.cOpen, CharType.cClose
]

RestDelimiters = [ CharType.comma, CharType.colon, CharType.dot, CharType.semicolon ]

Nocat = [ CharType.unknown, CharType.ws, CharType.com, CharType.newline, CharType.backslash ]

StringLiterals = [ CharType.squote, CharType.dquote ]

transit = { State.nostate: {
  CharType.unknown: State.err,

  CharType.af: State.identifier,
  CharType.e: State.identifier,
  CharType.j: State.identifier,
  CharType.x: State.identifier,
  CharType.o: State.identifier,
  CharType.b: State.identifier,
  CharType.restL: State.identifier,
  CharType.underscore: State.identifier,

  CharType.C0: State.zero,
  CharType.C1: State.diL,
  CharType.C27: State.diL,
  CharType.C89: State.diL,

  CharType.ws: State.nostate,

  CharType.plus: State.op,
  CharType.minus: State.op,
  CharType.mult: State.op,
  CharType.div: State.op,
  CharType.remainder: State.op,
  CharType.matrixMult: State.op,
  CharType.less: State.op,
  CharType.more: State.op,
  CharType.amp: State.op,
  CharType.pipe: State.op,
  CharType.xor: State.op,
  CharType.bnot: State.op,
  CharType.equal: State.op,
  CharType.bang: State.op,

  CharType.com: State.comment,
  CharType.newline: State.newline,

  CharType.pOpen: State.pOpen,
  CharType.pClose: State.pClose,
  CharType.bOpen: State.bOpen,
  CharType.bClose: State.bClose,
  CharType.cOpen: State.cOpen,
  CharType.cClose: State.cClose,

  CharType.comma: State.lim,
  CharType.colon: State.lim,
  CharType.dot: State.dot,
  CharType.semicolon: State.lim,

  CharType.backslash: State.elj,

  CharType.squote: State.sL,
  CharType.dquote: State.sL
}}

# String literals
transit.update({ State.sL: {
  i: State.sL if i not in [ *StringLiterals ]
  else State.nostate
  for i in CharType
}})
# -

# Identifiers
transit.update({ State.identifier: {
  i: State.newline if i == CharType.newline
  else State.identifier if i in [ *Letters, *Numbers, CharType.underscore ]
  else State.err if i in [ CharType.unknown ]
  else State.nostate
  for i in CharType
}})
# -

# Zero
transit.update({ State.zero: {
  i: State.zeros if i == CharType.C0
  else State.zerosU if i == CharType.underscore
  else State.fL  if i == CharType.dot
  else State.efL if i == CharType.e
  else State.biL if i == CharType.b
  else State.oiL if i == CharType.o
  else State.hiL if i == CharType.x
  else State.ifL if i == CharType.j
  else State.err if i in [ *Letters, *Numbers ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.zerosU: {
  i: State.zeros if i == CharType.C0
  else State.err
  for i in CharType
}})

transit.update({ State.zeros: {
  i: State.zeros if i == CharType.C0
  else State.fL if i == CharType.dot
  else State.zerosU if i == CharType.underscore
  else State.err if i in [ *Letters, *Numbers ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Decimal Integers
transit.update({ State.diL: {
  i: State.nostate if i in [ 
    *Operators, *DelimitersPCB, 
    CharType.ws, CharType.comma, CharType.colon, CharType.semicolon
  ]
  else State.efL if i == CharType.e
  else State.ifL if i == CharType.j
  else State.fL if i == CharType.dot
  else State.diL if i in [ *Numbers ]
  else State.diLU if i == CharType.underscore
  else State.newline if i == CharType.newline
  else State.err
  for i in CharType
}})

transit.update({ State.diLU: {
  i: State.diL if i in [ *Numbers ]
  else State.err
  for i in CharType
}})
# -

# Binary Integers
transit.update({ State.biL: {
  i: State.biL if i in [ CharType.C0, CharType.C1, CharType.underscore ]
  else State.err if i in [ *Letters, *Numbers ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Hex Integers
transit.update({ State.hiL: {
  i: State.hiL if i in [ CharType.b, CharType.e, CharType.af, CharType.C0, CharType.C1, CharType.C27, CharType.C89, CharType.underscore ]
  else State.err if i in [ *Letters, *Numbers ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Oct Numbers
transit.update({ State.oiL: {
  i: State.oiL if i in [ CharType.underscore, CharType.C0, CharType.C1, CharType.C27 ]
  else State.err if i in [ *Letters, *Numbers ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Regular Floats
transit.update({ State.fL: {
  i: State.nostate if i in [ CharType.ws, *Operators, *DelimitersPCB, *RestDelimiters ]
  else State.fLNU if i in [ *Numbers ]
  else State.efL if i == CharType.e
  else State.ifL if i == CharType.j
  else State.err
  for i in CharType
}})

transit.update({ State.fLNU: {
  i: State.nostate if i in [ CharType.ws, *Operators, *DelimitersPCB, *RestDelimiters ]
  else State.fLNU if i in [ *Numbers ]
  else State.fLU if i == CharType.underscore
  else State.efL if i == CharType.e
  else State.ifL if i == CharType.j
  else State.newline if i == CharType.newline
  else State.err
  for i in CharType
}})

transit.update({ State.fLU: {
  i: State.fLNU if i in [ *Numbers ]
  else State.err
  for i in CharType
}})
# -

# Exponent Floats
transit.update({ State.efL: {
  i: State.efsL if i in [ *Numbers, CharType.plus ]
  else State.efnL if i == CharType.minus
  else State.err
  for i in CharType
}})

transit.update({ State.efsL: {
  i: State.efsL if i in [ *Numbers ]
  else State.efsLU if i == CharType.underscore
  else State.err if i in [ *Letters ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.efsLU: {
  i: State.efsL if i in [ *Numbers ]
  else State.err
  for i in CharType
}})

transit.update({ State.efnL: {
  i: State.efnL if i in [ *Numbers ]
  else State.efnLU if i == CharType.underscore
  else State.err if i in [ *Letters ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.efnLU: {
  i: State.efnL if i in [ *Numbers ]
  else State.err
  for i in CharType
}})
# -

# Imaginary Floats
transit.update({ State.ifL: {
  i: State.err if i in [ *Numbers, *Letters, CharType.underscore ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Operations
transit.update({ State.op: {
  i: State.op if i in [ *Operators, CharType.equal ]
  else State.err if i in [ *RestDelimiters ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

# Delimiters
transit.update({ State.lim: {
  i: State.err if i in [ *DelimitersPCB ]
  else State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.dot: {
  i: State.err if i not in [ 
    CharType.underscore, *Letters, *Numbers
  ]
  else State.fL if i in [ *Numbers ]
  else State.nostate
  for i in CharType
}})

transit.update({ State.pOpen: {
  i: State.err if i in [ 
    CharType.mult, CharType.div, CharType.remainder,
    CharType.less, CharType.more, CharType.equal, CharType.colon,
    CharType.xor, CharType.bnot, CharType.matrixMult, CharType.newline,
    CharType.com, CharType.comma, CharType.semicolon, CharType.backslash
  ]
  else State.nostate
  for i in CharType
}})

transit.update({ State.pClose: {
  i: State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.bOpen: {
  i: State.err if i in [
    CharType.mult, CharType.div, CharType.remainder,
    CharType.less, CharType.more, CharType.equal, CharType.colon,
    CharType.xor, CharType.bnot, CharType.matrixMult, CharType.newline,
    CharType.com, CharType.comma, CharType.semicolon, CharType.backslash
  ]
  else State.nostate
  for i in CharType
}})

transit.update({ State.bClose: {
  i: State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})

transit.update({ State.cOpen: {
  i: State.err if i in [
    CharType.mult, CharType.div, CharType.remainder,
    CharType.less, CharType.more, CharType.equal, CharType.colon,
    CharType.xor, CharType.bnot, CharType.matrixMult, CharType.newline,
    CharType.com, CharType.comma, CharType.semicolon, CharType.backslash
  ]
  else State.nostate
  for i in CharType
}})

transit.update({ State.cClose: {
  i: State.newline if i == CharType.newline
  else State.nostate
  for i in CharType
}})
# -

transit.update({ State.newline: {
  i: State.nostate for i in CharType
}})

def getState(state, ch) -> object:
  type = getType(ch)
  return transit[state].get(type, State.err)

if __name__ == "__main__":
  for st in transit:
    print(transit[st])

  while True:
    i = input("Input: ")
    print(getState(State.nostate, i))