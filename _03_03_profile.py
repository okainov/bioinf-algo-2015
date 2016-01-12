def profile_most_probable_kmer(dna, k, profile):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}

    max_probability = -1
    most_probable = ''

    for i in range(len(dna)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[nuc_loc[nucleotide]][j]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        dna = f.readline().strip()
        k = int(f.readline())
        profile = [list(map(float, line.strip().split())) for line in f.readlines()]

    most_probable = profile_most_probable_kmer(dna, k, profile)

    with open('out.txt', 'w') as f:
        f.write(most_probable)