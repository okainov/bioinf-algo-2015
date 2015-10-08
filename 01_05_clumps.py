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


def t_frequent_words(text, k, t):
    kmers = ["".join(x) for x in window(text, k)]
    count_dict = dict()
    for kmer in kmers:
        if kmer not in count_dict:
            count_dict[kmer] = 0
        count_dict[kmer] += 1

    result = [key for key in count_dict if count_dict[key] >= t]
    return result


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()[:-1]
        k, L, t = map(int, f.readline().split())
    result = set()
    for win in ["".join(x) for x in window(text, L)]:
        result.update(set(t_frequent_words(win, k, t)))
    with open('out.txt', 'w') as f:
        f.write(str(' '.join(result)))
