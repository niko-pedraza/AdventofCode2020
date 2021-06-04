import time


class PassportChecker:
    conditions = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    hcl_cond = {'a', 'b', 'c', 'd', 'e', 'f','0','1','2','3','4','5','6','7','8','9'}
    ecl_cond = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def __init__(self, passports):
        self._database = passports
        self.passport = {}

        self.validpassports = 0

    def run(self):
        print('Running Passport Checker')
        return self.__unpackage_info()


    def __unpackage_info(self):
        # for key,data in [attribute.strip().split(':') for attribute in [line.split(' ') for line in self._database]]:
        for line in self._database:
            if line == '\n':
                check = self.__is_valid(self.passport)
                if check:
                    self.validpassports += 1
                    print(self.passport)

                self.passport.clear()
                continue
            for key, data in [attribute.split(":") for attribute in line.strip().split(" ")]:
                self.passport[key] = data

        return self.validpassports

    def __is_valid(self, passport):
        for check in self.conditions:
            if check not in passport:
                return False
            if check == 'byr':
                if not 1920 <= int(passport[check]) <= 2002:
                    return False
            elif check == 'iyr':
                if not 2010 <= int(passport[check]) <= 2020:
                    return False
            elif check == 'eyr':
                if not 2020 <= int(passport[check]) <= 2030:
                    return False
            elif check == 'hgt':
                if passport[check][-2:] == 'in':
                    if not 59 <= int(passport[check][:-2]) <= 76:
                        return False
                elif passport[check][-2:] == 'cm':
                    if not 150 <= int(passport[check][:-2]) <= 193:
                        return False
                else:
                    return False
            elif check == 'hcl':
                if passport[check][0] == "#" and len(passport[check]) == 7:
                    for char in passport[check][1:]:
                        if char not in self.hcl_cond:
                            return False
                else:
                    return False
            elif check == 'ecl':
                if passport[check] not in self.ecl_cond:
                    return False

            elif check == 'pid':
                if len(passport[check]) != 9:
                    return False

        return True


file = open('input', 'r')
database = []
for x in file:
    database.append(x)
start = time.process_time()
checker = PassportChecker(database)
end = time.process_time()
print(f'{checker.run()} valid passports in {(end-start)} ms ')
