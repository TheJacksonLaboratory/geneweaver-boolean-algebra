"""Test that the combination intersection function works as expected."""
import pytest
from geneweaver.tools.boolean_algebra.intersection import combination_intersection

from tests.unit.const import (
    BOOLEAN_GENESET_GENES_0,
    BOOLEAN_GENESET_GENES_1,
    BOOLEAN_GENESET_GENES_2,
    INT_BOOLEAN_GENESET_GENES_0_1,
    INT_BOOLEAN_GENESET_GENES_0_1_2,
    INT_BOOLEAN_GENESET_GENES_0_2,
    INT_BOOLEAN_GENESET_GENES_1_2,
)


# Successful test cases
@pytest.mark.parametrize(
    ("input_sets", "min_size", "max_size", "expected"),
    [
        (
            ({1, 2, 3}, {2, 3, 4}, {3, 4, 5}),
            2,
            3,
            {(0, 1): {2, 3}, (0, 2): {3}, (1, 2): {3, 4}, (0, 1, 2): {3}},
        ),
        (
            ({1, 2}, {2, 3}, {3, 4}, {4, 5}),
            2,
            None,
            {
                (0, 1): {2},
                (0, 2): set(),
                (0, 3): set(),
                (1, 2): {3},
                (1, 3): set(),
                (2, 3): {4},
                (0, 1, 2): set(),
                (0, 1, 3): set(),
                (0, 2, 3): set(),
                (1, 2, 3): set(),
                (0, 1, 2, 3): set(),
            },
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            2,
            None,
            {
                (0, 1): INT_BOOLEAN_GENESET_GENES_0_1,
                (0, 2): INT_BOOLEAN_GENESET_GENES_0_2,
                (1, 2): INT_BOOLEAN_GENESET_GENES_1_2,
                (0, 1, 2): INT_BOOLEAN_GENESET_GENES_0_1_2,
            },
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            2,
            None,
            {
                (0, 1): INT_BOOLEAN_GENESET_GENES_0_1,
                (0, 2): INT_BOOLEAN_GENESET_GENES_0_2,
                (1, 2): INT_BOOLEAN_GENESET_GENES_1_2,
                (0, 1, 2): INT_BOOLEAN_GENESET_GENES_0_1_2,
            },
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            3,
            None,
            {
                (0, 1, 2): INT_BOOLEAN_GENESET_GENES_0_1_2,
            },
        ),
        (
            (BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1, BOOLEAN_GENESET_GENES_2),
            3,
            3,
            {
                (0, 1, 2): INT_BOOLEAN_GENESET_GENES_0_1_2,
            },
        ),
    ],
)
def test_combination_intersection_success(input_sets, min_size, max_size, expected):
    """Test that the function returns the expected output when given valid input."""
    assert (
        combination_intersection(*input_sets, min_size=min_size, max_size=max_size)
        == expected
    )


# Error test cases
@pytest.mark.parametrize(
    ("input_sets", "min_size", "max_size", "expected_error_msg"),
    [
        (({1, 2, 3}, {2, 3, 4}, {3, 4, 5}), 1, 3, "min_size must be greater than 2"),
        (
            ({1, 2, 3}, {2, 3, 4}, {3, 4, 5}),
            2,
            1,
            "max_size must be greater than min_size",
        ),
        (
            ({1, 2, 3}, {2, 3, 4}, {3, 4, 5}),
            2,
            4,
            "max_size must be less than or equal to the number of sets",
        ),
    ],
)
def test_combination_intersection_error(
    input_sets, min_size, max_size, expected_error_msg
):
    """Test that the function raises a ValueError when given invalid input."""
    with pytest.raises(ValueError, match=expected_error_msg):
        combination_intersection(*input_sets, min_size=min_size, max_size=max_size)
