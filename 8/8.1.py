f = open("i", "r")
lines = [[l.split(" ") for l in line.split(" | ")] for line in f.read().split("\n")]

easy_digits = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

counter = 0


def remove_from_list(a, b):
    return [c for c in a if c not in b]


def find_seg_6(len_6_digits, digits):
    for d in len_6_digits:
        seg = remove_from_list(d, digits[7])
        seg = remove_from_list(seg, digits[4])

        if len(seg) == 1:
            return seg[0], d


def find_seq_3(len_5_digits, digits, seg6):
    for d in len_5_digits:
        seg = remove_from_list(d, digits[7])
        seg = remove_from_list(seg, seg6)

        if len(seg) == 1:
            return seg[0], d


def find_seq_1(len_5_digits, digits):
    for d in len_5_digits:
        seg = remove_from_list(d, digits[3])

        if len(seg) == 1:
            return seg[0], d


for line in lines:
    output = line[1]
    input = line[0]
    digits = {}
    s = [0, 0, 0, 0, 0, 0, 0]
    digits_by_length = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    for d in input:
        if len(d) in easy_digits.keys():
            digits[easy_digits[len(d)]] = d

        digits_by_length[len(d)].append(d)

    for d in digits_by_length[5]:
        seg = remove_from_list(d, digits[7])
        seg = remove_from_list(seg, digits[4])

        if len(seg) == 1:
            s[6] = seg[0]

    s[0] = remove_from_list(digits[7], digits[1])[0]
    s[6], digits[9] = find_seg_6(digits_by_length[6], digits)
    s[4] = remove_from_list(digits[8], digits[9])[0]
    s[3], digits[3] = find_seq_3(digits_by_length[5], digits, s[6])
    s[1], digits[5] = find_seq_1(digits_by_length[5], digits)
    s[2] = remove_from_list(digits[9], digits[5])[0]
    s[5] = remove_from_list("abcdefg", s)[0]

    digits[0] = s[0] + s[1] + s[2] + s[4] + s[5] + s[6]
    digits[2] = s[0] + s[2] + s[3] + s[4] + s[6]
    digits[6] = s[0] + s[1] + s[3] + s[4] + s[5] + s[6]
    digits[9] = s[0] + s[1] + s[2] + s[3] + s[5] + s[6]

    for d in output:
        if len(d) in easy_digits.keys():
            counter += 1

print(counter)
