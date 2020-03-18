def array_front9(nums):
  ok = False
  for i in range(min(len(nums), 4)):
    if nums[i] == 9:
      ok = True
      break
  return ok
