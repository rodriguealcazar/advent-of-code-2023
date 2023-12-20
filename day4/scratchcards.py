import sys


def main(lines):
    total = 0
    for line in lines:
        line = line.strip()
        _, game = line.split(":")
        winning, played = game.split("|")
        winning = {n for n in winning.strip().split(" ") if n}
        matches = 0
        for number in played.strip().split(" "):
            if number and number in winning:
                matches += 1
        total += 2 ** (matches - 1) if matches > 0 else 0
    print(total)


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(file, "r") as f:
        main(f.read().splitlines())
