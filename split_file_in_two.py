def split_file(filename):
    with open(filename, "r", encoding="utf-8", errors="replace") as file:
        lines = file.readlines()

    middle = len(lines) // 2

    part1 = filename.replace(".txt", "") + "_part1.pgn"
    part2 = filename.replace(".txt", "") + "_part2.pgn"

    with open(part1, "w", encoding="utf-8", errors="replace") as file:
        file.writelines(lines[:middle])
    with open(part2, "w", encoding="utf-8", errors="replace") as file:
        file.writelines(lines[middle:])

    print("File split")

split_file("chessabc_base.pgn")
