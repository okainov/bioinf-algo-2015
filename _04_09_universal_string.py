import itertools
import random


def universal_extend(inlist):
    outlist = []
    for elem in inlist:
        outlist.append(elem + '0')
        outlist.append(elem + '1')
    return outlist

def universal_extend_n(n):
    counter = n
    outlist = ['']
    while counter > 0:
        outlist = universal_extend(outlist)
        counter -= 1
    return outlist

def k_universal_graph(k):
    graph = {}
    for node in universal_extend_n(k-1):
        graph[node] = set(universal_extend([node[1:]]))
    return graph

def find_cycle_starting_at(graph, startnode):
    from random import sample

    cycle = [startnode]
    node = startnode
    complete = False
    while not complete:
        sinks = graph[node]
        next = sample(sinks, 1)[0]
        if len(sinks) > 1:
            graph[node] = sinks - set([next])
        else:
            del(graph[node])
        cycle.append(next)
        node = next
        complete = (node == startnode)
    return cycle, graph

def find_cycle(graph):
    startnode = random.choice(list(graph.keys()))
    return find_cycle_starting_at(graph, startnode)

def combine_cycles(cycle, index, new_cycle):
    cycle = cycle[:index] + new_cycle + cycle[index+1:]
    return cycle

def find_eulerian_cycle(graph):
    cycle, remaining_graph = find_cycle(graph)
    while remaining_graph:
        for index, new_start in enumerate(cycle):
            if new_start in remaining_graph:
                new_cycle, remaining_graph = find_cycle_starting_at(remaining_graph, new_start)
                cycle = combine_cycles(cycle, index, new_cycle)
                break
        else:
            raise Exception("Cannot find any nodes from {} in remaining graph {}".format(cycle, remaining_graph))
    return cycle

def overlap_n(a, b, n):
    return a[-n:] == b[:n]

# 57-6
# 57-10
# 59-5
def assemble_path(path):
    sequence = path[0]
    for kmer in path[1:]:
        if overlap_n(sequence, kmer, len(kmer)-1):
            sequence += kmer[-1]
        else:
            raise Exception('kmer {} does not extend existing sequence {}'.format(kmer, sequence))
    return sequence

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        k = int(f.readline())

    graph = k_universal_graph(k)
    cycle = find_eulerian_cycle(graph)

    result = assemble_path(cycle[:-1])[:2**k]

    with open('out.txt', 'w') as f:
        f.write(result)
