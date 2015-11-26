from _02_04_cyclopeptide_gen import cyclopeptide

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline().strip()
        expected_spectrum = f.readline().split()
    with open('peptide_table.txt', 'r') as f:
        table = {}
        for line in f.readlines():
            letter, w = line.split()
            w = int(w)
            table[letter] = w
    perfect_spectrum = cyclopeptide(text, table)
    score = 0
    i1 = 0
    i2 = 0
    perfect_spectrum = map(int, perfect_spectrum)
    expected_spectrum = map(int, expected_spectrum)
    while i1 < len(perfect_spectrum) and i2 < len(expected_spectrum):
        if perfect_spectrum[i1] == expected_spectrum[i2]:
            score += 1
            i1 += 1
            i2 += 1
        elif perfect_spectrum[i1] > expected_spectrum[i2]:
            i2 += 1
        elif perfect_spectrum[i1] < expected_spectrum[i2]:
            i1 += 1
    with open('out.txt', 'w') as f:
        f.write(str(score))
