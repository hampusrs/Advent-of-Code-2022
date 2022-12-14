def read_file(file):
    file = open(file, 'r')

    elfs = []
    elf = []
    for line in file:
        if line == '\n':
            elfs.append(elf.copy())
            elf.clear()
        else:
            elf.append(int(line))

    return elfs

def find_totals(elfs):
    totals = []
    for elf in elfs:
        total = sum(elf)
        totals.append(total)
    return totals

def main():
    file =  "./input.txt"
    elfs = read_file(file)

    totals = find_totals(elfs)
    totals.sort(reverse = True)

    ans = totals[0]+totals[1]+totals[2]
    print("Answer: %s" % ans)

if __name__ == '__main__':
    main()