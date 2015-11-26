import copy
import re
import itertools
from _01_03_reverse_dna import reverse_dna

# CYCLOPEPTIDESEQUENCING(Spectrum)
#         Peptides ? a set containing only the empty peptide
#         while Peptides is nonempty
#             Peptides ? Expand(Peptides)
#             for each peptide Peptide in Peptides
#                 if Mass(Peptide) = ParentMass(Spectrum)
#                     if Cyclospectrum(Peptide) = Spectrum
#                         output Peptide
#                     remove Peptide from Peptides
#                 else if Peptide is not consistent with Spectrum
#                     remove Peptide from Peptides

from _02_06_peptide_scoring import score
from _02_04_cyclopeptide_gen import weight, generate_cyclo_spectrum, generate_linear_spectrum

LETTERS = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']


def is_spectrum_consistent(experimental_spectrum, perfect_spectrum):
    temp_spectr = copy.deepcopy(perfect_spectrum)
    for x in experimental_spectrum:
        if x not in temp_spectr:
            return False
        else:
            temp_spectr.remove(x)
    return True


def cyclo_sequence(spectrum, table):
    leaderboard = ['']
    leader_peptides = ['']
    parent_mass = spectrum[-1]
    while len(leaderboard) > 0:
        new_leaderboard = []
        map(lambda x: new_leaderboard.extend([peptide + x for peptide in leaderboard]), LETTERS)
        leaderboard = new_leaderboard
        stuff_to_remove = []
        for peptide in leaderboard:
            if weight(peptide, table) == parent_mass:
                if generate_cyclo_spectrum(peptide, table) == spectrum:
                    leader_peptides.append(peptide)
                stuff_to_remove.append(peptide)
            elif not is_spectrum_consistent(generate_linear_spectrum(peptide, table), perfect_spectrum):
                stuff_to_remove.append(peptide)
        [leaderboard.remove(x) for x in stuff_to_remove]

    return leader_peptides


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        perfect_spectrum = map(int, f.readline().split())
    with open('peptide_table.txt', 'r') as f:
        table = {}
        for line in f.readlines():
            letter, w = line.split()
            w = int(w)
            table[letter] = w
    # peptide = compute_leaderboard(n, perfect_spectrum, table)[0]
    peptides = cyclo_sequence(perfect_spectrum, table)
    full_result = ''
    print len(peptides)
    print peptides
    for peptide in peptides:
        result = '-'.join(map(str, map(lambda x: table[x], peptide)))
        full_result += result + ' '
    with open('out.txt', 'w') as f:
        f.write(str(full_result))
