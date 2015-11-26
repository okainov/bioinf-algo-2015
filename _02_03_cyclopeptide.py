import re
import itertools
from _01_03_reverse_dna import reverse_dna


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        n = int(f.readline())
    with open('codon_table.txt', 'r') as f:
        table = {}
        reverse_table = {}
        for line in f.readlines():
            gens, acid = line.split()
            if acid == '""':
                acid = ''
            table[gens] = acid
            if acid not in reverse_table:
                reverse_table[acid] = [gens]
            else:
                reverse_table[acid].append(gens)
        reverse_table[''].append('')

    result = (n-1) * n
    with open('out.txt', 'w') as f:
        f.write(str(result))
