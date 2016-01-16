import sys

sys.setrecursionlimit(2000)


def get_backtrack(v, w, scoring_matrix, indel=5):
    n = len(v)
    m = len(w)

    s = [[i * j * indel for j in range(-1, 1)] for i in range(len(v) + 1)]
    s[0][1] = -indel
    backtrack = [0] * (n + 1)

    for j in range(1, m / 2 + 1):
        for i in range(0, n + 1):
            if i == 0:
                s[i][1] = -j * indel
            else:
                scores = [s[i - 1][0] + scoring_matrix[v[i - 1]][w[j - 1]], s[i][0] - indel, s[i - 1][1] - indel]
                s[i][1] = max(scores)
                backtrack[i] = scores.index(s[i][1])
        if j != m / 2:
            s = [[row[1]] * 2 for row in s]

    return [row[1] for row in s], backtrack


def middle_edge(v, w, scoring_matrix, indel=5):
    source_to_middle = get_backtrack(v, w, scoring_matrix, indel)[0]

    if len(w) % 2 == 1 and len(w) > 1:
        temp_w = '#' + w
    else:
        temp_w = w
    middle_to_sink, backtrack = get_backtrack(v[::-1], temp_w[::-1], scoring_matrix, indel)
    middle_to_sink, backtrack = middle_to_sink[::-1], backtrack[::-1]

    scores = map(sum, zip(source_to_middle, middle_to_sink))

    max_score = max(scores)
    max_middle = scores.index(max_score)

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w) / 2 + 1)
    else:
        next_node = [(max_middle + 1, len(w) / 2 + 1),
                     (max_middle, len(w) / 2 + 1),
                     (max_middle + 1, len(w) / 2)][backtrack[max_middle]]

    return (max_middle, len(w) / 2), next_node


if __name__ == '__main__':
    scoring_matrix = {}
    with open('BLOSUM62.txt') as input_data:
        for line in input_data.readlines():
            letter_from, letter_to, cost = line.strip().split()
            cost = int(cost)
            if letter_from not in scoring_matrix:
                scoring_matrix[letter_from] = {}
            scoring_matrix[letter_from][letter_to] = cost

    with open('in.txt', 'r') as f:
        v = f.readline().strip()
        w = f.readline().strip()

    middle = middle_edge(v, w, scoring_matrix)
    print (middle)
    # path = list(map(str, path))
    # with open('out.txt', 'w') as f:
    #     f.write('\n'.join([str(max_cost), '->'.join(path)]))
