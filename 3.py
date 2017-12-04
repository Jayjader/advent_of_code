from collections import defaultdict
from enum import Enum
from typing import List, Tuple


def ring_size_from_position(position: int) -> int:
    """
    Computes which ring the position falls on.
    Ring size is determined by the length of its sides (so ring sizes increase 2 by 2).
    """
    x = 1
    while x ** 2 < position:
        x += 2

    return x


def position_on_ring(global_position, ring_size: int) -> int:
    """
    Computes the local/relative position on a ring.
    Positions go from 0 (bottom right corner) to 4*(ring_size - 1)
    """
    ring_pos = ring_size ** 2 - global_position
    # print(f'Position on ring of size {ring_size}: {ring_pos}')
    return ring_pos


def distance_from_center_of_ring_side(position_on_ring, ring_size: int) -> int:
    """
    Computes a position's offset from the center of the side of it's associated ring.
    """
    if ring_size == 1:
        return 0
    side = position_on_ring // (ring_size - 1)
    position_on_side = position_on_ring - side * (ring_size - 1)

    center_of_ring_side = int(ring_size / 2 + 0.5) - 1  # Ring sides are always odd in length
    # print(f'Center of ring side of length {ring_size} is of relative position {center_of_ring_side}')
    return abs(center_of_ring_side - position_on_side)


def distance_from_center(distance_from_center_of_ring_side, ring_size: int) -> int:
    # print(f'At {distance_from_center_of_ring_side} from center on ring of size {ring_size}')
    if ring_size == 1:
        return 0
    elif distance_from_center_of_ring_side == 0:
        return 1 + distance_from_center(0, ring_size - 2)
    else:  # distance_from_center_of_ring_side > 0
        return 2 + distance_from_center(distance_from_center_of_ring_side - 1, ring_size - 2)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_position")
args = parser.parse_args()

data_position = int(args.data_position)

ring_size = ring_size_from_position(data_position)

print(distance_from_center(distance_from_center_of_ring_side(position_on_ring(data_position,
                                                                              ring_size), ring_size), ring_size))


# Part Two

class Direction(tuple, Enum):
    RIGHT = (1, 0)
    UP = (0, 1)
    LEFT = (-1, 0)
    DOWN = (0, -1)

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = (members.index(self) + 1) % len(members)
        return members[index]


def neighbours(coords: Tuple[int, int]) -> List[Tuple[int, int]]:
    output = []
    x, y = coords
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if not (dx == dy == 0):
                output.append((x + dx, y + dy))

    return output


def add(t1, t2: Tuple[int, int]) -> Tuple[int, int]:
    t2 = tuple(t2)
    return t1[0] + t2[0], t1[1] + t2[1]


grid = defaultdict(int)

current_val = 1
current_index = 0
current_wrapping_direction = Direction.RIGHT
next_wrapping_direction = current_wrapping_direction.next()
current_coords = (0, 0)

while True:
    grid[current_coords] = current_val

    if grid[add(current_coords, next_wrapping_direction)] == 0:
        current_wrapping_direction = next_wrapping_direction
        next_wrapping_direction = current_wrapping_direction.next()

    current_coords = add(current_coords, current_wrapping_direction)
    current_val = 0
    for cell in neighbours(current_coords):
        current_val += grid[cell]

    if current_val > data_position:
        break

print(current_val)
