# Python lexer/parser \w Python3 (3.6.9)

# How to run

To run default test:
- python3 main.py

To run specific test:
- python3 main.py -i \<test_name\> (Note: .py extension is not needed)

# Quick overview

StateMachine.py and TypeMachine.py are one of the core files  
providing a backbone to the whole lexer module  

While TypeMachine.py is fairly simple providing cross-ref between symbols and types used by lexer/parser  
StateMachine.py is intended as automata for parsing lexemes

States.py and CharTypes.py are cross-ref files for files mentioned previously  

Token.py Stack.py Interpreter.py LexemeTypes.py are utility files  
They are there for easy and quick access to Token and Stack classes as well as  
interpriter for literals and it's supporting lexeme types file

# Main files

Main files are: 
- main.py: used to choose tests and start analysis
- Lexer.py: used for lexical analysis
- Parser.py: used for syntax analysis

inputs folder: Folder for storing test files

# Grammar

```
File
  : [Statements] ENDMARKER
  ;
```

```
Statements
  : Statement
  | Statements
  ;
```

```
Statement
  : CompoundStatement NEWLINE
  | SimpleStatement NEWLINE
  ;
```

```
CompoundStatement
  : FunctionDefinition
  | IFStatement
  | ForStatement
  | WhileStatement
  ;
```

```
SimpleStatement
  : Assignment
  | ReturnStatement
  | ImportStatement
  | EmptyStatement
  | Break
  | Continue
  ;
```

```
Assignment
  | IDENTIFIER ASSIGN
```