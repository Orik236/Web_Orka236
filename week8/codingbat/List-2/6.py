def has22(nums):
  for i in range(len(nums)-1):
    if (nums[i] == 2) & (nums[i+1] == 2):
      return True
  return False
