def check_if_is_subdict(
    freq_t: dict[str, int], freq_main: dict[str, int]
) -> bool:
    return all(freq_t[key] <= freq_main.get(key, 0) for key in freq_t)


def min_window(s: str, t: str):
    min_subsr_len = float('inf')
    minimum_susbstr = ''
    start, end = 0, 0
    freq_main = {}
    freq_t = {elem: t.count(elem) for elem in t}
    while end < len(s):
        if s[end] in freq_t:
            freq_main[s[end]] = freq_main.get(s[end], 0) + 1
            while check_if_is_subdict(freq_t, freq_main):
                if end - start + 1 < min_subsr_len:
                    res_start = start
                    res_end = end
                    min_subsr_len = end - start + 1
                if s[start] in freq_main:
                    freq_main[s[start]] -= 1
                start += 1
        end += 1
    return (
        minimum_susbstr
        if min_subsr_len == float('inf')
        else s[res_start : res_end + 1]
    )


print(min_window('ACBBACA', 'ABA'))
