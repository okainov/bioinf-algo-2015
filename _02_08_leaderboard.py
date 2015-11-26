from _02_06_peptide_scoring import score
from _02_04_cyclopeptide_gen import weight

LETTERS = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']


def compute_leaderboard(n, spectrum, table):
    leaderboard = ['']
    leader_peptides = ['']
    leader_score = score(leader_peptides[0], spectrum, table)
    parent_mass = spectrum[-1]
    peptides_83 = []
    while len(leaderboard) > 0:
        new_leaderboard = []
        map(lambda x: new_leaderboard.extend([peptide + x for peptide in leaderboard]), LETTERS)
        leaderboard = new_leaderboard
        stuff_to_remove = []
        for peptide in leaderboard:
            if weight(peptide, table) == parent_mass:
                if score(peptide, spectrum, table) == 83:
                    peptides_83.append(peptide)
                if score(peptide, spectrum, table) > leader_score:
                    leader_peptides = [peptide]
                    leader_score = score(peptide, spectrum, table)
                elif score(peptide, spectrum, table) == leader_score:
                    leader_peptides.append(peptide)
            elif weight(peptide, table) > parent_mass:
                stuff_to_remove.append(peptide)
        [leaderboard.remove(x) for x in stuff_to_remove]

        def trim(leaderboard, spectrum, N):
            if (len(leaderboard) < N):
                return leaderboard
            temp = []
            for peptide in leaderboard:
                temp.append((peptide, score(peptide, spectrum, table)))
            temp.sort(key=lambda x: x[1], reverse=True)
            edge_score = temp[N - 1][1]
            assert temp[0][1] >= temp[-1][1]
            result = [x[0] for x in temp if x[1] >= edge_score]
            print 'Trimmed length %s against given N=%s' % (len(result), N)
            return result

        leaderboard = trim(leaderboard, spectrum, n)
    print leader_score
    return leader_peptides


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        n = int(f.readline())
        perfect_spectrum = map(int, f.readline().split())
    with open('peptide_table.txt', 'r') as f:
        table = {}
        for line in f.readlines():
            letter, w = line.split()
            w = int(w)
            table[letter] = w
    # peptide = compute_leaderboard(n, perfect_spectrum, table)[0]
    peptides = compute_leaderboard(n, perfect_spectrum, table)
    full_result = ''
    print len(peptides)
    print peptides
    for peptide in peptides:
        result = '-'.join(map(str, map(lambda x: table[x], peptide)))
        full_result += result + ' '
    with open('out.txt', 'a') as f:
        f.write(str(full_result))
