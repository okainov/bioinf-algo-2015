class Trie:
    def __init__(self):
        self.nodes = list()
        self.nodes.append(dict())
        self.number = 1

    def add_elem(self, pattern):
        current_node = self.nodes[0]  # Root
        for letter in pattern:
            if letter not in current_node:
                self.nodes.append(dict())
                current_node[letter] = self.number
                self.number += 1
            current_node = self.nodes[current_node[letter]]

    def __str__(self):
        result = ''
        for i, node in enumerate(self.nodes):
            for key in node:
                result += '%s->%s:%s\n' % (i, node[key], key)
        return result


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        patterns = [x.strip() for x in f.readlines()]

    trie = Trie()
    for pattern in patterns:
        trie.add_elem(pattern)

    with open('out.txt', 'w') as f:
        f.write(str(trie))
