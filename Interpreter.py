def getInterpritation(string, type):
  if type == 'INTEGER':
    if len(string) < 3:
      return int(string)
    if string[1] == 'x' or string[1] == 'X':
      return int(string, base=16)
    elif string[1] == 'o' or string[1] == 'O':
      return int(string, base=8)
    elif string[1] == 'b' or string[1] == 'B':
      return int(string, base=2)
    else:
      return int(string)
  elif type == 'FLOAT':
    return float(string)
  elif type == 'STRING':
    return string[1:-1]
  else:
    return string