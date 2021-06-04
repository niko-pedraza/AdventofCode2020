from collections import deque
from collections import namedtuple
from collections import defaultdict
import time
import collections
from chap8 import Circular_Queue

def main():
    FILE = [line for line in open('input')]
    starting_turns = deque()
    memory = defaultdict(lambda:[0,0])
    counter = 1
    for x in FILE[0].split(','):
        value = int(x)
        memory[value][0] = counter

        counter += 1
    length = len(memory)
    start = time.process_time()
    prev_value = value
    for turn in range(length+1, 30000001):
        if prev_value in memory:
            memory[prev_value][1] = turn - 1
            value = memory[prev_value][1]-memory[prev_value][0]
            memory[prev_value][0] = memory[prev_value][1]
        else:
            memory[prev_value][0] = turn-1
            value = 0
        prev_value = value

    end = time.process_time()
    print(f'turn {turn} value {value} in {round(end- start,4)} seconds')

if __name__ == '__main__':
    main()
