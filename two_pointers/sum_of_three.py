def find_sum_of_three(nums: list[int], target: int) -> bool:
    nums.sort()
    for i, elem in enumerate(nums):
        ptr1 = i + 1
        ptr2 = len(nums) - 1
        while ptr1 < ptr2:
            cur_sum = elem + nums[ptr1] + nums[ptr2]
            if cur_sum == target:
                return True
            if cur_sum < target:
                ptr1 += 1
            else:
                ptr2 -= 1
    return False


print(find_sum_of_three([-1, 2, 1, -4, 5, -3], -8))
