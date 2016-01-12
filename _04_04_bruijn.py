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
        dna = f.readline().strip()

    edges=[]
    nodes=[]
    d={}
    for i in range(len(dna)-k+1):
        r=dna[i:i+k]
        v=dna[i:i+k-1]
        edges.append(r)
        nodes.append(v)
        if v in d.keys():
            d[v].append(r[1:])
        else:
            temp=[]
            temp.append(r[1:])
            d[v]=temp
    result = []
    for key in d.keys():
        result.append('%s -> %s' % (key, ','.join(d[key])))
    with open('out.txt', 'w') as f:
        f.write('\n'.join(result))
