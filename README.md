# CalculatorInReversePolishNotation
Calculator in Reverse Polish Notation

the calculator will be able to handle arbitrary functions on floating point numbers, 
specified in Reverse Polish Notation, which removes the need for worrying about parentheses in mathematical expressions.

Ultimately, we will implement this calculator as a function evaluate(expression, stack, binary_operations, unary_operations), 
which will take four arguments:

a string containing a mathematical expression in RPN
a list to be used as the stack 
a dictionary mapping names of binary operators to functions that compute their results
a dictionary mapping names of unary operators to functions that compute their results

Your function should evaluate the given expression and return the result.
