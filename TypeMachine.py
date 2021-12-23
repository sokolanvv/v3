from CharTypes import CharType

dictionary  = { chr(i): CharType.restL for i in range(65, 91) }
dictionary.update({ chr(i): CharType.restL for i in range(97, 123) })

dictionary.update({ chr(i): CharType.af for i in range(65, 71) })
dictionary.update({ chr(i): CharType.af for i in range(91, 103) })

dictionary.update({'e': CharType.e, 'E': CharType.e})
dictionary.update({'b': CharType.b, 'B': CharType.b})
dictionary.update({'j': CharType.j, 'J': CharType.j})
dictionary.update({'o': CharType.o, 'O': CharType.o})
dictionary.update({'x': CharType.x, 'X': CharType.x})

dictionary.update({ chr(i): CharType.C27 for i in range(48, 58) })
dictionary.update({'0': CharType.C0, '1': CharType.C1})
dictionary.update({'8': CharType.C89, '9': CharType.C89})

dictionary.update({'_': CharType.underscore})

# Operators
dictionary.update({'+': CharType.plus})
dictionary.update({'-': CharType.minus})
dictionary.update({'*': CharType.mult})
dictionary.update({'/': CharType.div})
dictionary.update({'%': CharType.remainder})
dictionary.update({'@': CharType.matrixMult})

dictionary.update({'<': CharType.less})
dictionary.update({'>': CharType.more})
dictionary.update({'&': CharType.amp})
dictionary.update({'|': CharType.pipe})
dictionary.update({'^': CharType.xor})

dictionary.update({'~': CharType.bnot})
dictionary.update({'=': CharType.equal})
dictionary.update({'!': CharType.bang})

# Delimiters
dictionary.update({'(': CharType.pOpen})
dictionary.update({')': CharType.pClose})
dictionary.update({'[': CharType.bOpen})
dictionary.update({']': CharType.bClose})
dictionary.update({'{': CharType.cOpen})
dictionary.update({'}': CharType.cClose})

dictionary.update({',': CharType.comma})
dictionary.update({':': CharType.colon})
dictionary.update({';': CharType.semicolon})
dictionary.update({'.': CharType.dot})

dictionary.update({'\'': CharType.squote})
dictionary.update({'"': CharType.dquote})

# Special characters
dictionary.update({'#': CharType.com})
dictionary.update({'\\': CharType.backslash})

dictionary.update({'\n': CharType.newline})

# Whitespace
dictionary.update({' ': CharType.ws})
dictionary.update({'\t': CharType.ws})
dictionary.update({'\r': CharType.ws})
dictionary.update({'\f': CharType.ws})

dictionary.update({'': CharType.unknown})

def getType(ch):
  return dictionary.get(ch)

if __name__ == "__main__":
  i = input("Input char: ")
  print(getType(i))