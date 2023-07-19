"""Test the union function."""
import pytest
from geneweaver.tools.boolean_algebra.union import union
from geneweaver.tools.boolean_algebra.schema import GeneValue

from tests.unit.const import (
    BOOLEAN_GENESET_GENES_0,
    BOOLEAN_GENESET_GENES_1,
    BOOLEAN_GENESET_GENES_2,
    UNION_BOOLEAN_GENESET_GENES_0_1,
    UNION_BOOLEAN_GENESET_GENES_0_2,
    UNION_BOOLEAN_GENESET_GENES_0_1_2,
)


@pytest.mark.parametrize(
    "input_sets, expected",
    [
        # Two sets with no overlap
        [({1, 2, 3}, {4, 5, 6}), {1, 2, 3, 4, 5, 6}],
        # Two sets with overlap
        [({1, 2, 3}, {3, 4, 5}), {1, 2, 3, 4, 5}],
        # Three sets with no overlap
        [({1, 2}, {3, 4}, {5, 6}), {1, 2, 3, 4, 5, 6}],
        # Three sets with overlap
        [({1, 2}, {2, 3}, {3, 4}), {1, 2, 3, 4}],
        # Empty sets
        [(set(), set()), set()],
        # One empty set and one non-empty set
        [(set(), {1, 2, 3}), {1, 2, 3}],
        # Sets with strings
        [({"a", "b"}, {"b", "c"}), {"a", "b", "c"}],
        # Sets with different types
        [({1, "a"}, {2, "b"}), {1, 2, "a", "b"}],
        # Sets with actual GeneValue objects
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1),
            UNION_BOOLEAN_GENESET_GENES_0_1,
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_2),
            UNION_BOOLEAN_GENESET_GENES_0_2,
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            UNION_BOOLEAN_GENESET_GENES_0_1_2,
        ),
    ],
)
def test_union(input_sets, expected):
    assert union(*input_sets) == expected
