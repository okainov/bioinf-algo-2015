from collections import Counter
import heapq
from itertools import product, izip, ifilter


def select_spectrum(Spectrum,M):
    poten = [pt1-pt2 for pt1,pt2 in product(Spectrum,Spectrum) if pt1-pt2 >= 57 and pt1-pt2 <= 200]
    lst = Counter(poten).most_common()
    tie = heapq.nlargest(M,lst,key=lambda x:x[1])[-1][1]
    res = list(ifilter(lambda x: x[1]>=tie, lst))
    return list(izip(*res))[0]

def score(theorectical_spectrum,experimental_spectrum):
    return len(list((Counter(theorectical_spectrum) & Counter(experimental_spectrum)).elements()))

def generate_subspectrums(peptide):
    l = len(peptide)
    looped = peptide + peptide
    return [0,sum(peptide)]+[sum(looped[start:start+length]) for start,length in product(range(0,l),range(1,l))]

def cut(Leaderboard,Spectrum,N):
    if len(Leaderboard) > N:
        results = []
        for Peptide in Leaderboard:
            try:
                Peptide_experimental_spectrum = generate_subspectrums(Peptide)
            except:
                Peptide = Peptide[0]+[Peptide[1]]
                Peptide_experimental_spectrum = generate_subspectrums(Peptide)
            results.append((Peptide,score(Spectrum,Peptide_experimental_spectrum)))
        tie = heapq.nlargest(N,results,key=lambda x: x[1])[-1][1]
        res = list(ifilter(lambda x: x[1]>=tie,results))
        return list(izip(*res))[0]
    else:
        return Leaderboard

def LeaderboardCyclopeptideSequencing(M,N,Spectrum):
    Leaderboard = [0]
    LeaderPeptide = []
    table = select_spectrum(Spectrum,M)
    while Leaderboard != []:
        Leaderboard = [list(pt) for pt in product(Leaderboard,table)]
        for Peptide in Leaderboard:
            try:
                Peptide_experimental_spectrum = generate_subspectrums(Peptide)
            except:
                Leaderboard = [Peptide[0]+[Peptide[1]] if x == Peptide else x for x in Leaderboard]
                Peptide = Peptide[0]+[Peptide[1]]
                Peptide_experimental_spectrum = generate_subspectrums(Peptide)
            if max(Peptide_experimental_spectrum) == max(Spectrum):
                LeaderPeptide_experimental_spectrum = generate_subspectrums(LeaderPeptide)
                if score(Spectrum,Peptide_experimental_spectrum) > score(Spectrum,LeaderPeptide_experimental_spectrum):
                    LeaderPeptide = Peptide
            elif max(Peptide_experimental_spectrum) > max(Spectrum):
                Leaderboard.remove(Peptide)
        Leaderboard = cut(Leaderboard,Spectrum,N)
    return LeaderPeptide


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        m = int(f.readline())
        n = int(f.readline())
        spectrum = map(int, f.readline().split())

    results = LeaderboardCyclopeptideSequencing(m,n,spectrum)

    with open('out.txt', 'w') as f:
        f.write('-'.join(map(str,results[1:])))
