from compiler.ast import flatten


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
        kmers = f.read().split()

    edges = {}
    for kmer in kmers:
        if kmer[:-1] in edges:
            edges[kmer[:-1]].append(kmer[1:])
        else:
            edges[kmer[:-1]] = [kmer[1:]]

    # Determine the balanced and unbalanced edges.
    balanced, unbalanced = [], []
    out_values = reduce(lambda a,b: a+b, edges.values())
    for node in set(out_values+edges.keys()):
        out_value = out_values.count(node)
        if node in edges:
            in_value = len(edges[node])
        else:
            in_value = 0

        if in_value == out_value == 1:
            balanced.append(node)
        else:
            unbalanced.append(node)

    # Generate the contigs.
    get_contigs = lambda s, c: flatten([c+e[-1] if e not in balanced else get_contigs(e,c+e[-1]) for e in edges[s]])
    contigs = sorted(flatten([get_contigs(start,start) for start in set(unbalanced) & set(edges.keys())]))

    with open('out.txt', 'w') as f:
        f.write('\n'.join(contigs))
