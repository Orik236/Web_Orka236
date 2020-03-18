def reverse3(nums):
    for i in range(0, len(nums) // 2):
        nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]

    return nums

