# Basic Calculator Library

A Python library for performing basic arithmetic and advanced mathematical operations with precision and robust error handling.

## Features

- Basic arithmetic: Addition, Subtraction, Multiplication, Division
- Advanced operations: Power, Square Root, Percentage, Add Percentage
- Handles edge cases like division by zero and invalid input types.
- Uses Python's `decimal` module for high precision calculations.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/asadmirza6/Gemini-cli-cal.git # Replace with your repo if different
    cd Gemini-cli-cal
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Example

```python
from src.calculator.operations import add, subtract, multiply, divide, power, sqrt, percent, add_percent
from src.calculator.exceptions import InvalidInputError
from decimal import Decimal

# Basic Operations
print(f"2 + 3 = {add(2, 3)}") # Output: 5
print(f"5 - 2 = {subtract(5, 2)}") # Output: 3
print(f"2 * 3 = {multiply(2, 3)}") # Output: 6
print(f"6 / 3 = {divide(6, 3)}") # Output: 2

# Advanced Operations
print(f"2 ^ 3 = {power(2, 3)}") # Output: 8
print(f"sqrt(9) = {sqrt(9)}") # Output: 3
print(f"50% of 200 = {multiply(200, percent(50))}") # Output: 100.0
print(f"200 + 10% = {add_percent(200, 10)}") # Output: 220

# Decimal precision
print(f"Decimal add: {add(Decimal('0.1'), Decimal('0.2'))}") # Output: 0.3
print(f"Decimal sqrt: {sqrt(Decimal('25'))}") # Output: 5

# Error Handling
try:
    divide(1, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}") # Output: Error: Cannot divide by zero.

try:
    add("a", 3)
except InvalidInputError as e:
    print(f"Error: {e}") # Output: Error: Both inputs must be numeric for addition.

try:
    sqrt(-1)
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Cannot calculate square root of a negative number for real results.
```

## Running Tests

To run the unit tests, navigate to the project root and execute:

```bash
pytest tests/
```

To run tests with coverage report:

```bash
pytest --cov=src/calculator tests/
```
