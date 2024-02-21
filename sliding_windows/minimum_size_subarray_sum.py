def min_sub_array_len(target: int, nums: list[int]) -> int:
    shortest, sum_, start = float('inf'), 0, 0
    for end, num in enumerate(nums):
        sum_ += num
        while sum_ >= target:
            shortest = (
                end - start + 1 if end - start + 1 < shortest else shortest
            )
            sum_ -= nums[start]
            start += 1

    return shortest if shortest != float('inf') else 0


print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))
