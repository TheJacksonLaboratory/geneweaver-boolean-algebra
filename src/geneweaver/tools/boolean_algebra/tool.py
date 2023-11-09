"""Boolean algebra tool."""
# ruff: noqa: D102
from __future__ import annotations

from pathlib import Path
from typing import Optional, Type

from geneweaver.tools.boolean_algebra.intersection import combination_intersection
from geneweaver.tools.boolean_algebra.symmetric_difference import symmetric_difference
from geneweaver.tools.boolean_algebra.union import union
from geneweaver.tools.boolean_algebra.utils import iterable_to_sets
from geneweaver.tools.framework import ToolInput, ToolOutput
from geneweaver.tools.framework.abstract import AbstractTool
from geneweaver.tools.framework.enum import WorkflowType

from .schema import BooleanAlgebraInput, BooleanAlgebraOutput, BooleanAlgebraType


class BooleanAlgebra(AbstractTool):
    """Boolean algebra tool."""

    @property
    def tool_input(self: AbstractTool) -> Type[ToolInput]:
        return BooleanAlgebraInput

    @property
    def tool_output(self: AbstractTool) -> Type[ToolOutput]:
        return BooleanAlgebraOutput

    def run(
        self: BooleanAlgebra, tool_input: BooleanAlgebraInput
    ) -> BooleanAlgebraOutput:
        genesets = tool_input.input_genesets
        inputs = tool_input if isinstance(genesets, set) else iterable_to_sets(genesets)

        if tool_input.type is BooleanAlgebraType.UNION:
            return BooleanAlgebraOutput(result=union(*inputs))
        elif tool_input.type is BooleanAlgebraType.INTERSECTION:
            return BooleanAlgebraOutput(
                result=combination_intersection(
                    *inputs,
                    min_size=tool_input.intersection_min,
                    max_size=tool_input.intersection_max,
                )
            )
        elif tool_input.type is BooleanAlgebraType.DIFFERENCE:
            return BooleanAlgebraOutput(result=symmetric_difference(*inputs))

    @property
    def workflow_definition(self: BooleanAlgebra) -> Optional[Path]:
        return Path(__file__).parent / "workflow" / "boolean_algebra.nf"

    @property
    def workflow_type(self: BooleanAlgebra) -> Optional[WorkflowType]:
        return WorkflowType.NEXTFLOW

    @property
    def tool_name(self: AbstractTool) -> str:
        return "Boolean Algebra"
