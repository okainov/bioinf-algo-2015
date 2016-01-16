from _01_02_frequent_words import window


def common_subst(text1, text2):
    for k in range(min([len(text1), len(text2)]), 1, -1):
        for kmer in ["".join(x) for x in window(text1, k)]:
            if kmer in text2:
                return kmer


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text1 = f.readline()
        text2 = f.readline()

    result = common_subst(text1, text2)
    with open('out.txt', 'w') as f:
        f.write(str(result))
