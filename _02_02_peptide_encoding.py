import re
import itertools
from _01_03_reverse_dna import reverse_dna


def translate_prot(text, table):
    elems = re.findall('[A-Z]{3}', text)
    result = ''
    for elem in elems:
        result += table[elem]
    return result


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
        pattern = f.readline()
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

    stuff = []
    # stuff.append(reverse_table[''])
    for letter in pattern:
        stuff.append(reverse_table[letter])
        # stuff.append(reverse_table[''])
    result = []
    # text = text.replace('T', 'U')
    for candidate in itertools.product(*stuff):
        string = ''.join(candidate)
        string = string.replace('U', 'T')
        if string in text:
            result.append(string)
        string = reverse_dna(string)
        if string in text:
            result.append(string)
    with open('out.txt', 'w') as f:
        f.write('\n'.join(result))
