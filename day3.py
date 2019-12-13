from dataclasses import dataclass


def main_part1():
    with open('day3.txt', 'r') as fh:
        wire1 = fh.readline().split(',')
        wire2 = fh.readline().split(',')

    print('Wire 1:', wire1)
    print('Wire 2:', wire2)


def main_part2():
    pass


if __name__ == "__main__":
    main_part1()
    main_part2()
