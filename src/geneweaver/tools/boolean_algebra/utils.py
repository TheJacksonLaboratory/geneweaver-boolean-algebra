"""Utility functions for boolean algebra operations."""
from typing import List, Tuple, Dict, Iterable, Hashable


def iterable_to_sets(input_sets: Iterable[Iterable[Hashable]]) -> List[set]:
    """Convert an iterable of iterables to a list of sets.

    :param input_sets: A list of lists of geneset ids.
    :return: A list of sets of geneset ids.
    """
    return [set(s) for s in input_sets]
