# API Contracts: Basic Calculator Library

## Functions

### `add(num1: Union[int, float, Decimal], num2: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns the sum of two numbers.
**Raises**: `TypeError` if inputs are not numeric.

### `subtract(num1: Union[int, float, Decimal], num2: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns the difference of two numbers (`num1 - num2`).
**Raises**: `TypeError` if inputs are not numeric.

### `multiply(num1: Union[int, float, Decimal], num2: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns the product of two numbers.
**Raises**: `TypeError` if inputs are not numeric.

### `divide(num1: Union[int, float, Decimal], num2: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns the quotient of two numbers (`num1 / num2`).
**Raises**: `TypeError` if inputs are not numeric. `ZeroDivisionError` if `num2` is zero.

### `power(base: Union[int, float, Decimal], exponent: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns `base` raised to the power of `exponent`.
**Special Case**: `0^0` returns `1`.
**Raises**: `TypeError` if inputs are not numeric.

### `sqrt(num: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Returns the square root of a number.
**Raises**: `TypeError` if input is not numeric. `ValueError` if `num` is negative (for real results).

### `percent(num: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Converts a number to its percentage equivalent (e.g., `50` returns `0.5`).
**Raises**: `TypeError` if input is not numeric.

### `add_percent(value: Union[int, float, Decimal], percentage: Union[int, float, Decimal]) -> Union[int, float, Decimal]`
**Description**: Adds a percentage of a value to the value itself (e.g., `add_percent(200, 10)` returns `220`).
**Raises**: `TypeError` if inputs are not numeric.
