import math


"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2.
"""


def calculate_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    return max([fuel, 0])

def main_part1():
    with open('day1.txt', 'r') as fh:
        masses = [int(line.strip()) for line in fh]

    divided_by_3 = [mass // 3 for mass in masses]
    subtracted_2 = [mass - 2 for mass in divided_by_3]

    fuel_sum = sum(subtracted_2)

    print('Part 1 Answer:', fuel_sum)


def main_part2():
    with open('day1.txt', 'r') as fh:
        masses = [int(line.strip()) for line in fh]

    fuels = [calculate_fuel(mass) for mass in masses]
    fuel_sum = sum(fuels)

    print('Part 2 Answer:', fuel_sum)


if __name__ == "__main__":
    main_part1()
    main_part2()
