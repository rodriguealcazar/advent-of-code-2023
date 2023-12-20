import re
import sys


def main(lines):
    """
    10

    1   9   n - 1
    2   16  n - 3
    3   21  n - 5
    4   24  n - 7
    5   25  n - 9   n - (n -1)
    6   24  n - 7

    9

    1   8   n - 1
    2   14  n - 3
    3   18  n - 5
    4   20  n - 7
    5   20  n - 9   n - n
    """
    times = re.split(" +", lines[0].split("Time:")[1].strip())
    distances = re.split(" +", lines[1].split("Distance:")[1].strip())
    total_winning_ways = 1
    for i, time in enumerate(times):
        record = int(distances[i])
        time = int(time)
        d = n = 0
        for i in range(1, time + 1, 2):
            d += time - i
            if d > record:
                n += 1
        winning_ways = ((n - 1) * 2) if time % 2 else ((n * 2) - 1)
        print(winning_ways)
        total_winning_ways *= winning_ways
    print(total_winning_ways)


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(file, "r") as f:
        main(f.read().splitlines())
