def two_break_dist(P, Q):
    graph = {}
    for perm_cycle in P + Q:
        L = len(perm_cycle)
        for i in range(len(perm_cycle)):
            if perm_cycle[i] not in graph:
                graph[perm_cycle[i]] = []
            if -1 * perm_cycle[(i + 1) % L] not in graph:
                graph[-1 * perm_cycle[(i + 1) % L]] = []
            graph[perm_cycle[i]].append(-1 * perm_cycle[(i + 1) % L])
            graph[-1 * perm_cycle[(i + 1) % L]].append(perm_cycle[i])

    component_count = 0
    remaining = set(graph.keys())
    while len(remaining) > 0:
        component_count += 1
        queue = [remaining.pop()]
        while len(queue) > 0:
            current = queue.pop(0)
            if current in graph:
                queue += [node for node in graph[current] if node in remaining]
            remaining -= set(queue)

    return sum(map(len, P)) - component_count


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in f.readlines()]
        P = [list(map(int, block.split())) for block in P]
        Q = [list(map(int, block.split())) for block in Q]

    result = two_break_dist(P, Q)

    with open('out.txt', 'w') as f:
        f.write(str(result))
