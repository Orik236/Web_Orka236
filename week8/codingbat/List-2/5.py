def sum67(nums):
  ok = False
  sum = 0
  for i in nums:
    if i == 6:
      ok = True
      continue
    elif (i == 7) & (ok):
      ok = False
      continue
    elif ok:
      continue
    sum+=i
  return sum
