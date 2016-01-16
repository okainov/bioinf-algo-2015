import re


def longest_path(source, sink, edges):
    s = dict()
    s[source] = (0, None)  # Cost, parent
    queue = [source]
    max_cost = 0
    max_vertex = -1
    while len(queue) > 0:
        v_from = queue.pop()
        for v_to in edges[v_from]:
            if v_to not in s:
                s[v_to] = -1, None

            weight = edges[v_from][v_to]
            current_cost, current_parent = s[v_to]
            new_cost = weight + s[v_from][0]
            new_parent = v_from
            if new_cost > current_cost:
                s[v_to] = new_cost, new_parent
            if s[v_to][0] > max_cost:
                max_cost = s[v_to][0]
                max_vertex = v_to
            queue.append(v_to)

    path = []
    current_vertex = max_vertex
    while current_vertex != source:
        path.append(current_vertex)
        current_vertex = s[current_vertex][1]

    path.append(current_vertex)
    return path[::-1], max_cost


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        source = int(f.readline().strip())
        sink = int(f.readline().strip())
        edges = {}
        for line in f.readlines():
            v_from, v_to, weight = map(int, re.findall(r"[0-9']+", line))
            if v_from not in edges:
                edges[v_from] = {}
            if v_to not in edges:
                edges[v_to] = {}
            edges[v_from][v_to] = weight
    path, max_cost = longest_path(source, sink, edges)
    path = list(map(str, path))
    with open('out.txt', 'w') as f:
        f.write('\n'.join([str(max_cost), '->'.join(path)]))
