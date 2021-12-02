def part1():
    with open("input.txt") as f:
        num = None
        count = 0
        for line in f:
            line = line.strip()
            if line:
                n = int(line)
                if num == None:
                    num = n
                else:
                    if n > num:
                        count += 1
                    num = n
    print(count)

def part2():
    with open("input.txt") as f:
        window = []
        count = 0
        for line in f:
            line = line.strip()
            if line:
                n = int(line)
                if len(window) < 3:
                    window.append(n)
                else:
                    if sum(window[1:]) + n > sum(window):
                        count += 1
                    window.pop(0)
                    window.append(n)
    print(count)

if __name__ == "__main__":
    part2()