"""Test the boolean algebra tool class."""

import pytest
from geneweaver.tools.boolean_algebra.plugin import (
    BooleanAlgebra,
    BooleanAlgebraInput,
    BooleanAlgebraOutput,
    BooleanAlgebraType,
)

from tests.unit.const import (
    BOOLEAN_GENESET_GENES_0,
    BOOLEAN_GENESET_GENES_1,
    BOOLEAN_GENESET_GENES_2,
    DIFF_BOOLEAN_GENESET_GENES_0_1_2,
    INT_BOOLEAN_GENESET_GENES_0_1,
    INT_BOOLEAN_GENESET_GENES_0_1_2,
    INT_BOOLEAN_GENESET_GENES_0_2,
    INT_BOOLEAN_GENESET_GENES_1_2,
    UNION_BOOLEAN_GENESET_GENES_0_1,
)


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        # Union
        (
            BooleanAlgebraInput(
                type=BooleanAlgebraType.UNION,
                input_genesets=[BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1],
            ),
            BooleanAlgebraOutput(result=UNION_BOOLEAN_GENESET_GENES_0_1),
        ),
        # Intersection
        (
            BooleanAlgebraInput(
                type=BooleanAlgebraType.INTERSECTION,
                input_genesets=[
                    BOOLEAN_GENESET_GENES_0,
                    BOOLEAN_GENESET_GENES_1,
                    BOOLEAN_GENESET_GENES_2,
                ],
                intersection_min=2,
            ),
            BooleanAlgebraOutput(
                result={
                    (0, 1): INT_BOOLEAN_GENESET_GENES_0_1,
                    (0, 2): INT_BOOLEAN_GENESET_GENES_0_2,
                    (1, 2): INT_BOOLEAN_GENESET_GENES_1_2,
                    (0, 1, 2): INT_BOOLEAN_GENESET_GENES_0_1_2,
                }
            ),
        ),
        # Difference
        (
            BooleanAlgebraInput(
                type=BooleanAlgebraType.DIFFERENCE,
                input_genesets=[
                    BOOLEAN_GENESET_GENES_0,
                    BOOLEAN_GENESET_GENES_1,
                    BOOLEAN_GENESET_GENES_2,
                ],
            ),
            BooleanAlgebraOutput(result=DIFF_BOOLEAN_GENESET_GENES_0_1_2),
        ),
    ],
)
def test_boolean_algebra_run(input_value, expected):
    """The Boolean Algebra tool class can run with different inputs."""
    ba = BooleanAlgebra()
    run_result = ba.run(input_value)
    for item in run_result.result:
        assert item in expected.result
    for item in expected.result:
        assert item in run_result.result
