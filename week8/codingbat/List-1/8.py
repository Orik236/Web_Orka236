def make_ends(nums):
  if len(nums) == 1:
    return nums*2
  else:
    return [nums[0]] + [nums[-1]]
