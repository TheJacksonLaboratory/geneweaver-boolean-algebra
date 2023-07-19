"""Find the symmetric difference of N sets."""
from typing import Hashable, Set

from geneweaver.tools.boolean_algebra.intersection import combination_intersection
from geneweaver.tools.boolean_algebra.union import union


def symmetric_difference(*args: Set[Hashable]) -> Set[Hashable]:
    """Find the symmetric difference of N genesets.

    This function works by finding the union of the input genesets, and then
    subtracting the union of the intersections of the input genesets.

    Result  = (A U B U C) - ((A N B) U (A N C) U (B N C))

    :param args: The genesets to find the symmetric difference of.
    :return: A set representing the symmetric difference of the input genesets.
    """
    union_set = union(*args)
    union_of_intersections = union(
        *combination_intersection(*args, max_size=2).values()
    )

    return union_set - union_of_intersections
