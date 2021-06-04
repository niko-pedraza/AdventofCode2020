""" Day 12 """
import time
import numpy as np
import math


class Boat:
    def __init__(self):
        self.x, self.y = 0, 0
        self.degree = 0

    def addx(self, val):
        self.x += val

    def subx(self, val):
        self.x -= val

    def addy(self, val):
        self.y += val

    def suby(self, val):
        self.y -= val


class Waypoint():
    def __init__(self):
        self.x, self.y = 10, 1
        self.theta = 0

    def addx(self, val):
        self.x += val

    def subx(self, val):
        self.x -= val

    def addy(self, val):
        self.y += val

    def suby(self, val):
        self.y -= val


# Part 1
start = time.perf_counter()
INPUT = open('input')
myboat = Boat()

Directions = {'N': lambda char, val: myboat.addy(val), 'S': lambda char, val: myboat.suby(val),
              'E': lambda char, val: myboat.addx(val), 'W': lambda char, val: myboat.subx(val),
              'L': lambda char, val: degreeshift(char, val), 'R': lambda char, val: degreeshift(char, val),
              'F': lambda char, val: forward(val)}


def degreeshift(direction, shift):
    if direction == 'R':
        myboat.degree -= shift
    elif direction == 'L':
        myboat.degree += shift
    myboat.degree %= 360


def forward(shift):
    if myboat.degree == 0:
        myboat.addx(shift)
    elif myboat.degree == 90:
        myboat.addy(shift)
    elif myboat.degree == 180:
        myboat.subx(shift)
    elif myboat.degree == 270:
        myboat.suby(shift)
    else:
        assert ValueError("Something went wrong")


# for character, value in [(line[0], line[1:]) for line in INPUT]:
#     Directions[character](character, int(value))

# part 2

myboat2 = Boat()
waypoint = Waypoint()
WayDirections = {'N': lambda char, val: waypoint.addy(val), 'S': lambda char, val: waypoint.suby(val),
                 'E': lambda char, val: waypoint.addx(val), 'W': lambda char, val: waypoint.subx(val),
                 'L': lambda char, val: relativeshift(char, val), 'R': lambda char, val: relativeshift(char, val),
                 'F': lambda char, val: wayforward(val)}


def wayforward(multiplier):
    myboat2.x += multiplier * waypoint.x
    myboat2.y += multiplier * waypoint.y


def relativeshift(char, val):
    theta = 0
    if char == 'R':
        theta -= val
    elif char == 'L':
        theta += val
    theta %= 360
    print(f'{waypoint.x},{waypoint.y}')
    print(theta)
    radians =math.radians(theta)
    temp = waypoint.x
    waypoint.x = (waypoint.x*round(math.cos(radians))) - (waypoint.y*round(math.sin(radians)))
    waypoint.y = (temp*round(math.sin(radians))) + (waypoint.y*round(math.cos(radians)))
    print(f'{waypoint.x},{waypoint.y}')

for character, value in [(line[0], line[1:]) for line in INPUT]:
    WayDirections[character](character, int(value))

print(f'x: {myboat.x}, y: {myboat.y}')
part1 = abs(myboat.x) + abs(myboat.y)
print(f'x: {myboat2.x}, y: {myboat2.y}')
part2 = abs(myboat2.x) + abs(myboat2.y)
end = time.perf_counter()
print(f'part1: {part1}')
print(f'part2: {part2}')
