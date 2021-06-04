class Customs:
    def __init__(self, database):
        self._database = database
        self.group = []
        self.total_sum = 0
        self.questions = set()

    def part1(self):

        return self.__countsum()

    def part2(self):
        self.total_sum = 0
        return self.__countsum2()

    def __countsum2(self):
        for line in self._database:
            if line == '\n':
                answered_yes = len(set.intersection(*self.group))
                self.total_sum += answered_yes
                self.group.clear()
            else:
                for c in line.strip():
                    self.questions.add(c)
                self.group.append(self.questions.copy())
                self.questions.clear()

        return self.total_sum

    def __countsum(self):
        for line in self._database:
            if line == '\n':
                questions_answered = len(self.questions)
                self.total_sum += questions_answered
                self.questions.clear()

            for char in line.strip():
                self.questions.add(char)

        return self.total_sum


file = open('input', 'r')

test = Customs(file)

result = test.part2()

print(result)
