"""Tests for the iterable_to_sets() function."""
import pytest
from geneweaver.tools.boolean_algebra.utils import iterable_to_sets


@pytest.mark.parametrize(
    ("input_sets", "expected"),
    [
        ([[1, 2, 3], [4, 5, 6]], [{1, 2, 3}, {4, 5, 6}]),
        ([[1, 1, 2, 2, 3, 3], [4, 4, 5, 5, 6, 6]], [{1, 2, 3}, {4, 5, 6}]),
        ([[], []], [set(), set()]),
        ([[], [1, 2, 3]], [set(), {1, 2, 3}]),
        ([], []),
        # Integer input
        ([[1, 2], [3, 4, 5]], [{1, 2}, {3, 4, 5}]),
        # String input
        ([["a", "b"], ["c", "d", "e"]], [{"a", "b"}, {"c", "d", "e"}]),
        # Mixed type input
        ([[1, "a"], [2, "b"]], [{1, "a"}, {2, "b"}]),
        # Single-item lists
        ([[1], ["a"]], [{1}, {"a"}]),
        # Duplicates within and between lists
        ([[1, 2], [2, 3]], [{1, 2}, {2, 3}]),
        # Duplicates only between lists
        ([[1, 2], [1, 2]], [{1, 2}, {1, 2}]),
        # List with one duplicate and one unique item
        ([[1, 2, 2], [3, 3, 4]], [{1, 2}, {3, 4}]),
        # Single-item list repeated
        ([[1], [1], [1]], [{1}, {1}, {1}]),
        # Empty list and list with one item
        ([[], [1]], [set(), {1}]),
        # Lists with multiple identical items
        ([[1, 1, 1], [2, 2, 2]], [{1}, {2}]),
        # Tuples
        ([("a", "b"), ("c", "d")], [{"a", "b"}, {"c", "d"}]),
        # Tuples with duplicate values
        ([("a", "a"), ("b", "b")], [{"a"}, {"b"}]),
        # Sets (are already sets)
        ([{1, 2, 3}, {4, 5, 6}], [{1, 2, 3}, {4, 5, 6}]),
        # Frozensets (are already sets, but immutable)
        ([frozenset([1, 2, 3]), frozenset([4, 5, 6])], [{1, 2, 3}, {4, 5, 6}]),
        # Frozensets are hashable, and so should work as items in the inner iterable
        (
            [[frozenset([1, 2, 3]), frozenset([4, 5, 6])]],
            [{frozenset([1, 2, 3]), frozenset([4, 5, 6])}],
        ),
    ],
)
def test_iterable_to_sets(input_sets, expected):
    """Test that iterable_to_sets() returns the expected output."""
    assert iterable_to_sets(input_sets) == expected


@pytest.mark.parametrize(
    "input_sets",
    [
        # List of lists of lists
        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
        # List of lists of sets
        [[{1, 2, 3}, {4, 5, 6}], [{7, 8, 9}, {10, 11, 12}]],
        # List of lists of dicts
        [[{1: "a", 2: "b"}, {3: "c", 4: "d"}], [{5: "e", 6: "f"}, {7: "g", 8: "h"}]],
        # List of lists of bytearrays
        [[bytearray([1, 2, 3]), bytearray([4, 5, 6])]],
    ],
)
def test_raises_unhashable(input_sets):
    """Test that passing unhashable types to iterable of sets should raise and error."""
    with pytest.raises(TypeError, match="unhashable type"):
        iterable_to_sets(input_sets)
