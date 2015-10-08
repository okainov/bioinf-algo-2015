import string


# noinspection PyShadowingNames
def reverse_dna(text):
    # http://www.tutorialspoint.com/python/string_translate.htm
    intab = "ATCG"
    outtab = "TAGC"
    trantab = string.maketrans(intab, outtab)

    return text.translate(trantab)[::-1]

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
    result = reverse_dna(text)
    with open('out.txt', 'w') as f:
        f.write(str(result))
