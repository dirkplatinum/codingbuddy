# codingbuddy

## Calculator

`calculator.py` evaluates a single expression made of two numbers and one
operator. The supported operators are:

| Operator | Operation      |
| -------- | -------------- |
| `+`      | addition       |
| `-`      | subtraction    |
| `*`      | multiplication |
| `/`      | division       |

### From Python

```python
from calculator import calculate

calculate(2, "+", 3)  # 5
calculate(7, "/", 2)  # 3.5
```

`calculate` raises `ValueError` when the operator is not one of the symbols
listed above.

### From the command line

```console
$ python calculator.py 7 / 2
3.5
```

Operands are read as floating point numbers, so results are printed as floats.
Quote the operator when your shell would expand it, for example
`python calculator.py 6 '*' 7`.

### Division by zero

Dividing by zero is not an error: `calculate` returns the string
`"Error: division by zero"`, and the command line prints that message and exits
with status `0`.
