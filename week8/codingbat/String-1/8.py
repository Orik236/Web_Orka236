def combo_string(a, b):
  if len(b) < len(a):
    b, a = a, b
  return a + b + a
