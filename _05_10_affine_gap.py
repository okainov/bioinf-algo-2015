import sys

sys.setrecursionlimit(2000)


def get_backtrack(v, w, scoring_matrix, sigm, eps):
    n = len(v)
    m = len(w)

    s = {0: {0: {}},
         1: {0: {}},
         2: {0: {}}, }
    backtrack = {0: {}, 1: {}, 2: {}}
    for i in xrange(len(v) + 1):
        s[0][i] = {j: 0 for j in xrange(len(w) + 1)}
        s[1][i] = {j: 0 for j in xrange(len(w) + 1)}
        s[2][i] = {j: 0 for j in xrange(len(w) + 1)}
        backtrack[0][i] = {j: 0 for j in xrange(len(w) + 1)}
        backtrack[1][i] = {j: 0 for j in xrange(len(w) + 1)}
        backtrack[2][i] = {j: 0 for j in xrange(len(w) + 1)}

    for i in range(1, n + 1):
        s[0][i][0] = -sigm - (i - 1) * eps
        s[1][i][0] = -sigm - (i - 1) * eps
        s[2][i][0] = -10 * sigm

    for j in range(1, m + 1):
        s[0][0][j] = -10 * sigm
        s[1][0][j] = -sigm - (j - 1) * eps
        s[2][0][j] = -sigm - (j - 1) * eps

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            lower_scores = [s[0][i - 1][j] - eps, s[1][i - 1][j] - sigm]
            s[0][i][j] = max(lower_scores)
            backtrack[0][i][j] = lower_scores.index(s[0][i][j])

            upper_scores = [s[2][i][j - 1] - eps, s[1][i][j - 1] - sigm]
            s[2][i][j] = max(upper_scores)
            backtrack[2][i][j] = upper_scores.index(s[2][i][j])

            middle_scores = [s[0][i][j], s[1][i - 1][j - 1] + scoring_matrix[v[i - 1]][w[j - 1]], s[2][i][j]]
            s[1][i][j] = max(middle_scores)
            backtrack[1][i][j] = middle_scores.index(s[1][i][j])

    i = n
    j = m
    v_aligned, w_aligned = v, w

    matrix_scores = [s[0][i][j], s[1][i][j], s[2][i][j]]
    max_score = max(matrix_scores)
    backtrack_matrix = matrix_scores.index(max_score)

    while i != 0 and j != 0:
        if backtrack_matrix == 0:
            if backtrack[0][i][j] == 1:
                backtrack_matrix = 1

            i -= 1
            w_aligned = w_aligned[:j] + '-' + w_aligned[j:]
        elif backtrack_matrix == 1:
            if backtrack[1][i][j] == 0:
                backtrack_matrix = 0
            elif backtrack[1][i][j] == 2:
                backtrack_matrix = 2
            else:
                i -= 1
                j -= 1
        else:
            if backtrack[2][i][j] == 1:
                backtrack_matrix = 1
            j -= 1
            v_aligned = v_aligned[:i] + '-' + v_aligned[i:]

    while i != 0:
        w_aligned = w_aligned[:0] + '-' + w_aligned[0:]
        i -= 1
    while j != 0:
        v_aligned = v_aligned[:0] + '-' + v_aligned[0:]
        j -= 1

    return max_score, v_aligned, w_aligned


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

    max_score, good_v, good_w = get_backtrack(v, w, scoring_matrix, 11, 1)
    print (max_score)
    print (good_v)
    print (good_w)
    # path = list(map(str, path))
    # with open('out.txt', 'w') as f:
    #     f.write('\n'.join([str(max_cost), '->'.join(path)]))
