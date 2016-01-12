
if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        spectrum = map(int, f.readline().split())
    spectral_convolution = dict()

    convolution = [str(i-j) for i in spectrum for j in spectrum if i-j > 0]
    with open('out.txt', 'w') as f:
        f.write(' '.join(convolution))
