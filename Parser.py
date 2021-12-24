class Parser:
  def __init__(self, tokenList):
    self.tokens = tokenList
    self.tokenC = 0

  def getNextToken(self):
    token = self.tokens[self.tokenC]
    self.tokenC += 1
    return token

  def parse(self):
    self.lookahead = self.tokens.getNextToken()

    return self.Program()

  def Program(self):
    return {
      "type": "Program",
      "body": self.StatementList()
    }

  def StatementList(self):
    statementList = [self.Statement()]

    while (self.lookahead != None):
      statementList.append(self.Statement())

    return statementList

  def Statement(self):
    return self.ExpressionStatement()

  def ExpressionStatement(self):
    expression = self.Expression()
    self.consume('NEWLINE')
    return {
      "type": "ExpressionStatement",
      "expression": expression
    }

  def Expression(self):
    return self.AssignmentExpression()

  def AssignmentExpression(self):
    left = self.BinAddExpression()

    return left
    if (self.lookahead.interprited in [
      'ASSIGN', 'ASSIGN_ADD', 'ASSIGN_REM', 'ASSIGN_MUL', 'ASSIGN_DIV'
    ]):
      pass

  def BinAddExpression(self):
    left = self.BinMultExpression()

    while (self.lookahead.interpreted in ['PLUS', 'MINUS']):
      operator = self.consume(self.lookahead.interpreted)
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

    while (self.lookahead.interprited in ['MULT', 'DIV']):
      operator = self.consume(self.lookahead.interprited)
      right = self.PrimaryExpression()

      left = {
        "type": 'BinaryExpression',
        "operator": operator,
        "left": left,
        "right": right
      }

    return left

  def PrimaryExpression(self):
    if (self.lookahead.interprited == 'PAROPEN'):
      return self.ParanthesisedPrimary()
    else:
      return self.Literal()

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
      token.type != tokenType or
      token.interprited != tokenType
    ):
      raise SyntaxError(f"Unexpected token: Got {token.type}, expected: {tokenType}")

    self.lookahead = self.getNextToken()
    return token

  def display():
    print("Not implemented yet")