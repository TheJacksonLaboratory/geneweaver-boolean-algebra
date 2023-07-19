"""Find the intersection of N genesets.

The result will contain sets of genes that are shared across the input sets.
"""
import itertools
from typing import Dict, Hashable, Optional, Set


def intersection(*args: Set[Hashable]) -> Set[Hashable]:
    """Find the intersection of N genesets.

    The result will contain sets of genes that are shared across the input sets.

    :param input_sets: A list of geneset ids to find the intersection of.
    :return: A list of geneset ids that are the intersection of the input sets.
    """
    return set.intersection(*args)


def combination_intersection(
    *args: Set[Hashable], min_size: int = 2, max_size: Optional[int] = None
) -> Dict[Hashable, Set[Hashable]]:
    """Find the intersection of N genesets, across combinations of the input sets."""
    result = {}
    arg_indexes = tuple(range(len(args)))
    _max_size = len(args) if max_size is None else max_size

    if min_size < 2:
        raise ValueError("min_size must be greater than 2")

    if _max_size < min_size:
        raise ValueError("max_size must be greater than min_size")

    if _max_size > len(args):
        raise ValueError("max_size must be less than or equal to the number of sets")

    for i in range(min_size, _max_size + 1):
        for combination in itertools.combinations(arg_indexes, i):
            sets = [args[index] for index in combination]
            result[combination] = intersection(*sets)

    return result
