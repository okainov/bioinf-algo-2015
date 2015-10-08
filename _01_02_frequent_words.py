import itertools


def window(seq, n=2):
    """
    http://stackoverflow.com/questions/7636004/python-split-string-in-moving-window
    Returns a sliding window (of width n) over data from the iterable
      s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """

    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def frequent_words(text, k):
    kmers = ["".join(x) for x in window(text, k)]
    count_dict = dict()
    max_count = 0
    for kmer in kmers:
        if kmer not in count_dict:
            count_dict[kmer] = 0
        count_dict[kmer] += 1
        if count_dict[kmer] > max_count:
            max_count = count_dict[kmer]

    result = [key for key in count_dict if count_dict[key] == max_count]
    return result


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
        k = int(f.readline())
    result = frequent_words(text, k)
    with open('out.txt', 'w') as f:
        f.write(str(' '.join(result)))
