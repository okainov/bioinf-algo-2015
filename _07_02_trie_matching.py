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

    def match(self, text):
        text_index = 0
        symbol = text[text_index]
        current_node = self.nodes[0]
        pattern = ''
        while True:
            if symbol in current_node:
                current_node = self.nodes[current_node[symbol]]
                text_index += 1
                pattern += symbol
                try:
                    symbol = text[text_index]
                except:
                    pass

            elif not current_node:
                return pattern
            else:
                return None




if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline().strip()
        patterns = [x.strip() for x in f.readlines()]

    trie = Trie()
    for pattern in patterns:
        trie.add_elem(pattern)
    index = 0
    result = list()
    while len(text) > 0:
        if trie.match(text):
            result.append(index)
        index += 1
        text = text[1:]

    with open('out.txt', 'w') as f:
        f.write(' '.join(map(str, result)))
