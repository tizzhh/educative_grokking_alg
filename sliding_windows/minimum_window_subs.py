def min_window(str1: str, str2: str) -> str:
    min_len_sub_seq = float('inf')
    min_sub_seq = ''
    index_s1, index_s2 = 0, 0
    while index_s1 < len(str1):
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1
            if index_s2 == len(str2):
                start, end = index_s1, index_s1
                index_s2 -= 1
                while index_s2 >= 0:
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    start -= 1
                start += 1
                substr = str1[start : end + 1]
                if len(substr) < min_len_sub_seq:
                    min_len_sub_seq = len(substr)
                    min_sub_seq = substr
                index_s2 = 0
                index_s1 = start
        index_s1 += 1
    return min_sub_seq


print(min_window('abcdbebe', 'bbe'))
