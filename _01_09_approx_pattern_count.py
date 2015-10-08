from _01_07_hamming_distance import hamming_distance
from _01_02_frequent_words import window


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline())

    fragment_length = len(pattern)
    count = 0
    for i, fragment in enumerate(["".join(x) for x in window(text, fragment_length)]):
        if hamming_distance(fragment, pattern) <= d:
            count += 1

    with open('out.txt', 'w') as f:
        f.write(str(count))
