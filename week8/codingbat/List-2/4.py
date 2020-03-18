def sum13(nums):
  if len(nums) == 0:
    return 0
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      nums[min(i+1, len(nums)-1)] = 0
    else:
      sum+=nums[i]
  return sum
