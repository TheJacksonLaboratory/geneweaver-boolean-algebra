"""Schema for the Boolean Algebra tool."""
import enum
from typing import Any, Dict, Hashable, List, Optional, Set, Union

from geneweaver.tools.framework.schema import ToolInput, ToolOutput
from pydantic import BaseModel


class GeneValue(BaseModel):
    """A gene value."""

    symbol: str
    value: float

    _hash_with_value = False

    class Config:
        """Pydantic config."""

        allow_mutation = False

    def __hash__(self: "GeneValue") -> int:
        """Hash the gene symbol (without value)."""
        # TODO note about hashing collisions
        return hash(self.symbol)

    def __eq__(self: "GeneValue", other: Any) -> bool:  # noqa: ANN401
        """Compare the gene symbol (without value)."""
        if isinstance(other, GeneValue):
            return self.symbol == other.symbol
        return False


class GeneValueFullHash(GeneValue):
    """A gene value with full hashing."""

    class Config:
        """Pydantic config."""

        allow_mutation = False

    def __hash__(self: "GeneValue") -> int:
        """Hash the gene symbol (with value)."""
        # TODO note about hashing collisions
        return hash(tuple(self.__dict__.values()))

    def __eq__(self: "GeneValue", other: Any) -> bool:  # noqa: ANN401
        """Compare the gene symbol (with value)."""
        if isinstance(other, GeneValue):
            return self.__dict__ == other.__dict__
        return False


class BooleanAlgebraType(enum.Enum):
    """Type of Boolean Algebra tool."""

    UNION = "union"
    INTERSECTION = "intersection"
    DIFFERENCE = "difference"


class BooleanAlgebraInput(ToolInput):
    """Input schema for the Boolean Algebra tool."""

    type: BooleanAlgebraType  # noqa: A003
    input_genesets: List[List[GeneValue]]
    intersection_min: int = 2
    intersection_max: Optional[int] = None


class BooleanAlgebraMultiSetOutput(BaseModel):
    """Output schema for the Boolean Algebra tool."""

    result_geneset_ids: Dict[Hashable, Set[Hashable]]


class BooleanAlgebraSingleSetOutput(BaseModel):
    """Output schema for the Boolean Algebra tool."""

    result_geneset_ids: Union[List[Hashable], Set[Hashable]]


class BooleanAlgebraOutput(ToolOutput):
    """Output schema for the Boolean Algebra tool."""

    result: Union[Union[List[Hashable], Set[Hashable]], Dict[Hashable, Set[Hashable]]]
