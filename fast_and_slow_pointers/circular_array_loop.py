def circular_array_loop(nums: list[int]) -> bool:
    slow, fast = 0, 0
    for i, _ in enumerate(nums):
        slow, fast = i, i
        while True:
            prev_slow = slow
            slow += nums[prev_slow]
            slow = slow if abs(slow) < len(nums) else slow % len(nums)
            if nums[slow] * nums[prev_slow] < 0 or slow == prev_slow:
                break
            prev_fast = fast
            fast += nums[prev_fast]
            fast = fast if abs(fast) < len(nums) else fast % len(nums)
            if nums[fast] * nums[prev_fast] < 0 or fast == prev_fast:
                break
            prev_fast = fast
            fast += nums[prev_fast]
            fast = fast if abs(fast) < len(nums) else fast % len(nums)
            if nums[fast] * nums[prev_fast] < 0 or fast == prev_fast:
                break
            if fast == slow:
                return True

    return False


print(circular_array_loop([1, 3, -2, -4, 1]))
