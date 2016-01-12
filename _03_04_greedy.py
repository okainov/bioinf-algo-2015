def profile_most_probable_kmer_swap(dna, k, profile):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}

    max_probability = -1
    most_probable = ''

    for i in range(len(dna)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable
def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search(dna_list, k, t):
    best_score = t*k

    for i in range(len(dna_list[0])-k+1):
        motifs = [dna_list[0][i:i+k]]

        for j in range(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_most_probable_kmer_swap(dna_list[j], k, current_profile))

        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, t = map(int, f.readline().split())
        dnas = f.read().split()

    best_motifs = greedy_motif_search(dnas, k, t)
    with open('out.txt', 'w') as f:
        f.write('\n'.join(best_motifs))
