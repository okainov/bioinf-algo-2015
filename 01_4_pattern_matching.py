import re


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        pattern = f.readline()[:-1]
        text = f.readline()
    result = [str(m.start(0)) for m in re.finditer('(?=%s)' % pattern, text)]
    with open('out.txt', 'w') as f:
        f.write(str(' '.join(result)))
