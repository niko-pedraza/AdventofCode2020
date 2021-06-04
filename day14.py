from collections import defaultdict
from re import findall
from itertools import product


def part1(FILE):
    mask = None
    mem = defaultdict(lambda: ['0'] * 36)

    for line in FILE:
        c, v = line.strip().split(' = ')
        if c == 'mask':
            mask = ''.join(reversed(v))
        else:
            address = findall(r'\d+', c)[0]
            # print(f"Decimal Value {v}")
            binary_val = bin(int(v))
            sign, value = binary_val.strip().split('b')
            # print(f'sign {sign} value {value}')
            value = "".join(reversed(value))
            # print(f'reversed value {value}')
            # print(f'print Mask {mask}')
            for i in range(len(mask)):
                if mask[i] == '1':
                    mem[address][i] = '1'
                elif mask[i] == '0':
                    mem[address][i] = '0'
                else:
                    try:
                        mem[address][i] = value[i]
                    except IndexError:
                        if sign == '0':
                            mem[address][i] = '0'
                        elif sign == '1':
                            mem[address][i] = '1'
    total = 0
    for location, stored in mem.items():
        decimal = int("".join(reversed(stored)), 2)
        print(f'Memory Location {location} stores {decimal}')
        total += decimal
    print(f'Summation of values in memory: {total}')


def part2(FILE):
    mask = None
    mem = defaultdict(int)

    for line in FILE:
        c, v = line.strip().split(' = ')
        if c == 'mask':
            mask = ''.join(reversed(v))
        else:
            encoded_address = findall(r'\d+', c)[0]
            binary_EA = bin(int(encoded_address)).split('b')[1]
            binary_EA = "".join(reversed(binary_EA))

            temp = ['0'] * 36
            x_positions = []
            for i in range(len(mask)):
                if mask[i] == 'X':
                    temp[i] = 'X'
                    x_positions.append(i)
                elif mask[i] == '1':
                    temp[i] = '1'
                else:
                    try:
                        temp[i] = binary_EA[i]
                    except IndexError:
                        temp[i] = '0'
            table = list(product([0, 1], repeat=len(x_positions)))
            addresses = []
            for combination in table:
                copy = temp.copy()
                for i in range(len(combination)):
                    copy[x_positions[i]] = str(combination[i])

                addresses.append(int("".join(reversed(copy)), 2))
            for x in addresses:
                mem[x] = int(v)
    total = 0
    for stored in mem.values():
        total += stored
    print(f'Summation of values in memory: {total}')


def main():
    FILE = [line for line in open('input')]
    print('Part 1')
    part1(FILE)
    print('Part 2')
    part2(FILE)


if __name__ == "__main__":
    main()
