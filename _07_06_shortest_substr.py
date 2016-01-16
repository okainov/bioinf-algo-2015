from _01_02_frequent_words import window


def common_subst(text1, text2):
    for k in range(1, min([len(text1), len(text2)])):
        for kmer in ["".join(x) for x in window(text1, k)]:
            if kmer not in text2:
                return kmer
    return None


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text1 = f.readline().strip()
        text2 = f.readline().strip()

    result = common_subst(text1, text2)
    with open('out.txt', 'w') as f:
        f.write(str(result))
