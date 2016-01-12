import random
from _01_02_frequent_words import window
from _03_03_profile import profile_most_probable_kmer
from _03_04_greedy import profile_most_probable_kmer_swap, score, profile
from _03_05_pseudo import profile_with_pseudocounts


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k = int(f.readline())
        dna = f.readline().strip()

    substr_kmers = set(["".join(x) for x in window(dna, k)])
    result = sorted(substr_kmers)
    with open('out.txt', 'w') as f:
        f.write('\n'.join(sorted(substr_kmers)))
