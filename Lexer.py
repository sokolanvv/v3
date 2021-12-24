from Stack import Stack

from States import State

from Lexeme import Lexeme
from Token import Token
from CharTypes import CharType

from Escape import getEscape
from StateMachine import getState
from TypeMachine import getType
from LexemeTypes import getTyping
from Interpreter import getInterpritation

class Lexer:
  indent_stack = Stack.fromValue(0)
  tokens = []
  lexemes = []
  file = None

  backdash = False

  current_line_number = 0
  current_cursor = 0

  buffer = ''
  state = State.nostate
  char = ''

  def __init__(self, path) -> None:
    if path:
      path = f'inputs/{path}.py'
    else:
      path = 'inputs/input.py'
    self.file = open(path, "r").readlines()

  def cursor_to_content(self, line) -> None:
    cursor = 0
    while getType(line[cursor]) == CharType.ws:
      cursor += 1

    return cursor

  def process_leftover_indents(self) -> None:
    tokens = self.indent_stack.clear(self.current_line_number)
    if tokens:
      for token in tokens:
        self.tokens.append(token)

  def getLexeme(self, string, state) -> Lexeme:
    typing = getTyping(state)
    if typing == 'IDENTIFIER' and string in [
    'None', 'True', 'False', 'and', 'as', 'assert', 'break',
    'continue', 'def', 'del', 'elif', 'else', 'except',
    'for', 'from', 'global', 'if', 'import', 'in',
    'class', 'finally', 'is', 'lambda', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
    'yield'
    ]:
      typing = 'KEYWORD'

    return Lexeme(
      self.current_line_number,
      self.current_cursor,
      typing,
      getInterpritation(string, typing),
      string
    )

  def bufferCleanUp(self):
    if self.buffer != '':
      self.tokens.append(Token(
        self.current_line_number, 0,
        self.getLexeme(self.buffer, self.state)
      ))
    self.buffer = ''

  def process_lexemes_3(self, line) -> None:
    self.char = line[self.current_cursor]
    self.state = getState(State.nostate, self.char)

    self.current_cursor += 1

    while (self.current_cursor < len(line)):
      c_char = line[self.current_cursor]
      c_state = getState(self.state, c_char)

      if (c_state == State.err):
        raise SyntaxError(f"Syntax error! Line {self.current_line_number} column {self.current_cursor}")

      if (c_state == State.newline):
        self.buffer += self.char
        self.bufferCleanUp()
        self.backdash = False
        self.tokens.append(Token(
          self.current_line_number, len(line),
          'NEWLINE'
        ))
      elif (c_state == State.elj):
        self.bufferCleanUp()
        self.backdash = True
        return
      elif (c_state == State.comment):
        self.bufferCleanUp()
        self.backdash = False
        return
      elif (c_state == State.escapeS):
        self.state = State.escapeS
      elif (c_state == State.escapeC):
        c_char = getEscape(c_char)
        self.buffer += c_char
        self.state = State.sL
      elif (c_state == State.nostate):
        if (getType(c_char) == CharType.squote or getType(c_char) == CharType.dquote) and self.state == State.sL:
          self.buffer += self.char
          self.buffer += c_char
          self.bufferCleanUp()
          self.state = State.nostate
          self.char = ''
        else:
          self.buffer += self.char
          self.bufferCleanUp()
          if getType(c_char) == CharType.ws:
            self.state = State.nostate
            self.char = ''
          else:
            self.char = c_char
            self.state = getState(c_state, c_char)
      else:
        self.buffer += self.char
        self.state = c_state
        self.char = c_char

      self.current_cursor += 1

    # for i, token in enumerate(self.tokens):
    #   print(f"Token #{i+1}: {token.toString()}")
    # print()

  def analyse(self) -> None:
    last_line = self.file[-1]
    if last_line[-1] != '\n':
      self.file[-1] = last_line + '\n'
    
    for line_num, line in enumerate(self.file):
      self.current_line_number = line_num + 1

      cursor = self.cursor_to_content(line)
      if (
        getType(line[cursor]) != CharType.newline and
        getType(line[cursor]) != CharType.com
      ):
        self.current_cursor = cursor

        if not self.backdash:
          tokens = self.indent_stack.push(cursor, self.current_line_number)
          if tokens != []:
            for token in tokens:
              self.tokens.append(token)
        print(f"Proccessed line #{self.current_line_number}:\n{line[cursor:]}\n", end="")

        self.process_lexemes_3(line)

    self.process_leftover_indents()


  def display(self) -> None:
    self.analyse()
    print()
    # with open("test", "w") as f:
    for i, token in enumerate(self.tokens):
      print(f"{token.toString()}")