import re
from collections import defaultdict


def validvalueRange(string_list):
    validvalues = set()
    for line in string_list:

        field, string = line.split(': ')
        rules = string.split(' or ')
        for group in rules:
            min, max = group.split('-')
            validvalues.update([*range(int(min), int(max) + 1)])
    return validvalues


def field_rules(Input):
    res = defaultdict(list)
    for line in Input:
        field, string = line.split(': ')
        rules = string.split(' or ')
        for group in rules:
            min, max = group.split('-')
            res[field].append((int(min), int(max)))
    return res


def CalculateErrorpart1(tickets, ValidValues):
    result = 0
    for ticket in tickets:
        for val in ticket:
            if int(val) not in ValidValues:
                result += int(val)

    return result


def removeinvalidticket(tickets, ValidValues):
    res = []
    for ticket in tickets:
        valid = True
        for val in ticket:
            if int(val) not in ValidValues:
                valid = False
                break
        if valid:
            res.append(ticket)

    return res


def sort(myticket, validtickets, field_rules):
    sort= defaultdict(set)
    ticket_length = len(myticket)
    for position in range(0, ticket_length):
        for field, valuerange in field_rules.items():
            min1, max1 = valuerange[0]
            min2, max2 = valuerange[1]
            matches_cond = True
            for ticket in validtickets:
                if not ((min1 <= int(ticket[position]) <= max1) or (min2 <= int(ticket[position]) <= max2)):
                    matches_cond = False
                    break
            if matches_cond:
                sort[field].add(position)
    for iteration in range(ticket_length):
        for k,v in sort.items():
            if len(v) == 1:
                for key,value in sort.items():
                    if key == k:
                        continue
                    value.difference_update(v)

    res = {}
    for iteration in range(ticket_length):
        for k,v in sort.items():
            for x in v:
                res[k] = myticket[x]

    print(res)

    return res


def main():
    temp = []
    FILE = []

    for line in open('input'):
        if line == '\n':
            FILE.append(temp.copy())
            temp.clear()
        else:
            temp.append(line.strip())
    del temp

    rules_for_ticket_field = validvalueRange(FILE[0])
    myticket = [int(x) for x in FILE[1][1].split(',')]
    nearbyticket = [x for x in [ticket.split(',') for ticket in FILE[2][1:]]]
    print(f'Error scanning rate part 1 {CalculateErrorpart1(nearbyticket, rules_for_ticket_field)}')
    lookup_rules = field_rules(FILE[0])
    valid_tickets = removeinvalidticket(nearbyticket, rules_for_ticket_field)

    myticket_sorted = sort(myticket, valid_tickets, lookup_rules)
    result = 1
    for key,val in myticket_sorted.items():
        if 'departure' in key:
            result *= val

    print(f'Result for part 2 {result}')



if __name__ == '__main__':
    main()
