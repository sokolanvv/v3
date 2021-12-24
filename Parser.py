class ObjWrap:
  def __init__(self, val):
    self.interprited = val
    self.type = val

class Parser:
  def __init__(self, tokenList):
    print()
    self.tokens = tokenList
    self.tokenC = 0

  def getNextToken(self):
    try:
      token = self.tokens[self.tokenC].value
      if (token in ['NEWLINE', 'INDENT', 'DEDENT']):
        token = ObjWrap(token)
      self.tokenC += 1
    except IndexError:
      token = None
    return token

  def parse(self):
    self.lookahead = self.getNextToken()

    return self.Program()

  def Program(self):
    return {
      "type": "Program",
      "body": self.StatementList()
    }

  def StatementList(self):
    s = self.Statement()
    statementList = [s]

    while (self.lookahead != None):
      statementList.append(self.Statement())

    return statementList

  def Statement(self):
    return self.ExpressionStatement()

  def ExpressionStatement(self):
    expression = self.Expression()
    k = self.consume('NEWLINE')
    return {
      "type": "ExpressionStatement",
      "expression": expression
    }

  def Expression(self):
    return self.AssignmentExpression()

  def AssignmentExpression(self):
    left = self.BinAddExpression()

    if (self.lookahead.interprited in [
      'ASSIGN', 'ASSIGN_ADD', 
      'ASSIGN_REM', 'ASSIGN_MUL', 
      'ASSIGN_DIV'
    ]):
      opType = self.lookahead.interprited
      self.consume(opType)

      left = self.validateCanAssign(left)

      return {
        "type": 'AssignmentExpression',
        "operator": opType,
        "left": left,
        "right": self.AssignmentExpression()
      }

    return left

  def AssignmentTarget(self):
    return self.Identifier()

  def validateCanAssign(self, node):
    if (node["type"] == 'Identifier'):
      return node
    
    raise SyntaxError(f"Invalid assignment target!")

  def BinAddExpression(self):
    left = self.BinMultExpression()

    while (self.lookahead.interprited in ['PLUS', 'MINUS']):
      operator = self.consume(self.lookahead.interprited).interprited
      right = self.BinMultExpression()

      left = {
        "type": "BinaryExpression",
        "operator": operator,
        "left": left,
        "right": right
      }

    return left

  def BinMultExpression(self):
    left = self.PrimaryExpression()

    self.lookahead
    while (self.lookahead.interprited in ['MULT', 'DIV']):
      operator = self.consume(self.lookahead.interprited).interprited
      right = self.PrimaryExpression()

      left = {
        "type": 'BinaryExpression',
        "operator": operator,
        "left": left,
        "right": right
      }

    return left

  def PrimaryExpression(self):
    if (self.isLiteral(self.lookahead)):
      return self.Literal()
    if (self.lookahead.interprited == 'PAROPEN'):
      return self.ParanthesisedPrimary()
    else:
      return self.AssignmentTarget()

  def Identifier(self):
    token = self.consume('IDENTIFIER')
    return {
      "type": 'Identifier',
      "value": token.interprited
    }

  def ParanthesisedPrimary(self):
    self.consume('PAROPEN')
    expression = self.Expression()
    self.consume('PARCLOSE')
    return expression

  def Literal(self):
    if (self.lookahead == None):
      raise SyntaxError("Expected a literal!")
    
    t = self.lookahead.type
    if   (t == 'INTEGER'):
      return self.NumLiteral('INTEGER')
    elif (t == 'FLOAT'):
      return self.NumLiteral('FLOAT')
    elif (t == 'STRING'):
      return self.StringLiteral()
    else:
      raise SyntaxError(f"Unexpected literal! Got: {t}")

  def isLiteral(self, token):
    return token.type in [
      'INTEGER', 'FLOAT', 'STRING'
    ]

  def NumLiteral(self, f):
    token = self.consume(f)
    return {
      "type": 'NumericLiteral',
      "value": token.interprited
    }

  def StringLiteral(self):
    token = self.consume('STRING')
    return {
      "type": 'StringLiteral',
      "value": token.interprited
    }

  def consume(self, tokenType):
    token = self.lookahead

    if (token == None):
      raise SyntaxError(f"Unexpected EOS, expected {tokenType}")

    if (
      token.type != tokenType and
      token.interprited != tokenType
    ):
      raise SyntaxError(f"Unexpected token: Got '{token.type}', expected: '{tokenType}'")

    self.lookahead = self.getNextToken()
    return token

  def display():
    print("Not implemented yet")