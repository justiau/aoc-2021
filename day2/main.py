def part1():
    x = 0
    y = 0
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                action, value = line.split()
                value = int(value)
                if action == "forward":
                    x += value
                elif action == "down":
                    y += value
                elif action == "up":
                    y-= value
    return x, y

def part2():
    x = 0
    y = 0
    aim = 0
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                action, value = line.split()
                value = int(value)
                if action == "forward":
                    x += value
                    y += value * aim
                elif action == "down":
                    aim += value
                elif action == "up":
                    aim -= value
    return x, y


if __name__ == "__main__":
    x, y = part2()
    print(x*y)