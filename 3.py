def ring_size_from_position(position: int) -> int:
    '''
    Computes which ring the position falls on.
    Ring size is determined by the length of its sides (so ring sizes increase 2 by 2).
    '''
    x = 1
    while x ** 2 < position:
        x += 2

    return x


def position_on_ring(global_position, ring_size: int) -> int:
    '''
    Computes the local/relative position on a ring.
    Positions go from 0 (bottom right corner) to 4*(ring_size - 1)
    '''
    ring_pos = ring_size ** 2 - global_position
    # print(f'Position on ring of size {ring_size}: {ring_pos}')
    return ring_pos


def distance_from_center_of_ring_side(position_on_ring, ring_size: int) -> int:
    '''
    Computes a position's offset from the center of the side of it's associated ring.
    '''
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

spiral_index = 0
current_ring_size = 1


def ring_length(ring_size: int) -> int:
    return 4 * ring_size - 4
