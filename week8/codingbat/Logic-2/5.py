def round_sum(a, b, c):
  a = check(a)
  b = check(b)
  c = check(c)
  return a+b+c
def check(n):
  if n%10 >= 5:
    return n+10-n%10
  return n-n%10
