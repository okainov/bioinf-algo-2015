import random
from _03_03_profile import profile_most_probable_kmer
from _03_04_greedy import profile_most_probable_kmer_swap, score, profile
from _03_05_pseudo import profile_with_pseudocounts


def motifs_from_profile(profile, dna, k):
    return [profile_most_probable_kmer_swap(seq, k, profile) for seq in dna]

def randomized_motif_search(dnas, k, t, N):
    rand_ints = [random.randint(0,len(dnas[0])-k) for a in range(t)]
    motifs = [dnas[i][r:r+k] for i, r in enumerate(rand_ints)]

    best_score = [score(motifs), motifs]
    for j in range(N):
        i = random.randint(0, t-1)
        profile = profile_with_pseudocounts(motifs[:i-1] + motifs[i:])
        motifs[i] = profile_most_probable_kmer_swap(dnas[i], k, profile)
        current_score = score(motifs)
        if current_score < best_score[0]:
            best_score = [current_score, motifs]
    return best_score


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, t, N = map(int, f.readline().split())
        dnas = f.read().split()

    best_motifs = randomized_motif_search(dnas, k, t, N)
    for i in range(20):
        current_motifs = randomized_motif_search(dnas,k,t, N)
        if current_motifs[0] < best_motifs[0]:
            best_motifs = current_motifs
    with open('out.txt', 'w') as f:
        f.write('\n'.join(best_motifs[1]))
