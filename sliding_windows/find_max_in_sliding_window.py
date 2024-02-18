def find_max_sliding_window(nums: list[int], w: int) -> list[int]:
    max_vals = []
    for i in range(0, len(nums) - w + 1):
        sub_arr = nums[i : i + w]
        max_vals.append(max(sub_arr))
    return max_vals


print(find_max_sliding_window([-4, 2, -5, 3, 6], 3))
