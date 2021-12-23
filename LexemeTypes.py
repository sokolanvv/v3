from States import State

dict = {
  State.identifier: 'IDENTIFIER',
  State.sL: 'STRING',
  State.zero: 'INTEGER',
  State.zeros: 'INTEGER',
  State.diL: 'INTEGER',
  State.biL: 'INTEGER',
  State.hiL: 'INTEGER',
  State.oiL: 'INTEGER',
  State.fL: 'FLOAT',
  State.fLNU: 'FLOAT',
  State.efsL: 'FLOAT',
  State.efnL: 'FLOAT',
  State.ifL: 'IMAGINARY',
  State.op: 'OPERATOR',
  State.lim: 'DELIMITER',
  State.dot: 'DELIMITER',
  State.pOpen: 'DELIMITER',
  State.pClose: 'DELIMITER',
  State.bOpen: 'DELIMITER',
  State.bClose: 'DELIMITER',
  State.cOpen: 'DELIMITER',
  State.cClose: 'DELIMITER'
}

def getTyping(state):
  res = dict.get(state, None)
  if res == None:
    raise SyntaxError("Unexpected Lexeme!")
  return res