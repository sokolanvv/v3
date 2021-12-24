class Token:
  line = None
  pos = None
  name = "NONAME"


  def __init__(self, line, pos, value) -> None:
    self.line = line
    self.pos = 0
    self.value = value

  def toString(self) -> None:
    if self.line != None and self.pos != None and self.value != "NONAME":
      if type(self.value) != str:
        val = self.value.toString()
      else:
        val = self.value
      return f"{val}"
    else:
      raise Exception("Tried displaying incomplete token")