import sys

sys.setrecursionlimit(2000)

def vote(a, b, c):
    if a == b and b == c:
        return 1
    else:
        return 0

def get_backtrack(v, w, u):
    n = len(v)
    m = len(w)

    s = [[[0 for k in range(len(u)+1)] for j in range(len(w)+1)] for i in range(len(v)+1)]
    backtrack = [[[0 for k in range(len(u)+1)] for j in range(len(w)+1)] for i in range(len(v)+1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in xrange(1, len(u)+1):
                scores = [s[i-1][j-1][k-1] + vote(v[i-1], w[j-1], u[k-1]),
                          s[i-1][j][k],
                          s[i][j-1][k],
                          s[i][j][k-1],
                          s[i-1][j][k-1],
                          s[i][j-1][k-1]]
                s[i][j][k] = max(scores)
                backtrack[i][j][k] = scores.index(s[i][j][k])
    i = len(v)
    j = len(w)
    k = len(u)
    v_aligned, w_aligned, u_aligned = v, w, u
    max_score = s[i][j][k]
    while i != 0 and j != 0 and k!= 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            w_aligned = w_aligned[:j] + '-' + w_aligned[j:]
            u_aligned = u_aligned[:k] + '-' + u_aligned[k:]
        elif backtrack[i][j][k] == 2:
            j -= 1
            v_aligned = v_aligned[:i] + '-' + v_aligned[i:]
            u_aligned = u_aligned[:k] + '-' + u_aligned[k:]
        elif backtrack[i][j][k] == 3:
            k -= 1
            v_aligned = v_aligned[:i] + '-' + v_aligned[i:]
            w_aligned = w_aligned[:j] + '-' + w_aligned[j:]
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            u_aligned = u_aligned[:k] + '-' + u_aligned[k:]
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            w_aligned = w_aligned[:j] + '-' + w_aligned[j:]
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            v_aligned = v_aligned[:i] + '-' + v_aligned[i:]
        else:
            i -= 1
            j -= 1
            k -= 1

    while len(w_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        w_aligned = w_aligned[:0] + '-' + w_aligned[0:]
    while len(v_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        v_aligned = v_aligned[:0] + '-' + v_aligned[0:]
    while len(u_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        u_aligned = u_aligned[:k] + '-' + u_aligned[k:]

    return max_score, v_aligned, w_aligned, u_aligned


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
        u = f.readline().strip()
    score, v, w, u = get_backtrack(v, w, u)
    print (score)
    print (v)
    print (w)
    print (u)
    # path = list(map(str, path))
    with open('out.txt', 'w') as f:
        f.write('\n'.join([str(score), v, w, u]))
