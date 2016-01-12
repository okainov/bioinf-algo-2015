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
    graph = dict()
    with open('in.txt', 'r') as f:
        for line in f:
            start, arrow, finish = line.split()
            graph[str(start)] = list(map(str, finish.split(',')))

    stack = []
    stack.append('000')
    result = []
    while len(stack) > 0:
        v = stack[-1]
        if not graph[v]:
            result.append(v)
            stack.pop()
        else:
            to = graph[v].pop()
            stack.append(to)
    result = result[::-1]

    with open('out.txt', 'w') as f:
        f.write('->'.join(map(str, result)))
