def find_longest_substring(input_str: str) -> int:
    if not input_str:
        return 0
    longest = 0
    window: dict[str, int] = {}
    start = 0
    for end, cur_char in enumerate(input_str):
        if cur_char in window:
            if start <= window[cur_char] <= end:
                longest = end - start if end - start > longest else longest
                start = window[cur_char] + 1
        window[cur_char] = end

    end += 1
    if longest < end - start:
        longest = end - start
    return longest


print(find_longest_substring('aba'))
