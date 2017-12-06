from typing import Dict, List, Set, Tuple


def reallocate(memory_allocation: List[int]) -> None:
    """
    Computes the next reallocation cycle by round-robin redistributing the first, most full memory bank to all memory
    banks.

    :param memory_allocation: Tuple[int, ...] Current memory allocation state
    """
    bank_to_reallocate = memory_allocation.index(max(memory_allocation))
    blocks_to_reallocate = memory_allocation[bank_to_reallocate]
    memory_allocation[bank_to_reallocate] = 0
    for _ in range(blocks_to_reallocate):
        bank_to_reallocate = (bank_to_reallocate + 1) % len(memory_allocation)
        memory_allocation[bank_to_reallocate] += 1


already_seen_configurations: Set[Tuple[int, ...]] = set()

with open('memory_banks.txt') as input_file_desc:
    bank_allocation = [int(blocks) for blocks in input_file_desc.readline().strip().split()]

while tuple(bank_allocation) not in already_seen_configurations:
    already_seen_configurations.add(tuple(bank_allocation))
    reallocate(bank_allocation)

print(len(already_seen_configurations))


# Part Two

past_configurations: Dict[Tuple[int, ...], int] = {}

with open('memory_banks.txt') as input_file_desc:
    bank_allocation = [int(blocks) for blocks in input_file_desc.readline().strip().split()]

step = 0

while past_configurations.get(tuple(bank_allocation)) is None:
    past_configurations[tuple(bank_allocation)] = step
    reallocate(bank_allocation)
    step += 1

print(step - past_configurations[tuple(bank_allocation)])
