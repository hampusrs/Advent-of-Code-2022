def read_file(file):
    file = open(file, 'r')
    data = []

    for rucksack in file:
        rucksack = rucksack.strip()
        break_point = int(len(rucksack) / 2)
        (c1, c2) = (rucksack[:break_point], rucksack[break_point:])
        data.append(rucksack)

    return data

def find_mutuals(data):
    mutuals = []

    for i in range(0, len(data)-2, 3):
        a, b, c = data[i], data[i+1], data[i+2]
        temp = set(a).intersection(b)
        temp = temp.intersection(c)
        mutuals.append(temp)


    return mutuals

def calculate_priority(data):
    priorities = []

    for rucksuck in data:
        for x in rucksuck:
            hej = ord(x)
            if 65 <= ord(x) <= 90:
                p = ord(x) - 64 + 26
                priorities.append(p)
            else:
                p = ord(x) - 96
                priorities.append(p)

    return priorities


def main():
    file =  "./input.txt"
    data = read_file(file)

    mutual_items = find_mutuals(data)

    priorities = calculate_priority(mutual_items)

    ans = sum(priorities)
    print("Answer: %d" % (ans))

if __name__ == '__main__':
    main()