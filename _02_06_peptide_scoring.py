from _02_04_cyclopeptide_gen import cyclopeptide


def score(peptide, perfect_spectrum, table):
    actual_spectrum = cyclopeptide(peptide, table)
    result_score = 0
    i1 = 0
    i2 = 0
    actual_spectrum = map(int, actual_spectrum)
    perfect_spectrum = map(int, perfect_spectrum)
    while i1 < len(actual_spectrum) and i2 < len(perfect_spectrum):
        if actual_spectrum[i1] == perfect_spectrum[i2]:
            result_score += 1
            i1 += 1
            i2 += 1
        elif actual_spectrum[i1] > perfect_spectrum[i2]:
            i2 += 1
        elif actual_spectrum[i1] < perfect_spectrum[i2]:
            i1 += 1
    return result_score


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline().strip()
        perfect_spectrum = f.readline().split()
    with open('peptide_table.txt', 'r') as f:
        table = {}
        for line in f.readlines():
            letter, w = line.split()
            w = int(w)
            table[letter] = w
    n_score = score(text, perfect_spectrum)
    with open('out.txt', 'w') as f:
        f.write(str(n_score))
