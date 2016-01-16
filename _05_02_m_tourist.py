def m_tourist(n, m, down, right):
    s = dict()
    s[0] = dict()
    s[0][0] = 0
    for i in range(1, n + 1):
        s[i] = dict()
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max([s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1]])
    return s[n][m]


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        n, m = map(int,f.readline().split())
        down = []
        right = []
        for i in range(n):
            down.append(list(map(int,f.readline().split())))
        f.readline()
        for i in range(n+1):
            right.append(list(map(int,f.readline().split())))
    result = m_tourist(n, m, down, right)
    with open('out.txt', 'w') as f:
        f.write(str(result))