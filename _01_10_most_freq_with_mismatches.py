import itertools

from _01_02_frequent_words import window
from _01_09_approx_pattern_count import approx_pattern_count


def generate_words_with_mismatches(s, d=2):
    # http://stackoverflow.com/questions/19822847/how-to-generate-all-strings-with-d-mismatches-python
    N = len(s)
    letters = 'ACGT'
    pool = list(s)

    for indices in itertools.combinations(range(N), d):
        for replacements in itertools.product(letters, repeat=d):
            skip = False
            for i, a in zip(indices, replacements):
                if pool[i] == a:
                    skip = True
            if skip:
                continue

            keys = dict(zip(indices, replacements))
            yield ''.join([pool[i] if i not in indices else keys[i]
                           for i in range(N)])


def frequent_words_with_mismatch(text, kmers, d):
    count_dict = dict()
    max_count = 0
    for kmer in kmers:
        app = approx_pattern_count(text, kmer, d)
        if app > 0:
            if kmer not in count_dict:
                count_dict[kmer] = 0
            count_dict[kmer] += app
            if count_dict[kmer] > max_count:
                max_count = count_dict[kmer]

    result = [key for key in count_dict if count_dict[key] == max_count]
    return result, max_count


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().split())

    kmers = set(["".join(x) for x in window(text, k)])
    result, max_count = frequent_words_with_mismatch(text, kmers, d)
    kmers = list()
    for base_word in result:
        kmers.extend(list(generate_words_with_mismatches(base_word, d)))
    result, max_count = frequent_words_with_mismatch(text, kmers, d)

    with open('out.txt', 'w') as f:
        f.write(str(' '.join(result)))

