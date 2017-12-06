from typing import List, Set, Tuple


def reallocate(memory_allocation: List[int]) -> None:
    """
    Computes the next reallocation cycle by round-robin redistributing the first, most full memory bank to all memory
    banks.
    :param memory_allocation: Tuple[int, ...] Current memory allocation state
    """
    bank_to_reallocate = memory_allocation.index(max(memory_allocation))
    blocks_to_reallocate = memory_allocation[bank_to_reallocate]
    # print(f'Memory state:\t\t{memory_allocation}')
    # print(f'Bank to reallocate: {bank_to_reallocate} (contains {blocks_to_reallocate} blocks)')
    memory_allocation[bank_to_reallocate] = 0
    for _ in range(blocks_to_reallocate):
        bank_to_reallocate = (bank_to_reallocate + 1) % len(memory_allocation)
        memory_allocation[bank_to_reallocate] += 1

    # print(f'New memory state:\t{memory_allocation}')


already_seen_configurations: Set[Tuple[int, ...]] = set()

with open('memory_banks.txt') as input_file_desc:
    bank_allocation = [int(blocks) for blocks in input_file_desc.readline().strip().split()]

while tuple(bank_allocation) not in already_seen_configurations:
    already_seen_configurations.add(tuple(bank_allocation))
    reallocate(bank_allocation)

print(len(already_seen_configurations))
