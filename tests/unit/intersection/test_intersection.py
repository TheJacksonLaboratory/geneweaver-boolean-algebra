import pytest

from geneweaver.tools.boolean_algebra.intersection import intersection

from tests.unit.const import (
    BOOLEAN_GENESET_GENES_0,
    BOOLEAN_GENESET_GENES_1,
    BOOLEAN_GENESET_GENES_2,
    INT_BOOLEAN_GENESET_GENES_0_1,
    INT_BOOLEAN_GENESET_GENES_0_2,
    INT_BOOLEAN_GENESET_GENES_1_2,
    INT_BOOLEAN_GENESET_GENES_0_1_2,
)


@pytest.mark.parametrize(
    "input_sets, expected",
    [
        # Two sets with no overlap
        [({1, 2, 3}, {4, 5, 6}), set()],
        # Two sets with overlap
        [({1, 2, 3}, {3, 4, 5}), {3}],
        # Three sets with no overlap
        [({1, 2}, {3, 4}, {5, 6}), set()],
        # Three sets with overlap
        [({1, 2}, {2, 3}, {2, 4}), {2}],
        # Empty sets
        [(set(), set()), set()],
        # One empty set and one non-empty set
        [(set(), {1, 2, 3}), set()],
        # Sets with strings
        [({"a", "b"}, {"b", "c"}), {"b"}],
        # Sets with different types
        [({1, "a"}, {1, "b"}), {1}],
        # Test with real geneset values
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1),
            INT_BOOLEAN_GENESET_GENES_0_1,
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_2),
            INT_BOOLEAN_GENESET_GENES_0_2,
        ),
        (
            (BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            INT_BOOLEAN_GENESET_GENES_1_2,
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            INT_BOOLEAN_GENESET_GENES_0_1_2,
        ),
    ],
)
def test_intersection(input_sets, expected):
    assert intersection(*input_sets) == expected
