def string_bits(str):
  t = ''
  for i in range(0, len(str), 2):
    t += str[i]
  return t