import copy


def format_permutation(perm):
    permutation = list()
    for i in perm:
        if i < 0:
            permutation.append(str(i))
        else:
            permutation.append('+' + str(i))
    return '(' + ' '.join(permutation) + ')'


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        permutation = list(map(int, f.readline().strip()[1:-1].split()))

    perm_sequence = []
    for i in range(0, len(permutation)):
        desired_elem = i + 1
        if permutation[i] == desired_elem:
            continue
        else:
            try:
                index = permutation.index(desired_elem)
            except:
                index = permutation.index(-desired_elem)
            permutation = permutation[:i] + [-x for x in permutation[i:index + 1:][::-1]] + permutation[index + 1:]
            perm_sequence.append(copy.deepcopy(permutation))

        if permutation[i] == -desired_elem:
            permutation[i] = desired_elem
            perm_sequence.append(permutation)

    with open('out.txt', 'w') as f:
        f.write('\n'.join([format_permutation(perm) for perm in perm_sequence]))
