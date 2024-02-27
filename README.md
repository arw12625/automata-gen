# Automata Gen
This project provides utilities for generating random automata.

This project utilizes [MDESops](https://gitlab.eecs.umich.edu/M-DES-tools/desops) as a dependency to represent and construct automata.

## Installation
A recent version of Python is required (at least 3.9.6).
Poetry is used to manage the project. It can be installed using the instructions provided here: [https://python-poetry.org/docs/](https://python-poetry.org/docs/).

In the main directory, the project can be installed with:

    $ poetry install

## Examples
The project contains several examples (with minimal documentation) in the `examples` directory. They can be run with the command:

	$ poetry run python examples/example_name.py

## Tests
This repository employs [pytest](https://docs.pytest.org/en/latest/) to write tests. All tests are located in `tests` directory, and must be written with the formats of `pytest`.

You can execute tests by the following command:
```
$ poetry run pytest
```
