def accum(st):
  string = ""
  for n, c in enumerate(st):
      if n == 0:
          string += c.upper() + "-"
      else:
          string += c.upper() + (c.lower() * n) + "-"
  return string[:-1:]