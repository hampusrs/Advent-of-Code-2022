def read_file(file):
    file = open(file, 'r')
    data = []

    return data


def main():
    file =  "./input.txt"
    data = read_file(file)

    ans = 0
    print("Answer: %s" % ans)

if __name__ == '__main__':
    main()