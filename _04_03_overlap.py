import random
from _01_02_frequent_words import window
from _03_03_profile import profile_most_probable_kmer
from _03_04_greedy import profile_most_probable_kmer_swap, score, profile
from _03_05_pseudo import profile_with_pseudocounts

def are_adj(kmer_1, kmer_2):
    #for i in range(1, len(kmer_1)):
    if kmer_1[1:] == kmer_2[:len(kmer_1)-1]:
        #if kmer_1[-i:] == kmer_2[:i]:
        return True
    return False

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        dnas = f.read().split()

    result = list()
    for kmer_1 in dnas:
        for kmer2 in dnas:
            if are_adj(kmer_1, kmer2):
                result.append('%s -> %s' % (kmer_1, kmer2))
    with open('out.txt', 'w') as f:
        f.write('\n'.join(result))
