def longest_repeating_character_replacement(s: str, k: int) -> int:
    start, end = 0, 0
    most_freq_char = 1
    length_of_max_substr = 1
    freq = {}
    freq[s[end]] = 1
    while end < len(s):
        if not (end - start + 1 == length_of_max_substr):
            freq[s[end]] = freq.get(s[end], 0) + 1
            most_freq_char = max(freq.values())
            if sum(freq.values()) - most_freq_char <= k:
                length_of_max_substr += 1
            else:
                freq[s[start]] -= 1
                start += 1
        end += 1
    return length_of_max_substr


print(longest_repeating_character_replacement('aabccbb', 2))
