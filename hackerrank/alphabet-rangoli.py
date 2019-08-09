import string

filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/alphabet-rangoli-testcases/input/input06.txt'


def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    with open(filename) as f:
        n = f.readline()

    # n = int(input())
    print_rangoli(int(n))
