import re


def pattern_count(text, pattern):
    result = re.findall('(?=%s)' % pattern, text)
    return len(result)

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text = f.readline()
        pattern = f.readline()[:-1]
    count = pattern_count(text, pattern)
    with open('out.txt', 'w') as f:
        f.write(str(count))