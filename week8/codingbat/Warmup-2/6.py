def array_count9(nums):
  cnt = 0
  for i in nums:
    cnt += i == 9
  return cnt
