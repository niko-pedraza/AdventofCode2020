class HandHeldHaulting:

    def __init__(self, file):
        self._instructions = [line.strip() for line in file]
        self._acc = 0
        self._instruction_check = set()
        self._pointer = 0
        self.command = {'nop': lambda y: self.nop(y), 'acc': lambda y: self.acc(y), 'jmp': lambda y: self.jmp(y)}
        self.switch = {'nop': lambda y: self.jmp(y), 'jmp': lambda y: self.nop(y)}

    def part1(self):
        print('Starting check')
        while self._pointer < len(self._instructions):
            if self._pointer in self._instruction_check:
                return self._acc
            command, value = self._instructions[self._pointer].split(' ')
            print(f'command: {command}')
            print(f'value: {value}')

            self._instruction_check.add(self._pointer)
            self.command[command](value)

        return -1

    def loop_check(self, instructions):
        print('Starting check')
        instruction_check = set()
        while self._pointer < len(instructions):
            if self._pointer in instruction_check:
                return False
            command, value = instructions[self._pointer].split(' ')
            print(f'command: {command}')
            print(f'value: {value}')

            instruction_check.add(self._pointer)
            self.command[command](value)

        return True

    def reset(self):
        self._acc = 0
        self._pointer = 0


    def part2(self):
        print('Starting test')
        pointer = 0
        for line in self._instructions:
            c, v = line.split(' ')
            if c == 'nop':
                print(f'Replacing {c} at {pointer}')
                copy = self._instructions.copy()
                copy[pointer] = f'jmp {v}'
                if self.loop_check(copy):
                    return self._acc
                self.reset()
            elif c == 'jmp':
                print(f'Replacing {c} at {pointer}')
                copy = self._instructions.copy()
                copy[pointer] = f'nop {v}'
                if self.loop_check(copy):
                    return self._acc
                self.reset()
            pointer += 1
        return -1

    def nop(self, value):
        self._pointer += 1

    def acc(self, value):
        if value[0] == '+':
            self._acc += int(value[1:])
        elif value[0] == '-':
            self._acc -= int(value[1:])
        else:
            raise ValueError('Invalid value has been read!!!')
        self._pointer += 1

    def jmp(self, value):
        if value[0] == '+':
            self._pointer += int(value[1:])
        elif value[0] == '-':
            self._pointer -= int(value[1:])
        else:
            raise ValueError('Jumping to invalid location!!!')


file = open('input', 'r')

test = HandHeldHaulting(file)

print(test.part2())
