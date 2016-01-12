from _01_07_hamming_distance import hamming_distance
from _01_02_frequent_words import window
from _01_10_most_freq_with_mismatches import generate_words_with_mismatches


def distance(kmer, string, k):
    result = k+2
    for fragment in ["".join(x) for x in window(string, k)]:
        if hamming_distance(kmer, fragment) < result:
            result = hamming_distance(kmer, fragment)
    return result

def d(kmer, dnas, k):
    result = 0
    for dna in dnas:
        result += distance(kmer, dna, k)
    return result

def median(dnas, k):
    kmers = set()
    for dna in dnas:
        substr_kmers = set(["".join(x) for x in window(dna, k)])
        for kmer in substr_kmers:
            kmers.update(set(generate_words_with_mismatches(kmer, k)))
    opt_kmer = ''
    opt_distance = len(dnas)*k + 1
    for kmer in kmers:
        if opt_distance > d(kmer, dnas, k):
            opt_distance = d(kmer, dnas, k)
            opt_kmer = kmer
    return opt_kmer, opt_distance

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k = int(f.readline().strip())
        dnas = f.read().split()

    opt_kmer, opt_dist = median(dnas, k)

    with open('out.txt', 'w') as f:
        f.write(opt_kmer)
