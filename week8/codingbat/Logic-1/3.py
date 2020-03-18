def squirrel_play(temp, is_summer):
  sumr = 0
  if is_summer:
    sumr = 10
  return (temp >= 60) & (temp <= 90+sumr)
