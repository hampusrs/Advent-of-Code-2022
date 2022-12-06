def read_file(file):
    file = open(file, 'r')
    data = []

    for section in file:
        section = section.strip()
        first, second = section.split(',')
        f1, f2 = first.split('-')
        s1, s2 = second.split('-')
        fs = list(range(int(f1),int(f2)+1))
        ss = list(range(int(s1),int(s2)+1))
        data.append([fs,ss])

    return data

def find_mutuals(data):
    mutuals = []

    for section in data:
        c1, c2 = section[0], section[1]
        c1, c2 = set(c1), set(c2)
        
        hello = c1.intersection(c2)
        if (len(hello) > 0):
            mutuals.append(True)
        else:
            mutuals.append(False)

    return mutuals

def count(data):
    counts = []

    return counts


def main():
    file =  "./input.txt"
    data = read_file(file)

    #test = [('abcdd', 'cddgh')]
    mutual_items = find_mutuals(data)



    ans = mutual_items.count(True)
    print("Answer: %d" % (ans))

if __name__ == '__main__':
    main()