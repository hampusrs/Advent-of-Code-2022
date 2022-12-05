def read_file(file):
    file = open(file, 'r')
    data = None

    return data


def main():
    file =  "./input.txt"
    data = read_file(file)

    ans1 = 0
    print("Answer: %s" % ans1)

if __name__ == '__main__':
    main()