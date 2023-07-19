"""Find the union of N genesets.

The union will contain one set with all the unique genes in the input sets.
"""
from typing import Hashable, Set


def union(*args: Set[Hashable]) -> Set[Hashable]:
    """Find the union of N genesets.

    The union will contain one set with all the unique genes in the input sets.

    Pass the genesets as positional arguments.

    :param args: The sets to find the union of.
    :return: A list of geneset ids that are the union of the input sets.
    """
    return set.union(*args)
