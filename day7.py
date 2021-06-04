import collections


class BagChecker:

    def __init__(self, file):
        self._rules = file
        self._cache = set()

        self.bag_list = collections.OrderedDict()

    def createbagDirectory(self, part):
        if part == 1:
            self.createbagDirectory1()
        elif part == 2:
            self.createbagDirectory2()
        else:
            raise ValueError('1 for part 1 and 2 for part 2 is only valid')

    def createbagDirectory1(self):

        for x, y in [line.split(' contain ') for line in self._rules]:
            a = []
            # print(f'x: {x[:-5]}')
            # print(f'y: {y.split(",")}')
            g = lambda a: a.strip().split(" ")[1:3]
            for c in y.split(','):
                a.append(" ".join(g(c)))
                # print("y:", " ".join(g(c)))

            # print('a:', a)
            self.bag_list[x[:-5]] = a

    def part1(self):
        print('Making a List of all Bags with Rules:')
        self.createbagDirectory(1)
        for contains in self.bag_list.values():
            print('contains: ', contains)
            for x in contains:
                print(x)
                if self.contains_gold_bag(x):
                    self.counter += 1
                    self._cache.add(x)
                    break
        return self.counter

    def part2(self):
        print('Make Bag Directory')
        self.createbagDirectory(2)
        print(self.bags_in_gold_bag('shiny gold'))

    def createbagDirectory2(self):
        g = lambda x: " ".join(x.split(' ')[:-1])
        for x, y in [line.split(' contain ') for line in self._rules]:
            a = []
            # print(f'x: {x[:-5]}')
            # print(f'y: {y.strip().split(",")}')
            for i in y.strip().split(', '):
                # print('i: ', g(i))
                a.append(g(i))
            self.bag_list[x[:-5]] = a

    def bags_in_gold_bag(self, bag):
        counter = 0
        for x in self.bag_list[bag]:
            if x[0].isnumeric():
                print('x[0]: ', x[0])
                counter += int(x[0]) + (int(x[0]) * int(self.bags_in_gold_bag(x[2:])))
            else:
                return 0
        return counter

    def contains_gold_bag(self, color):
        # print(self._cache)
        if color == 'shiny gold' or color in self._cache:
            return True
        elif color == 'other bags.':
            return False
        else:
            for contains in self.bag_list[color]:
                if self.contains_gold_bag(contains):
                    return True

            return False


file = open('input', 'r')
test = BagChecker(file)
test2 = BagChecker(file)

test2.part2()
