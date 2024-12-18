"""Plugin Definition for Jax.ATS."""
from __future__ import annotations

from geneweaver.tools.boolean_algebra.intersection import combination_intersection
from geneweaver.tools.boolean_algebra.symmetric_difference import symmetric_difference
from geneweaver.tools.boolean_algebra.union import union
from geneweaver.tools.boolean_algebra.utils import iterable_to_sets

from .schema import BooleanAlgebraInput, BooleanAlgebraOutput, BooleanAlgebraType


class BooleanAlgebra:
    """Boolean algebra tool ATS Plugin."""

    def run(
        self: BooleanAlgebra, input_data: BooleanAlgebraInput
    ) -> BooleanAlgebraOutput:
        """Run the Boolean Algebra tool."""
        genesets = input_data.input_genesets
        inputs = input_data if isinstance(genesets, set) else iterable_to_sets(genesets)

        if input_data.type is BooleanAlgebraType.UNION:
            return BooleanAlgebraOutput(result=union(*inputs))
        elif input_data.type is BooleanAlgebraType.INTERSECTION:
            return BooleanAlgebraOutput(
                result=combination_intersection(
                    *inputs,
                    min_size=input_data.intersection_min,
                    max_size=input_data.intersection_max,
                )
            )
        elif input_data.type is BooleanAlgebraType.DIFFERENCE:
            return BooleanAlgebraOutput(result=symmetric_difference(*inputs))
