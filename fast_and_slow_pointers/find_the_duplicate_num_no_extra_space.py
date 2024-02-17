def find_duplicate(nums: list[int]) -> int:
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast


# def find_duplicate(nums: list[int]) -> int:
#     nums.sort()
#     slow, fast = 0, 1
#     while True:
#         if nums[slow] == nums[fast]:
#             return nums[fast]
#         slow += 1
#         fast += 1

print(find_duplicate([1, 3, 3, 4, 2, 5]))
