def read_file(file):
    file = open(file, 'r')
    datastream = file.readline()

    return datastream

def find_marker(datastream):
    marker = []
    processes = 0
    limit = 4

    for c in datastream:
        marker.append(c)
        if len(marker) > limit:
            marker.pop(0)
        processes += 1
        if len(set(marker)) == len(marker) and len(marker) >= limit:
            return marker, processes

    return None, processes


def main():
    file =  "./input.txt"
    data = read_file(file)

    marker, processes = find_marker(data)

    ans = processes
    print("Answer: %s" % ans)

if __name__ == '__main__':
    main()