# def is_happy_number(n: int):
#     slow, fast = n, sum(map(lambda x: pow(x, 2), (int(elem) for elem in str(n))))
#     while fast != 1 and fast != slow:
#         slow, fast = sum(map(lambda x: pow(x, 2), (int(elem) for elem in str(slow)))), sum(map(lambda x: pow(x, 2), (int(elem) for elem in str(sum(map(lambda x: pow(x, 2), (int(elem) for elem in str(fast))))))))

#     return fast == 1

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         slow, fast = n, sum(int(i)**2 for i in str(n))
#         while fast != 1 and fast != slow:
#             slow, fast = sum(int(i)**2 for i in str(slow)), sum(int(i)**2 for i in str(sum(int(i)**2 for i in str(fast))))

#         return fast == 1


# best solution
class Solution:
    def isHappy(self, n: int) -> bool:
        already_calc = []
        elem = sum(int(i) ** 2 for i in str(n))
        already_calc.append(elem)
        while elem != 1:
            elem = sum(int(i) ** 2 for i in str(elem))
            if elem in already_calc:
                return False
            already_calc.append(elem)

        return elem == 1


s = Solution()
print(s.isHappy(28))
