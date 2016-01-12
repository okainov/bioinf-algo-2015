def are_adj(kmer_1, kmer_2):
    #for i in range(1, len(kmer_1)):
    if kmer_1[1:] == kmer_2[:len(kmer_1)-1]:
        #if kmer_1[-i:] == kmer_2[:i]:
        return True
    return False

if __name__ == '__main__':
    graph = dict()
    degrees = dict()
    with open('in.txt', 'r') as f:
        for line in f:
            start, arrow, finish = line.split()
            start = str(start)
            finish_vertexes = list(map(str, finish.split(',')))

            if start not in degrees:
                degrees[start] = len(finish_vertexes)
            else:
                degrees[start] += len(finish_vertexes)
            for vertex in finish_vertexes:
                if vertex not in degrees:
                    degrees[vertex] = 1
                else:
                    degrees[vertex] += 1

            if start not in graph:
                graph[start] = list()
            for vertex in finish_vertexes:
                if vertex not in graph:
                    graph[vertex] = list()

            graph[str(start)] = finish_vertexes

    if not [x for x in degrees if degrees[x]% 2 == 1]:
        start_vertex = '000'
    else:
        start_vertex = [x for x in degrees if degrees[x] % 2 == 1][0]
        second_vertex = [x for x in degrees if degrees[x] % 2 == 1][1]
        if start_vertex not in graph:
            graph[start_vertex] = list()

    #graph[start_vertex].append(second_vertex)

    stack = []
    stack.append(start_vertex)
    result = []
    while len(stack) > 0:
        v = stack[-1]
        if not graph[v]:
            result.append(v)
            stack.pop()
        else:
            to = graph[v].pop()
            stack.append(to)
    result = result[::-1]
    final_result = result
    print (start_vertex)
    if start_vertex != '000':
        print (second_vertex)
        for i in range(len(result)-1):
            if result[i-1] == start_vertex and result[i] == second_vertex:
                final_result = result[i:] + result[:i-1]
                break


    with open('out.txt', 'w') as f:
        f.write('\n'.join(map(str, final_result)))
        f.write('\n----------------------------\n')
        f.write('\n'.join(map(str, result)))
