def string_splosion(str):
  t = ''
  for i in range(1, len(str)+1):
    t += str[:i]
  return t
