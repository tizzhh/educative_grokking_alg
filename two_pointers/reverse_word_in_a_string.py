def reverse_words(sentence: str) -> str:
    res = ''
    string = sentence.strip()[::-1]
    start, end = 0, 0
    while end < len(string):
        if string[end] == ' ':
            res += string[start:end][::-1] + ' '
            while end < len(string) and string[end] == ' ':
                end += 1
            start = end
        end += 1
    if end == len(string):
        res += string[start:end][::-1]
    return res


print(reverse_words("We Love Java"))
