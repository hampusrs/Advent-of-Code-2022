class Dir:
    def __init__(self, name, parent=None):
        self.name = str(name)
        self.content = []
        self.parent = parent

    def add(self, object):
        self.content.append(object)

    def get_dir(self, dir_name):
        for object in self.content:
            if object.name == dir_name and isinstance(object, Dir):
                return object

    def get_parent(self):
        return self.parent

    def get_size(self):
        total_size = 0

        for object in self.content:
            s = object.get_size()
            total_size += s

        return total_size

class File:
    def __init__(self, name, size):
        self.name = str(name)
        self.size = int(size)

    def get_size(self):
        return self.size

def read_file(file):
    file = open(file, 'r').readlines()
    tree = Dir("/")
    current_dir = tree


    for i in range(2, len(file)):
        line = file[i]
        line_splits = line.split(' ')
        cmd = line_splits[0]

        if line.startswith("dir"):
            dir = line_splits[1]
            dir = Dir(dir, parent=current_dir)
            current_dir.add(dir)
        elif cmd.isnumeric():
            f = File(line_splits[1], line_splits[0])
            current_dir.add(f)
        elif line.startswith("$ cd "):  #cmd == '$':
            current_dir = handle_command(line, current_dir, tree)

    return tree

def handle_command(line, current_dir, tree):
    line_splits = line.split(' ')
    cmd = line_splits[1]

    if line.startswith("$ cd .."):
        return current_dir.get_parent()
    elif line.startswith("$ cd /"):
        return tree
    elif line.startswith("$ cd"):
        dir_name = line_splits[2]
        return current_dir.get_dir(dir_name)

def to_delete(tree, required_space, dir=None):
    if dir is None:
        dir = tree

    for object in tree.content:
        if isinstance(object, Dir):
            dir = to_delete(object, required_space, dir)

    if required_space <= tree.get_size() <= dir.get_size():
        return tree


    return dir


def main():
    file =  "./input.txt"
    tree = read_file(file)

    disk_space = 70000000
    update_space = 30000000

    used_space = tree.get_size()
    unused_space = disk_space - used_space
    required_space = update_space - unused_space

    ans = to_delete(tree, required_space).get_size()
    print("Answer: %s" % ans)

if __name__ == '__main__':
    main()