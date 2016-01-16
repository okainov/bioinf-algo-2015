from _01_02_frequent_words import window
from _01_03_reverse_dna import reverse_dna


def find_all(sub, string):
    # http://stackoverflow.com/a/3874760
    """
    >>> text = "Allowed Hello Hollow"
    >>> tuple(findall('ll', text))
    (1, 10, 16)
    """
    index = 0 - len(sub)
    try:
        while True:
            index = string.index(sub, index + len(sub))
            yield index
    except ValueError:
        pass


def get_kmers(s, k):
    return list(set(["".join(x) for x in window(s, k)]))


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k = int(f.readline())
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    possible_kmers = get_kmers(s1, k)
    result = list()
    for kmer in possible_kmers:
        for first_pos in find_all(kmer, s1):
            for second_pos in find_all(kmer, s2):
                result.append((first_pos, second_pos))
            for second_pos in find_all(reverse_dna(kmer), s2):
                result.append((first_pos, second_pos))

    with open('out.txt', 'w') as f:
        f.write(str('\n'.join(map(str, result))))
