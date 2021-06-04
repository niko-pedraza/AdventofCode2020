import collections
from collections import defaultdict
class AdapterArray:
    def __init__(self, file=open('input', 'r')):
        self._adapters = sorted([int(jolts.strip()) for jolts in file])
        self._1jolt = {x for x in range(1,20,1)}
        self._3jolt = {x for x in range(1,20,3)}
        self._2jolt = {x for x in range(1,20,2)}


    def part1(self):
        print('Part 1')
        self._adapters.insert(0,0)
        self._adapters.append(self._adapters[-1]+3)
        diff = defaultdict(int)
        for i in range(len(self._adapters)-1):
            diff[self._adapters[i+1]-self._adapters[i]] += 1
        print('Adapter set(jolts)',self._adapters)
        print('Difference count between n and n+1:',diff.items())
        print('Multiplication Result:', diff[1] * diff[3])
        # self.CountFrequency(diff)
        print()

    def part2(self):
        print('Part 2')
        count = defaultdict(int,{0:1})
        for a in self._adapters[1:]:
            count[a] = count[a-3] + count[a-2] + count[a-1]

        print('Valid ways to arrange adapters: ', count[self._adapters[-1]])



        # options = collections.deque()
        # for i in range(len(self._adapters)):
        #     curr = self._adapters[i]
        #     for j in range(i+1,len(self._adapters)):
        #         next = self._adapters[j]
        #         if next - curr <= 3
        #             options.append(next)
        #         else:
        #             break
        #     if options






test = AdapterArray()


test.part1()
test.part2()