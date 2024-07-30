def to_jaden_case(string):
  list = string.split()
  for n, p in enumerate(list):
      s = p.capitalize()
      list[n] = s
  return " ".join(list)