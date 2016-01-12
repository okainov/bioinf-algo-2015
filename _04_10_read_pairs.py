def eulerian_cycle(edge_dict):
    current_node = edge_dict.keys()[0]
    path = [current_node]

    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break

    while len(edge_dict) > 0:
        for i in range(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

def eulerian_path(edge_dict):
    out_values = reduce(lambda a,b: a+b, edge_dict.values())
    for node in set(out_values+edge_dict.keys()):
        out_value = out_values.count(node)
        if node in edge_dict:
            in_value = len(edge_dict[node])
        else:
            in_value = 0

        if in_value < out_value:
            unbalanced_from = node
        elif out_value < in_value:
            unbalanced_to = node

    if unbalanced_from in edge_dict:
        edge_dict[unbalanced_from].append(unbalanced_to)
    else:
        edge_dict[unbalanced_from] = [unbalanced_to]

    cycle = eulerian_cycle(edge_dict)

    divide_point = filter(lambda i: cycle[i:i+2] == [unbalanced_from, unbalanced_to], range(len(cycle)-1))[0]

    return cycle[divide_point+1:]+cycle[1:divide_point+1]


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k, d = map(int, f.readline().split())
        paired_reads = [line.strip().split('|') for line in f.readlines()]

    paired_dict = {}
    for pair in paired_reads:
        if (pair[0][:-1],pair[1][:-1]) in paired_dict:
            paired_dict[(pair[0][:-1],pair[1][:-1])].append((pair[0][1:],pair[1][1:]))
        else:
            paired_dict[(pair[0][:-1],pair[1][:-1])] = [(pair[0][1:],pair[1][1:])]

    paired_path = eulerian_path(paired_dict)

    strings = [paired_path[0][i] + ''.join(map(lambda x: x[i][-1], paired_path[1:])) for i in range(2)]
    text = strings[0][:k+d]+strings[1]

    with open('out.txt', 'w') as f:
        f.write(text)
