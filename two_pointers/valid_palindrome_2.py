def _check_sub_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if _check_sub_palindrome(s[left:right]):
                return True
            elif _check_sub_palindrome(s[left + 1 : right + 1]):
                return True
            else:
                return False
        left += 1
        right -= 1

    return True


print(is_palindrome('abceba'))
