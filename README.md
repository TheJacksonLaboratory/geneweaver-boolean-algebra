# Geneweaver - Boolean Algebra Tool

[![Tests](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/tests.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/tests.yml)
[![Style](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/style.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/style.yml)
[![Coverage](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/coverage.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-boolean-algebra/actions/workflows/coverage.yml)

The Boolean Algebra Tool performs basic set operations on at least two Gene Sets.
Results are displayed as lists of genes belonging to one of the three different types of
set operations: Union, Intersect, and Symmetric Difference. Furthermore, results allow
users to quickly determine new relationships between Gene Sets and create a new Gene Set
based on set-derived findings.

## Installation

### From PyPI

#### pip
```bash
pip install geneweaver-boolean-algebra
```

#### poetry
```bash
poetry add geneweaver-boolean-algebra
```

### From Source

Installing from source requires python 3.9 and [poetry](https://python-poetry.org/).

```bash
git clone git@github.com:TheJacksonLaboratory/geneweaver-boolean-algebra.git
cd geneweaver-boolean-algebra
poetry install
```

## Usage

See usage example in [Geneweaver Docs](https://thejacksonlaboratory.github.io/geneweaver-docs/tutorial/nci_60_example_01/#run-a-genweaver-tool-locally).