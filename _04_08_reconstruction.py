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
        k = int(f.readline())
        dnas = f.read().split()

    k=len(dnas[0])
    edges=[]
    nodes=[]
    patterns=[]
    smegnosty={}
    for r in dnas:
        prefix=r[:-1]
        suffix=r[1:]
        if not(prefix in patterns):
            patterns.append(prefix)
        if not(suffix in patterns):
            patterns.append(suffix)
    for pattern in patterns:
        smegnosty[pattern]=[]
    for r in dnas:
        smegnosty[r[:-1]].append(r[1:])

    result = []
    for key in sorted(smegnosty):
        if not(smegnosty[key]==[]):
            result.append('%s -> %s' % (key, ','.join(smegnosty[key])))

    with open('out.txt', 'w') as f:
        f.write('\n'.join(result))
