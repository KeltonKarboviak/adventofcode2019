from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Point(object):
    x: int
    y: int


# @dataclass(frozen=True, eq=True)
# class


origin = Point(0, 0)


def generate_points(point: Point, instruction):
    direction, step = instruction[0], int(instruction[1:])
    points = []

    if direction == 'U':
        points = [Point(point.x, point.y+i) for i in range(1, step+1)]
    elif direction == 'D':
        points = [Point(point.x, point.y-i) for i in range(1, step+1)]
    elif direction == 'R':
        points = [Point(point.x+i, point.y) for i in range(1, step+1)]
    elif direction == 'L':
        points = [Point(point.x-i, point.y) for i in range(1, step+1)]

    return points

def main_part1():
    with open('day3.txt', 'r') as fh:
        wire1 = fh.readline().split(',')
        wire2 = fh.readline().split(',')

    print('Wire 1:', wire1)
    print('Wire 2:', wire2)

    points_visited = {
        'wire1': set(),
        'wire2': set(),
    }

    current_point = origin
    for instruction in wire1:
        print('Current Point:', current_point)
        new_points = generate_points(current_point, instruction)
        current_point = new_points[-1]
        points_visited['wire1'].update(new_points)
    print()

    current_point = origin
    for instruction in wire2:
        print('Current Point:', current_point)
        new_points = generate_points(current_point, instruction)
        current_point = new_points[-1]
        points_visited['wire2'].update(new_points)
    print()

    both_visited = points_visited['wire1'].intersection(points_visited['wire2'])

    # print('Both Visited:', both_visited)

    # |𝑎−𝑐|+|𝑏−𝑑|.
    distances = (abs(point.x - origin.x) + abs(point.y - origin.y) for point in both_visited)
    answer = min(distances)

    print('Answer:', answer)


def main_part2():
    with open('day3.txt', 'r') as fh:
        wire1 = fh.readline().split(',')
        wire2 = fh.readline().split(',')

    print('Wire 1:', wire1)
    print('Wire 2:', wire2)

    points_visited = {
        'wire1': [],
        'wire2': [],
    }

    current_point = origin
    for instruction in wire1:
        print('Current Point:', current_point)
        new_points = generate_points(current_point, instruction)
        current_point = new_points[-1]
        points_visited['wire1'].extend(new_points)
    print()

    current_point = origin
    for instruction in wire2:
        print('Current Point:', current_point)
        new_points = generate_points(current_point, instruction)
        current_point = new_points[-1]
        points_visited['wire2'].extend(new_points)
    print()


    # both_visited = points_visited['wire1'].intersection(points_visited['wire2'])

    # print('Both Visited:', both_visited)

    # |𝑎−𝑐|+|𝑏−𝑑|.
    distances = (abs(point.x - origin.x) + abs(point.y - origin.y) for point in both_visited)
    answer = min(distances)

    print('Answer:', answer)


if __name__ == "__main__":
    main_part1()
    main_part2()
