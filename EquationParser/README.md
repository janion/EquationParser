# Equation Parser
### Or more accurately a function parser

This python library will take a function of variables x, y & t in plain text from and convert it into an object which can be evaluated given the values of x, y & t.

The supported functions are:
- \+ Plus
- \- Minus
- \* Multiply
- / Divide
- % Modulo
- ^ Power
- sin Sine
- cos Cosine
- tan Tangent
- exp Exponential
- log Natural logarithm
- abs Modulus

Order of operations is supported by modifying the string to match one where all brackets contain only a single operation.

## Future work:
- Add support for multiplication without the "*" operator explicitly used (eg. "2x" or "x(x + 2)").
- Add support for arbitrary variables instead of limiting to x, y & t.