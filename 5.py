from typing import List


def step(offsets: List[int], position: int) -> int:
    """
    Computes the next jump in the interrupt handling, and returns the new position
    """
    offset = offsets[position]
    offsets[position] += 1
    return position + offset


with open('offsets.txt') as input_file_desc:
    offsets = input_file_desc.readlines()

offsets = list(map(int, map(str.strip, offsets)))

steps = 0
number_of_offsets = len(offsets)
current_position = 0

while 0 <= current_position < number_of_offsets:
    current_position = step(offsets, current_position)
    steps += 1

print(steps)
