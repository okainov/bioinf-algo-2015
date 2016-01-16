from _01_02_frequent_words import window
from _06_05_shared_kmers import find_all


def repeat_subst(text):
    for k in range(len(text), 1, -1):
        for kmer in ["".join(x) for x in window(text, k)]:
            if len(list(find_all(kmer, text))) > 1:
                return kmer
    return None


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline().strip()

    result = repeat_subst(text)
    with open('out.txt', 'w') as f:
        f.write(str(result))
