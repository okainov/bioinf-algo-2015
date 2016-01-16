from _05_05_glob_align import get_backtrack

if __name__ == '__main__':
    scoring_matrix = {}
    with open('SIMPLE.txt') as input_data:
        for line in input_data.readlines():
            letter_from, letter_to, cost = line.strip().split()
            cost = int(cost)
            if letter_from not in scoring_matrix:
                scoring_matrix[letter_from] = {}
            scoring_matrix[letter_from][letter_to] = cost

    with open('in.txt', 'r') as f:
        v = f.readline().strip()
        w = f.readline().strip()
    score, v, w = get_backtrack(v, w, scoring_matrix, indel=1)
    print (-score)
    # path = list(map(str, path))
    # with open('out.txt', 'w') as f:
    #     f.write('\n'.join([str(max_cost), '->'.join(path)]))
