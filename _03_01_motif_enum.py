from _01_07_hamming_distance import hamming_distance
from _01_02_frequent_words import window
from _01_10_most_freq_with_mismatches import generate_words_with_mismatches


def enumerate_motifs(dnas, k, d):
    kmers = []
    for text in dnas:
        kmers.extend(["".join(x) for x in window(text, k)])
    resulting_set = set()
    for kmer in kmers:
        for modified_kmer in generate_words_with_mismatches(kmer, d):
            will_add = True
            for text in dnas:
                was_found = False
                for fragment in ["".join(x) for x in window(text, k)]:
                    if hamming_distance(fragment, modified_kmer) <= d:
                        was_found = True
                        break
                if not was_found:
                    will_add = False
                    break
            if will_add:
                resulting_set.add(modified_kmer)
    return list(resulting_set)


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, d = map(int, f.readline().split())
        dnas = f.read().split()

    patterns = enumerate_motifs(dnas, k, d)

    with open('out.txt', 'w') as f:
        f.write(' '.join(patterns))
