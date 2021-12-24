dict = {
  'n': '\n',
  'r': '\r',
  't': '\t',
  'f': '\f',
  'b': '\b'
}

def getEscape(ch):
  return dict.get(ch, ch)