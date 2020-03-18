def in1to10(n, outside_mode):
  if outside_mode:
    return (n<=1) | (n>=10)
  return (n>=1) & (n<=10)
