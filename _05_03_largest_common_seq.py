import sys

sys.setrecursionlimit(2000)


def get_backtrack(v, w):
    n = len(v)
    m = len(w)

    s = {0: {}}
    backtrack = {}
    s[0][0] = 0

    for i in range(1, n + 1):
        s[i] = dict()
        backtrack[i] = dict()
        s[i][0] = 0

    for j in range(1, m + 1):
        s[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max([s[i - 1][j], s[i][j - 1]])
            if v[i - 1] == w[j - 1]:
                s[i][j] = max([s[i][j], s[i - 1][j - 1] + 1])
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = 'down'
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = 'right'
            elif s[i][j] == s[i - 1][j - 1] + 1 and v[i - 1] == w[j - 1]:
                backtrack[i][j] = 'diag'
    return backtrack


def lcs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return
    if backtrack[i][j] == 'down':
        lcs(backtrack, v, i - 1, j)
    elif backtrack[i][j] == 'right':
        lcs(backtrack, v, i, j - 1)
    else:
        lcs(backtrack, v, i - 1, j - 1)
        print(v[i - 1])


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    backtrack = get_backtrack(s, t)
    lcs(backtrack, s, len(s), len(t))
    # with open('out.txt', 'w') as f:
    #    f.write(str(result))
