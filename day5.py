import collections
from typing import List
from array import *


class BinaryBoarding:
    SeatID = collections.namedtuple('SeatID', ('id', 'max'))

    def __init__(self, bp):
        self.boarding_passes = bp
        self.seat_ids: List[BinaryBoarding.SeatID] = []

    def find_max_id(self):
        for seat in self.boarding_passes:
            row_loc = seat[:7]
            print('row loc:',row_loc)
            col_loc = seat[7:]
            #print('col loc:',col_loc)
            row = self.convertdecimal(row_loc)
            print('row num',row)
            col = self.convertdecimal(col_loc)
            print('col num',col)
            id = self.seat_id(row, col)
            print(id)

            self.seat_ids.append(BinaryBoarding.SeatID(id, id if not self.seat_ids else max(id, self.seat_ids[-1].max)))
        return self.seat_ids[-1].max


    def convertdecimal(self, string):
        result = 0
        for x in range(len(string)):

            if string[x] == 'B':
                result += pow(2, 6 - x)
            elif string[x] == 'R':
                result += pow(2,2-x)

        return result

    def seat_id(self, row, col):
        return (row * 8) + col

    def findseat(self):
        list =[]
        for x in sorted(self.seat_ids):
            list.append(x.id)
        start = list[0]
        end = list[-1]
        return sorted(set(range(start,end+1)).difference(list))




file = open('input','r')

test = BinaryBoarding(file)

result = test.find_max_id()

print(result)

print(test.findseat())