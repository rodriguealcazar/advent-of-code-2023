def main():
    with open("input-1.txt", "r") as f:
        calibrations = []
        for l in f:
            l = l.strip()
            first = None
            second = None
            for i in range(len(l)):
                if first is None:
                    try:
                        first = int(l[i])
                    except ValueError:
                        pass
                if second is None:
                    try:
                        second = int(l[len(l) - 1 - i])
                    except ValueError:
                        pass
                if first is not None and second is not None:
                    calibrations.append(int(f"{first}{second}"))
                    break

        print(sum(calibrations))


if __name__ == "__main__":
    main()
