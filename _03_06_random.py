import random
from _03_03_profile import profile_most_probable_kmer
from _03_04_greedy import profile_most_probable_kmer_swap, score, profile
from _03_05_pseudo import profile_with_pseudocounts


def motifs_from_profile(profile, dna, k):
    return [profile_most_probable_kmer_swap(seq, k, profile) for seq in dna]

def randomized_motif_search(dnas, k, t):
    rand_ints = [random.randint(0,len(dnas[0])-k) for a in range(t)]
    motifs = [dnas[i][r:r+k] for i, r in enumerate(rand_ints)]

    best_score = [score(motifs), motifs]
    while True:
        profile = profile_with_pseudocounts(motifs)
        motifs = motifs_from_profile(profile, dnas, k)
        current_score = score(motifs)
        if current_score < best_score[0]:
            best_score = [current_score, motifs]
        else:
            return best_score


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, t = map(int, f.readline().split())
        dnas = f.read().split()

    best_motifs = randomized_motif_search(dnas, k, t)
    for i in range(1000):
        current_motifs = randomized_motif_search(dnas,k,t)
        if current_motifs[0] < best_motifs[0]:
            best_motifs = current_motifs
    with open('out.txt', 'w') as f:
        f.write('\n'.join(best_motifs[1]))
