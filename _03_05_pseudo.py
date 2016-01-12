from _03_04_greedy import profile_most_probable_kmer_swap, score


def profile_with_pseudocounts(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search_pseudocounts(dnas, k, t):
    best_score = t*k

    for i in range(len(dnas[0]) - k + 1):
        motifs = [dnas[0][i:i + k]]

        for j in range(1, t):
            current_profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer_swap(dnas[j], k, current_profile))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, t = map(int, f.readline().split())
        dnas = f.read().split()

    best_motifs = greedy_motif_search_pseudocounts(dnas, k, t)
    with open('out.txt', 'w') as f:
        f.write('\n'.join(best_motifs))
