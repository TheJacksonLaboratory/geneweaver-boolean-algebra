"""Constants for boolean algebra unit tests."""
from geneweaver.tools.boolean_algebra.schema import GeneValue

BOOLEAN_GENESET_GENES_0 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
}

BOOLEAN_GENESET_GENES_1 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
}

BOOLEAN_GENESET_GENES_2 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
    GeneValue(symbol="I", value=1),
}

UNION_BOOLEAN_GENESET_GENES_0_1 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
}

UNION_BOOLEAN_GENESET_GENES_0_2 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
    GeneValue(symbol="I", value=1),
}

UNION_BOOLEAN_GENESET_GENES_1_2 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
    GeneValue(symbol="I", value=1),
}

UNION_BOOLEAN_GENESET_GENES_0_1_2 = UNION_BOOLEAN_GENESET_GENES_0_2

INT_BOOLEAN_GENESET_GENES_0_1 = {GeneValue(symbol="A", value=1)}

INT_BOOLEAN_GENESET_GENES_0_2 = {GeneValue(symbol="A", value=1)}

INT_BOOLEAN_GENESET_GENES_1_2 = {
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
}

INT_BOOLEAN_GENESET_GENES_0_1_2 = {GeneValue(symbol="A", value=1)}

DIFF_BOOLEAN_GENESET_GENES_0_1 = {
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
}

DIFF_BOOLEAN_GENESET_GENES_0_2 = {
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
    GeneValue(symbol="E", value=1),
    GeneValue(symbol="F", value=1),
    GeneValue(symbol="G", value=1),
    GeneValue(symbol="H", value=1),
    GeneValue(symbol="I", value=1),
}

DIFF_BOOLEAN_GENESET_GENES_1_2 = {
    GeneValue(symbol="I", value=1),
}

DIFF_BOOLEAN_GENESET_GENES_0_1_2 = {
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="D", value=1),
    GeneValue(symbol="I", value=1),
}
