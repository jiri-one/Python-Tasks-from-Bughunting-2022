import fileinput
from enum import Enum
from collections import namedtuple

"""
This is a simulation of a ship.

It takes instructions in form of a <action><value> where
<action> is one of the letters NSEWLRF, and <value> is an integer.

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.
"""

class Direction(Enum):
    N = 0
    E = 90
    S = 180
    W = 270

    def __add__(self, other):
        return Direction((self.value + other.value) % 360)

    def __sub__(self, other):
        return Direction((self.value - other.value) % 360)

    def rotate(self, rotation):
        if rotation.type == "R":
            return self + rotation
        return self - rotation


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.E

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, direction: {self.direction}"

    def rotate(self, rotation):
        self.direction = self.direction.rotate(rotation)

    def go_forward(self, instruction):
        delta = self._get_delta(self.direction)
        self._move(delta, instruction)

    def move(self, instruction):
        delta = self._get_delta(instruction.type)
        self._move(delta, instruction)

    def _get_delta(self, direction):
        deltas = {
            Direction.N: (0, -1),
            Direction.E: (1, 0),
            Direction.S: (0, 1),
            Direction.W: (-1, 0),
        }
        return deltas[direction]

    def _move(self, delta, instruction):
        self.x = self.x + delta[0] * instruction.value
        self.y = self.y + delta[1] * instruction.value

    def parse_instructions(self, instruction):
        if instruction.type in ("R", "L"):
            self.rotate(instruction)
        elif instruction.type == "F":
            self.go_forward(instruction)
        else:
            self.move(instruction)


def read_instructions():
    instruction = namedtuple("Instruction", "type value")
    instructions = []
    directions = {
        "N": Direction.N,
        "E": Direction.E,
        "S": Direction.S,
        "W": Direction.W,
        }
    for line in fileinput.input():
        val = directions.get(line[0], line[0])
        instructions.append(instruction(val, int(line[1:])))
    return instructions


def main():
    instructions = read_instructions()
    ship = Ship()
    print(ship)
    for instruction in instructions:
        ship.parse_instructions(instruction)
        print(ship)


if __name__ == "__main__":
    main()
