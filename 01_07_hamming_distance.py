def hamming_distance(string_1, string_2):
    distance = 0
    for a, b in zip(string_1, string_2):
        if a != b:
            distance += 1
    return distance

if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text_1 = f.readline()
        text_2 = f.readline()
    distance = hamming_distance(text_1, text_2)
    with open('out.txt', 'w') as f:
        f.write(str(distance))
