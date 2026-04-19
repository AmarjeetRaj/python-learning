# Python Learning Summary

## Overview
This repository shows a progressive learning path through Python core concepts, from input/output and arithmetic to functions, control flow, file handling, regular expressions, object-oriented programming, and testing.

## Basic Syntax and Input/Output
- `hello.py` — functions, default parameters, string formatting, `if __name__ == "__main__"`, and `input()`.
- `calculator.py` — numeric input conversion, arithmetic operators, rounding, formatted output.
- `advanced_calculator.py` — function definitions, return values, and a simple main program pattern.
- `average.py` — using the standard library (`statistics.mean`) for built-in functionality.
- `say.py` / `sayings.py` — splitting code into imports, modules, and reusable functions.

## Control Flow
- `compare.py` — `if`, `elif`, `else`, comparison operators, and boolean logic.
- `grade.py` — chained comparisons and progressive refinement of conditionals.
- `loop.py` — `for` loops, `while` loops, input validation, and control flow with `break`.
- `house.py` — pattern matching with `match/case` in Python 3.10+.
- `hogwarts.py` — list iteration, dictionary access, and multiple loop styles.

## Functions, Parameters, and Return Values
- `parity.py` — small helper functions and using return values for program logic.
- `yell.py` — variable-length positional arguments (`*args`) and list comprehensions.
- `unpack.py` — unpacking dictionaries with `**kwargs`, positional vs named arguments, and a small helper function.
- `meows.py` — type hints, docstrings, `argparse`, and function-based program structure.

## File and Data Handling
- `names.py` — reading text files, iterating over file lines, strip/rstrip, and sorting output.
- `students.py` — parsing CSV-style data, lists of dictionaries, sorting with named functions and lambdas.
- `harrypotter.py` — reading CSV files with `csv.DictReader`, building lists of dictionaries, and sorting with lambdas.
- `csvwritter.py` — writing CSV rows with `csv.DictWriter` and using `with open(...)`.

## Regular Expressions and Validation
- `format.py` — basic use of `re.search`, capturing groups, string reformatting, and the walrus operator (`:=`).
- `twitter.py` — matching URLs with regex, optional protocol and subdomain handling.
- `validate.py` — validating email input with regex and case-insensitive matching.

## Exception Handling and Error Control
- `exception.py` — handling invalid input with `try/except`, specifically `ValueError`, and looping until valid input.

## Command-Line Arguments and Modules
- `cmdline.py` — reading `sys.argv`, validating argument count, and printing command-line parameters.
- `meows.py` — also demonstrates `argparse` for more robust CLI parsing.

## Object-Oriented Programming
- `bank.py` — classes, encapsulation with private attributes, properties, and basic methods.
- `vault.py` — custom classes with `__init__`, `__str__`, and operator overloading via `__add__`.
- `OOP/student.py` — class methods, properties with getters/setters, validation, `__str__`, and `match/case` logic.
- `OOP/hat.py` — class variables, class methods, and using `random.choice` inside a class context.
- `wizard.py` — inheritance, `super()`, and specialized subclasses.

## External Libraries and APIs
- `generate.py` — using the `random` module for choice, randint, and shuffling.
- `itunes.py` — making HTTP requests with `requests`, parsing JSON, and using command-line arguments for API queries.

## Testing
- `test_calculator.py` — unit tests with `pytest`, assertions, and exception testing.

## Learning Takeaways
- Start with basic I/O, arithmetic, and string formatting.
- Move into branching, loops, and data validation.
- Use functions and modules to organize code and reuse logic.
- Practice file I/O and CSV handling for practical data workflows.
- Learn regular expressions to validate and parse text input.
- Understand exceptions to make programs robust.
- Explore object-oriented design with classes, inheritance, properties, and operator overloading.
- Use built-in libraries like `random`, `csv`, `re`, and `requests` to extend Python beyond core syntax.
- Add tests early to verify behavior and prevent regressions.

## Suggested Review Order
1. `hello.py`, `calculator.py`, `advanced_calculator.py`
2. `compare.py`, `grade.py`, `loop.py`, `exception.py`
3. `say.py`, `sayings.py`, `parity.py`, `yell.py`, `unpack.py`
4. `names.py`, `students.py`, `harrypotter.py`, `csvwritter.py`
5. `format.py`, `twitter.py`, `validate.py`
6. `bank.py`, `vault.py`, `OOP/student.py`, `OOP/hat.py`, `wizard.py`
7. `generate.py`, `itunes.py`, `test_calculator.py`
