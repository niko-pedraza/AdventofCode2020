from collections import namedtuple
from math import gcd


def first_availble(x, buses):
    temp = None
    first_bus = None
    for bus in buses:
        factor = x + bus - (x % bus)
        if temp is None or factor < temp:
            temp = factor
            first_bus = bus
    return [temp, first_bus]


# def first_available_with_offset(list):
#     timestamp = list[0].id
#     increment = list[0].id
#     check_for = []
#     while False:
#         for x in list[1:]:
#             check_for.append(timestamp % x.id == 0 and timestamp % x.offset == 0)
#         print(timestamp)
#         if all(check_for):
#             return timestamp
#         timestamp *= increment


def ext_gcd(input1, input2):
    r, r1, t, t1, a, b = 1, 0, 0, 1, input1, input2
    print(f'Default r:{r} r1:{r1} t:{t} t1:{t1} a:{a} b:{b}')
    while b > 0:
        q = a // b
        r, r1 = r1, r - (q * r1)
        t, t1 = t1, t - (q * t1)
        a, b = b, a - (b * q)
        print(f'q:{q} r:{r} r1:{r1} t:{t} t1:{t1} a:{a} b:{b}')
    return r, t


def main():
    FILE = [line for line in open('input')]
    # part 1
    earliest_depart, available_buses = int(FILE[0]), [int(bus) for bus in FILE[1].split(',') if bus != 'x']
    first_availble_timestamp, first_availble_bus = first_availble(earliest_depart, available_buses)
    minutes_to_wait = first_availble_timestamp - earliest_depart
    # part 2
    Bus = namedtuple('Bus', ('id', 'offset'))
    buses_with_offset = [Bus(int(bus), (int(bus) - (offset % int(bus)))%int(bus)) for offset, bus in enumerate(FILE[1].split(','))
                         if bus != 'x' ]
    # buses_with_offset.remove(buses_with_offset[0])
    # buses_with_offset.insert(0, Bus(int(FILE[1].split(',')[0]), 0))
    print(buses_with_offset)
    while len(buses_with_offset) > 1:
        n1, a1 = buses_with_offset[-1]
        print(f'n1:{n1}, a1:{a1}')
        n2, a2 = buses_with_offset[-2]
        print(f'n2:{n2}, a2:{a2}')

        buses_with_offset.pop()
        buses_with_offset.pop()

        m1, m2 = ext_gcd(n1, n2)
        print(f'm1:{m1} m2:{m2}')
        x = (a1 * m2 * n2) + (a2 * m1 * n1)
        x %= n1 * n2
        if x == 0:
            x += n1 * n2
        buses_with_offset.append((n1 * n2, x))
        print(buses_with_offset)

    print('bus ', first_availble_bus)
    print('minutes waited ', minutes_to_wait)
    print(f'Part 1: {first_availble_bus * minutes_to_wait} ')
    print(f'Part 2: {buses_with_offset[0][1]}')


if __name__ == '__main__':
    main()
