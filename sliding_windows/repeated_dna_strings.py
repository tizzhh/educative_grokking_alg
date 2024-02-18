# def find_repeated_sequences(s: str, k: int) -> set[str]:
#     found = set()
#     duplicates = set()
#     for i in range(0, len(s) - k):
#         substr = s[i:i + k]
#         if substr in found:
#             duplicates.add(substr)
#         found.add(substr)

#     return duplicates


def find_repeated_sequences(s: str, k: int) -> set[str]:
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    a = 4
    numbers = [mapping[i] for i in s]
    hash_val = 0
    hash_set, output = set(), set()
    for i in range(0, len(s) - k + 1):
        if i == 0:
            for j in range(k):
                hash_val += numbers[j] * (a ** (k - j - 1))
        else:
            prev_hash = hash_val
            hash_val = (
                prev_hash - numbers[i - 1] * (a ** (k - 1))
            ) * 4 + numbers[i + k - 1]

        if hash_val in hash_set:
            output.add(s[i : i + k])
        hash_set.add(hash_val)

    return output


print(find_repeated_sequences('AAAAACCCCCAAAAACCCCCC', 8))
