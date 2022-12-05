def read_file(file):
    f = open(file, 'r')
    stacks = []
    for l in f:
        s = l.split()
        if s[0] == '1':
            for i in s:
                stacks.append([])
            break
    instructions = []

    file = open(file, 'r')
    for line in file:
        splits = line.split()
        if len(splits) != 0 and splits[0] != '1' and splits[0] != "move":
            for i in range(len(stacks)):
                index = 1 + 4 * i
                if len(line) >= index and line[index] != ' ':
                    stacks[i].append(line[index])
        elif len(splits) != 0 and splits[0] != '1' and splits[0] == "move":
            temp = []
            for x in splits:
                if x.isdigit():
                    temp.append(int(x))
            instructions.append(tuple(temp))


    return stacks, instructions

def do_instructions(stacks, instructions):
    for instruction in instructions:
        for i in range(instruction[0], 0, -1):
        #for i in range(0, instruction[0]): #pop(0)
            temp = stacks[instruction[1]-1].pop(i-1)
            stacks[instruction[2]-1].insert(0, temp)
            print()

    return

def main():
    file =  "./example.txt"
    stacks, instructions = read_file(file)

    do_instructions(stacks, instructions)

    tops=""
    for stack in stacks:
        tops = tops + stack[0]
    ans1 = tops
    print("Answer: %s" % ans1)

if __name__ == '__main__':
    main()