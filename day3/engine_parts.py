import sys


def _is_symbol(c):
    return c != "." and not c.isdecimal()


class Sum:
    def __init__(self):
        self._sum = 0

    def add(self, value):
        self._sum += value


def main(lines):
    parts_sum = Sum()

    previous = set()
    to_check = []
    for line in lines:
        to_check_after = []
        current = set()
        decimal_start = -1
        for i, c in enumerate(line):
            if c.isdecimal():
                if decimal_start == -1:
                    decimal_start = i
                if i == len(line) - 1:
                    # Symbol before?
                    if _is_symbol(line[decimal_start - 1]):
                        parts_sum.add(int(line[decimal_start : i + 1]))
                    # Symbol above?
                    is_part = False
                    for j in range(decimal_start - 1, i + 1):
                        if j in previous:
                            parts_sum.add(int(line[decimal_start : i + 1]))
                            is_part = True
                            break
                    # Symbol below?
                    if not is_part:
                        to_check_after.append(
                            (decimal_start, line[decimal_start : i + 1])
                        )
            elif _is_symbol(c):
                current.add(i)
                # Symbol after?
                if decimal_start != -1:
                    parts_sum.add(int(line[decimal_start:i]))
                    decimal_start = -1
                # Part above?
                for p in to_check[:]:
                    if p[0] - 1 <= i <= p[0] + len(p[1]):
                        parts_sum.add(int(p[1]))
                        to_check.pop(0)
            else:
                if decimal_start == -1:
                    # Multiple consecutive .
                    continue
                else:
                    # Symbol before?
                    if _is_symbol(line[decimal_start - 1]):
                        parts_sum.add(int(line[decimal_start:i]))
                    # Symbol above?
                    is_part = False
                    for j in range(decimal_start - 1, i + 1):
                        if j in previous:
                            parts_sum.add(int(line[decimal_start:i]))
                            is_part = True
                            break
                    # Symbol below?
                    if not is_part:
                        to_check_after.append((decimal_start, line[decimal_start:i]))

                    decimal_start = -1
        to_check = to_check_after
        previous = current
    print(parts_sum._sum)


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(file, "r") as f:
        main(f.read().splitlines())
