def min_skew(text):
    skew = 0
    min_skew_value = 0
    skew_indexes = list()
    for i, c in enumerate(text, 1):
        if c == 'C':
            skew -= 1
        elif c == 'G':
            skew += 1
        if skew < min_skew_value:
            min_skew_value = skew
            skew_indexes = [i]
        elif skew == min_skew_value:
            skew_indexes.append(i)
    return skew_indexes

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
    skew_indexes = min_skew(text)
    with open('out.txt', 'w') as f:
        f.write(' '.join(map(str, skew_indexes)))
