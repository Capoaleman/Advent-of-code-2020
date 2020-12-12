# December 12th Advent Calendar of Code 2020
# https://adventofcode.com/2020
# By Capoaleman

import pygame as pg

vec = pg.math.Vector2

DIRECTION = {"N": vec(0, 1),
             "E": vec(1, 0),
             "S": vec(0, -1),
             "W": vec(-1, 0)}


class Waypoint:
    def __init__(self):
        self.position = vec(10, 1)

    def move(self, mov, value):
        if mov == "E" or mov == "N" or mov == "S" or mov == "W":
            self.position += DIRECTION[mov]*value
        elif mov == "L":
            self.position = self.position.rotate(value)
        else:
            self.position = self.position.rotate(360-value)


class Ship:
    def __init__(self, waypoint=None):
        self.position = vec(0, 0)
        self.direc = vec(1, 0)
        self.waypoint = waypoint

    def turn(self, value):
        self.direc = self.direc.rotate(value)

    def move(self, mov, value):
        if self.waypoint == None:
            if mov == "F":
                self.position += self.direc*value
            elif mov == "R":
                self.turn(360-value)
            elif mov == "L":
                self.turn(value)
            else:
                self.position += DIRECTION[mov]*value
        else:
            if mov == "F":
                self.position += self.waypoint.position*value
            else:
                self.waypoint.move(mov, value)

    def man_dist(self):
        return int(abs(self.position.x)+abs(self.position.y))


if __name__ == "__main__":
    with open("InputDay12_2020.txt", "r") as file:
        data = file.read().splitlines()
    boat = Ship()
    boat2 = Ship(Waypoint())
    for inst in data:
        boat.move(inst[:1], int(inst[1:]))
        boat2.move(inst[:1], int(inst[1:]))
    print("The Manhattan distance from the starting point is:", boat.man_dist())
    print("The Manhattan distance from the starting point for part 2 is:",
          boat2.man_dist())
