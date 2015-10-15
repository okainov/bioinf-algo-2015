from _01_02_frequent_words import window
from _01_03_reverse_dna import reverse_dna
from _01_09_approx_pattern_count import approx_pattern_count
from _01_10_most_freq_with_mismatches import generate_words_with_mismatches


def frequent_words_with_mismatch(text, kmers, d):
    count_dict = dict()
    max_count = 0
    visited_kmers = set()
    for kmer in kmers:
        app = approx_pattern_count(text, kmer, d) + approx_pattern_count(text, reverse_dna(kmer), d)
        if app > 0 and kmer not in visited_kmers:
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

    substr_kmers = set(["".join(x) for x in window(text, k)])
    kmers = set()
    for kmer in substr_kmers:
        kmers.update(set(generate_words_with_mismatches(kmer, d)))

    result, max_count = frequent_words_with_mismatch(text, kmers, d)

    with open('out.txt', 'w') as f:
        f.write(str(' '.join(result)))

