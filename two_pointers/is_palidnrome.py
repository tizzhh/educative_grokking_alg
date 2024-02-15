def is_palindrome(n: str) -> bool:
    ptr1, ptr2 = 0, len(n) - 1
    while ptr1 < ptr2:
        if n[ptr1] != n[ptr2]:
            return False
        ptr1 += 1
        ptr2 -= 1
    return True


print(is_palindrome("abba"))
