# PSA formalizácia problému

Formalizácia problému PSA, slúži pre interné potreby diplomovej práce. Je opísaná v súbore [formalization.pdf](./out/formalization.pdf).

## Parser

Pre načítanie súboru `.psa` použite triedu `parser.Parser`. Príklad použitia:

```python

from parser import Parser

parser = Parser()
parser.load('./cvrptw001.psa')

```

## Autor

Samuel Mitas
