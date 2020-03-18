def centered_average(nums):
  nums.sort()
  nums = nums[1:len(nums)-1]
  mean = 0
  for i in nums:
    mean+=i
  return mean/len(nums)
