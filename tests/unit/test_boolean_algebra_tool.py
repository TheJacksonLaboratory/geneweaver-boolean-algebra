import pytest
from pathlib import Path

from geneweaver.tools.boolean_algebra.tool import (
    BooleanAlgebra,
    BooleanAlgebraType,
    BooleanAlgebraInput,
    BooleanAlgebraOutput,
    WorkflowType,
)

from tests.unit.const import (
    BOOLEAN_GENESET_GENES_0,
    BOOLEAN_GENESET_GENES_1,
    BOOLEAN_GENESET_GENES_2,
    UNION_BOOLEAN_GENESET_GENES_0_1,
    INT_BOOLEAN_GENESET_GENES_0_1,
    INT_BOOLEAN_GENESET_GENES_0_2,
    INT_BOOLEAN_GENESET_GENES_1_2,
    INT_BOOLEAN_GENESET_GENES_0_1_2,
    DIFF_BOOLEAN_GENESET_GENES_0_1_2,
)


@pytest.mark.parametrize(
    "input_value, expected",
    [
        # Union
        [
            BooleanAlgebraInput(
                type=BooleanAlgebraType.UNION,
                input_genesets=[BOOLEAN_GENESET_GENES_0, BOOLEAN_GENESET_GENES_1],
            ),
            BooleanAlgebraOutput(result=UNION_BOOLEAN_GENESET_GENES_0_1),
        ],
        # Intersection
        [
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
        ],
        # Difference
        [
            BooleanAlgebraInput(
                type=BooleanAlgebraType.DIFFERENCE,
                input_genesets=[
                    BOOLEAN_GENESET_GENES_0,
                    BOOLEAN_GENESET_GENES_1,
                    BOOLEAN_GENESET_GENES_2,
                ],
            ),
            BooleanAlgebraOutput(result=DIFF_BOOLEAN_GENESET_GENES_0_1_2),
        ],
    ],
)
def test_boolean_algebra_run(input_value, expected):
    ba = BooleanAlgebra()
    run_result = ba.run(input_value)
    for item in run_result.result:
        assert item in expected.result
    for item in expected.result:
        assert item in run_result.result


def test_boolean_algebra_properties():
    ba = BooleanAlgebra()
    assert ba.tool_name == "Boolean Algebra"
    assert ba.tool_input is BooleanAlgebraInput
    assert ba.tool_output is BooleanAlgebraOutput
    assert ba.workflow_type == WorkflowType.NEXTFLOW
    assert str(ba.workflow_definition).endswith(
        str(Path("workflow") / "boolean_algebra.nf")
    )
