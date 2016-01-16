if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        permutation = list(map(int, f.readline().strip()[1:-1].split()))

    result = 0
    for i in range(1, len(permutation)):
        if permutation[i] - permutation[i - 1] != 1:
            result += 1

    with open('out.txt', 'w') as f:
        f.write(str(result))
