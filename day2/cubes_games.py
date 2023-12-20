def main():
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open("input.txt", "r") as f:
        games = []
        for l in f:
            l = l.strip()
            # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            game, sets = l.split(":")
            game = int(game[5:])
            impossible = False
            for set_ in sets.split("; "):
                for cubes in set_.strip().split(", "):
                    x, colour = cubes.split(" ")
                    if int(x) > max_cubes[colour]:
                        impossible = True
                        break
            if not impossible:
                games.append(game)
        print(sum(games))


if __name__ == "__main__":
    main()
