def readinput(active, dimensions):
    assert 3 <= dimensions <= 4, 'Make sure dimensions is 3 or 4'
    FILE = [line for line in open('input')]
    for y, line in enumerate(FILE):
        for x, status in enumerate(line.strip()):
            if status == '#':
                coordinate = (x, y) + (0,) * (dimensions - 2)
                active.add(coordinate)


def Simulator(actives, Num_of_Cycles, Part):
    assert 1 <= Part <= 2, 'Make sure Part is 1 or 2'
    print('Num of actives before Cycle')

    print(f'Actives {len(actives)}')
    if Part == 1:
        for cycle in range(Num_of_Cycles):
            new_actives = set()
            # Points to check in this cycle
            xvals = [x[0] for x in actives]
            yvals = [y[1] for y in actives]
            zvals = [z[2] for z in actives]
            # print(f'xvals {xvals} yvals {yvals} zvals {zvals}')
            # neighbors active at this point
            neighbors_active = 0

            for _x in range(min(xvals) - 1, max(xvals) + 2):
                for _y in range(min(yvals) - 1, max(yvals) + 2):
                    for _z in range(min(zvals) - 1, max(zvals) + 2):
                        neighbors_active = 0
                        num_of_checks = 0
                        # print(f'Checking point ({_x},{_y},{_z})')
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    if (dx, dy, dz) != (0, 0, 0):
                                        num_of_checks += 1
                                        # print(f'{num_of_checks} ({_x+dx},{_y+dy},{_z+dz})')
                                        if (_x + dx, _y + dy, _z + dz) in actives:
                                            neighbors_active += 1
                        if (_x, _y, _z) in actives and (2 <= neighbors_active <= 3):
                            new_actives.add((_x, _y, _z))
                        elif (_x, _y, _z) not in actives and neighbors_active == 3:
                            new_actives.add((_x, _y, _z))
            actives = new_actives
            print(f'Actives after cycle {cycle + 1}')

            print(f'Actives {len(actives)}')
    else:
        for cycle in range(Num_of_Cycles):
            new_actives = set()
            # Points to check in this cycle
            xvals = [x[0] for x in actives]
            yvals = [y[1] for y in actives]
            zvals = [z[2] for z in actives]
            wvals = [w[3] for w in actives]
            # print(f'xvals {xvals} yvals {yvals} zvals {zvals} wvals {wvals}')
            # neighbors active at this point
            neighbors_active = 0

            for _x in range(min(xvals) - 1, max(xvals) + 2):
                for _y in range(min(yvals) - 1, max(yvals) + 2):
                    for _z in range(min(zvals) - 1, max(zvals) + 2):
                        for _w in range(min(wvals) - 1, max(wvals) + 2):
                            neighbors_active = 0
                            num_of_checks = 0
                            # print(f'Checking point ({_x},{_y},{_z},{_w})')
                            for dx in [-1, 0, 1]:
                                for dy in [-1, 0, 1]:
                                    for dz in [-1, 0, 1]:
                                        for dw in [-1, 0, 1]:
                                            if (dx, dy, dz, dw) != (0, 0, 0, 0):
                                                num_of_checks += 1
                                                # print(f'{num_of_checks} ({_x + dx},{_y + dy},{_z + dz},{_w+dw})')
                                                if (_x + dx, _y + dy, _z + dz, _w + dw) in actives:
                                                    neighbors_active += 1
                            if (_x, _y, _z, _w) in actives and (2 <= neighbors_active <= 3):
                                new_actives.add((_x, _y, _z, _w))
                            elif (_x, _y, _z) not in actives and neighbors_active == 3:
                                new_actives.add((_x, _y, _z, _w))
            actives = new_actives
            print(f'Actives after cycle {cycle + 1}')

            print(f'Actives {len(actives)}')

    res = len(actives)

    return res


def main():
    Active = set()
    readinput(Active, 3)

    print(f'part 1 3 dimensions:{Simulator(Active, 6, 1)}')

    print()

    Active = set()
    readinput(Active, 4)

    print(f'part 2 4 dimensions:{Simulator(Active, 6, 2)}')


if __name__ == '__main__':
    main()
