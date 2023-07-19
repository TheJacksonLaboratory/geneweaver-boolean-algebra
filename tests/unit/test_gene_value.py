import pytest
from geneweaver.tools.boolean_algebra.schema import GeneValue, GeneValueFullHash


@pytest.mark.parametrize(
    ("gene_value_0", "gene_value_1", "should_equal"),
    [
        (GeneValue(symbol="A", value=1), GeneValue(symbol="A", value=1), True),
        (GeneValue(symbol="A", value=1), GeneValue(symbol="A", value=0), True),
        (GeneValue(symbol="A", value=1), GeneValue(symbol="B", value=1), False),
        (GeneValue(symbol="A", value=1), GeneValue(symbol="B", value=0), False),
        (GeneValue(symbol="A", value=0), GeneValue(symbol="B", value=0), False),
        (
            GeneValueFullHash(symbol="A", value=1),
            GeneValueFullHash(symbol="A", value=1),
            True,
        ),
        (
            GeneValueFullHash(symbol="A", value=1),
            GeneValueFullHash(symbol="A", value=0),
            False,
        ),
        (
            GeneValueFullHash(symbol="A", value=1),
            GeneValueFullHash(symbol="B", value=1),
            False,
        ),
        (
            GeneValueFullHash(symbol="A", value=1),
            GeneValueFullHash(symbol="B", value=0),
            False,
        ),
        (
            GeneValueFullHash(symbol="A", value=0),
            GeneValueFullHash(symbol="B", value=1),
            False,
        ),
        (
            GeneValueFullHash(symbol="B", value=0),
            GeneValueFullHash(symbol="B", value=0),
            True,
        ),
        (
            GeneValueFullHash(symbol="B", value=0),
            GeneValueFullHash(symbol="B", value=1),
            False,
        ),
        (
            GeneValue(symbol="A", value=0),
            GeneValueFullHash(symbol="B", value=1),
            False
        ),
        (
                GeneValueFullHash(symbol="B", value=1),
                GeneValue(symbol="A", value=0),
                False
        ),
        (
            1,
            GeneValueFullHash(symbol="A", value=1),
            False
        ),
        (
            "A",
            GeneValueFullHash(symbol="A", value=1),
            False
        ),
        (
                1,
                GeneValue(symbol="A", value=1),
                False
        ),
        (
                "A",
                GeneValue(symbol="A", value=1),
                False
        )

    ],
)
def test_gene_values_equality(gene_value_0, gene_value_1, should_equal):
    if should_equal:
        assert gene_value_0 == gene_value_1
    else:
        assert gene_value_0 != gene_value_1


@pytest.mark.parametrize("gene_value", [
    GeneValue(symbol="A", value=1),
    GeneValue(symbol="A", value=0),
    GeneValue(symbol="B", value=1),
    GeneValue(symbol="B", value=0),
    GeneValue(symbol="C", value=1),
    GeneValue(symbol="C", value=0),
    GeneValueFullHash(symbol="A", value=1),
    GeneValueFullHash(symbol="A", value=0),
    GeneValueFullHash(symbol="B", value=1),
    GeneValueFullHash(symbol="B", value=0),
    GeneValueFullHash(symbol="C", value=1),
    GeneValueFullHash(symbol="C", value=0),
])
def test_can_hash_gene_values(gene_value):
    assert hash(gene_value) == hash(gene_value)