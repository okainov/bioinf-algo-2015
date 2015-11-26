import re


def translate_prot(text, table):
    elems = re.findall('[A-Z]{3}', text)
    result = ''
    for elem in elems:
        result += table[elem]
    return result

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        pattern = f.readline()
    with open('codon_table.txt', 'r') as f:
        table = {x.split()[0]:x.split()[1] for x in f.readlines()}
    for key in table:
        if table[key] == '""':
            table[key] = ''

    result = translate_prot(pattern, table)
    with open('out.txt', 'w') as f:
        f.write(str(result))
