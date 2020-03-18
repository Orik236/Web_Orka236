def caught_speeding(speed, is_birthday):
  bonus = 0
  if is_birthday:
    bonus = 5
  if speed <= 60 + bonus:
    return 0
  if speed >= 81 + bonus:
    return 2
  else:
    return 1
