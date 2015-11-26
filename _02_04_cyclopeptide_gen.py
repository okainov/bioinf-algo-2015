import re
import itertools
from _01_03_reverse_dna import reverse_dna


def weight(codon, table):
    result = 0
    for letter in codon:
        result += table[letter]
    return result

def generate_cyclo_spectrum(text, table):
    n = len(text)
    text = text * 2
    codon_weights = []
    for i in range(1, n):  # length
        for start in range(0, n):  # start position
            codon = text[start:start + i]
            codon_weights.append(weight(codon, table))
    codon_weights.append(0)
    codon_weights.append(weight(text[:n], table))
    codon_weights.sort()
    codon_weights = map(str, codon_weights)
    return map(int, codon_weights)

def generate_linear_spectrum(text, table):
    n = len(text)
    codon_weights = []
    for i in range(1, n+1):  # length
        for start in range(0, n-i+1):  # start position
            codon = text[start:start + i]
            codon_weights.append(weight(codon, table))
    codon_weights.append(0)
    #codon_weights.append(weight(text[:n], table))
    codon_weights.sort()
    codon_weights = map(str, codon_weights)
    return map(int,codon_weights)


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
    with open('peptide_table.txt', 'r') as f:
        table = {}
        for line in f.readlines():
            letter, w = line.split()
            w = int(w)
            table[letter] = w
    codon_weights = generate_cyclo_spectrum(text, table)
    with open('out.txt', 'w') as f:
        f.write(' '.join(codon_weights))
