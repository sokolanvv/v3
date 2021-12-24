from Lexer import Lexer
from Parser import Parser

from sys import argv

import json

def isValidPath(path) -> bool:
  return not(path == "" or path == "\n")

if __name__ == "__main__":
#   i = input("""
# Enter:
#  - lex: analyze file lexically
#  - par: analyze file syntactically
#  - ext: exit
# """)

  input_file = None
  if '-i' in argv:
    input_file = argv[argv.index('-i') + 1]
  
  # for i in range(1):
  #   l = Lexer(f'test{i+1}')
  #   l.display()

  k = Lexer(input_file)
  k.display()
  # g = Parser(k.tokens).parse()
  # print(json.dumps(g, indent=2))

  # if i == 'lex':
  #   path = input("    Input file name:\n\t")
  #   if isValidPath(path):
  #     lex = Lexer(path)
  #   else:
  #     lex = Lexer()
  #   lex.display()
  # elif i == 'par':
  #   path = input("    Input file name:\n\t")
  #   if isValidPath(path):
  #     pars = Parser(path)
  #   else:
  #     pars = Parser(path)
  #   pars.display()
  # elif i == 'ext':
  #   exit(0)
  # else:
  #   raise Exception("Wrong command")