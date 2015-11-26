from _02_06_peptide_scoring import score
from _02_04_cyclopeptide_gen import weight

LETTERS = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']


def compute_leaderboard(n, spectrum, table):
    leaderboard = ['']
    leader_peptide = ''
    leader_score = score(leader_peptide, spectrum, table)
    parent_mass = spectrum[-1]
    while len(leaderboard) > 0:
        new_leaderboard = []
        map(lambda x: new_leaderboard.extend([peptide + x for peptide in leaderboard]), LETTERS)
        leaderboard = new_leaderboard
        stuff_to_remove = []
        for peptide in leaderboard:
            if weight(peptide, table) == parent_mass:
                if score(peptide, spectrum, table) > leader_score:
                    leader_peptide = peptide
                    leader_score = score(peptide, spectrum, table)
            elif weight(peptide, table) > parent_mass:
                stuff_to_remove.append(peptide)
        [leaderboard.remove(x) for x in stuff_to_remove]

        def trim(leaderboard, spectrum, N):
            temp = []
            for peptide in leaderboard:
                temp.append((peptide, score(peptide, spectrum, table)))
            temp.sort(key=lambda x: x[1])
            return [x[0] for x in temp[-N:]]

        leaderboard = trim(leaderboard, spectrum, n)
    return leader_peptide


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
    peptide = compute_leaderboard(n, perfect_spectrum, table)
    result = '-'.join(map(str, map(lambda x: table[x], peptide)))
    with open('out.txt', 'w') as f:
        f.write(str(result))
