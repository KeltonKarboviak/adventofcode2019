ADD = 1
MUL = 2
HALT = 99


def main_part1():
    with open('day2.txt', 'r') as fh:
        intcodes = [int(i) for i in fh.read().split(',')]

    intcodes[1] = 12
    intcodes[2] = 2

    # intcodes = [int(i) for i in '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')]

    opcodes = [(idx*4, code) for idx, code in enumerate(intcodes[::4])]
    for idx, code in opcodes:
        instructions = intcodes[idx:idx+4]
        code, operand1_location, operand2_location, result_location = instructions
        print(idx, instructions, end=' ')
        if code == HALT:
            print('halt')
            break

        operand1, operand2 = intcodes[operand1_location], intcodes[operand2_location]

        if code == ADD:
            print(f'add {operand1} + {operand2} = {operand1 + operand2} -> stored in location {result_location}')
            intcodes[result_location] = operand1 + operand2
        elif code == MUL:
            print(f'mul {operand1} * {operand2} = {operand1 * operand2} -> stored in location {result_location}')
            intcodes[result_location] = operand1 * operand2

    print('Resulting intcodes:', intcodes)
    print('Answer:', intcodes[0])


def main_part2():
    pass


if __name__ == "__main__":
    main_part1()
    main_part2()
