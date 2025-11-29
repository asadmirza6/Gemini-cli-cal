import logging
from typing import Union
from decimal import Decimal, getcontext
import math
from src.calculator.exceptions import InvalidInputError, Numeric # Import Numeric and InvalidInputError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def _is_numeric(value):
    return isinstance(value, (int, float, Decimal))

def add(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Returns the sum of two numbers.

    Args:
        num1 (Numeric): The first number.
        num2 (Numeric): The second number.

    Returns:
        Numeric: The sum of num1 and num2.

    Raises:
        InvalidInputError: If either num1 or num2 is not a valid numeric type.
    """
    if not _is_numeric(num1) or not _is_numeric(num2):
        logging.error(f"InvalidInputError in add: Both inputs must be numeric. Got num1={type(num1)}, num2={type(num2)}")
        raise InvalidInputError("Both inputs must be numeric for addition.")
    
    # Convert to Decimal for precise calculations if either input is float or Decimal
    if isinstance(num1, float) or isinstance(num2, float):
        return float(num1) + float(num2)
    if isinstance(num1, Decimal) or isinstance(num2, Decimal):
        getcontext().prec = 28 # Ensure sufficient precision for Decimal operations
        return Decimal(str(num1)) + Decimal(str(num2))
    
    return num1 + num2

def subtract(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Returns the difference of two numbers (num1 - num2).

    Args:
        num1 (Numeric): The first number.
        num2 (Numeric): The second number.

    Returns:
        Numeric: The difference of num1 and num2.

    Raises:
        InvalidInputError: If either num1 or num2 is not a valid numeric type.
    """
    if not _is_numeric(num1) or not _is_numeric(num2):
        logging.error(f"InvalidInputError in subtract: Both inputs must be numeric. Got num1={type(num1)}, num2={type(num2)}")
        raise InvalidInputError("Both inputs must be numeric for subtraction.")

    # Convert to Decimal for precise calculations if either input is float or Decimal
    if isinstance(num1, float) or isinstance(num2, float):
        return float(num1) - float(num2)
    if isinstance(num1, Decimal) or isinstance(num2, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return Decimal(str(num1)) - Decimal(str(num2))

    return num1 - num2

def multiply(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Returns the product of two numbers.

    Args:
        num1 (Numeric): The first number.
        num2 (Numeric): The second number.

    Returns:
        Numeric: The product of num1 and num2.

    Raises:
        InvalidInputError: If either num1 or num2 is not a valid numeric type.
    """
    if not _is_numeric(num1) or not _is_numeric(num2):
        logging.error(f"InvalidInputError in multiply: Both inputs must be numeric. Got num1={type(num1)}, num2={type(num2)}")
        raise InvalidInputError("Both inputs must be numeric for multiplication.")

    # Convert to Decimal for precise calculations if either input is float or Decimal
    if isinstance(num1, float) or isinstance(num2, float):
        return float(num1) * float(num2)
    if isinstance(num1, Decimal) or isinstance(num2, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return Decimal(str(num1)) * Decimal(str(num2))

    return num1 * num2

def divide(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Returns the quotient of two numbers (num1 / num2).

    Args:
        num1 (Numeric): The numerator.
        num2 (Numeric): The denominator.

    Returns:
        Numeric: The quotient of num1 and num2.

    Raises:
        InvalidInputError: If either num1 or num2 is not a valid numeric type.
        ZeroDivisionError: If num2 is zero.
    """
    if not _is_numeric(num1) or not _is_numeric(num2):
        logging.error(f"InvalidInputError in divide: Both inputs must be numeric. Got num1={type(num1)}, num2={type(num2)}")
        raise InvalidInputError("Both inputs must be numeric for division.")
    
    if num2 == 0:
        logging.error(f"ZeroDivisionError in divide: Attempted to divide by zero. num1={num1}, num2={num2}")
        raise ZeroDivisionError("Cannot divide by zero.")

    # Convert to Decimal for precise calculations if either input is float or Decimal
    if isinstance(num1, float) or isinstance(num2, float):
        return float(num1) / float(num2)
    if isinstance(num1, Decimal) or isinstance(num2, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return Decimal(str(num1)) / Decimal(str(num2))

    return num1 / num2

def power(base: Numeric, exponent: Numeric) -> Numeric:
    """
    Returns the base raised to the power of the exponent.

    Args:
        base (Numeric): The base number.
        exponent (Numeric): The exponent.

    Returns:
        Numeric: The result of base ** exponent.

    Raises:
        InvalidInputError: If either base or exponent is not a valid numeric type.
    """
    if not _is_numeric(base) or not _is_numeric(exponent):
        logging.error(f"InvalidInputError in power: Both inputs must be numeric. Got base={type(base)}, exponent={type(exponent)}")
        raise InvalidInputError("Both inputs must be numeric for power operation.")

    # Handle 0^0 case as per spec
    if base == 0 and exponent == 0:
        return 1

    # Convert to Decimal for precise calculations if either input is float or Decimal
    if isinstance(base, float) or isinstance(exponent, float):
        return float(base) ** float(exponent)
    if isinstance(base, Decimal) or isinstance(exponent, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return Decimal(str(base)) ** Decimal(str(exponent))

    return base ** exponent

def sqrt(num: Numeric) -> Numeric:
    """
    Returns the square root of a number.

    Args:
        num (Numeric): The number.

    Returns:
        Numeric: The square root of num.

    Raises:
        InvalidInputError: If num is not a valid numeric type.
        ValueError: If num is negative (for real results).
    """
    if not _is_numeric(num):
        logging.error(f"InvalidInputError in sqrt: Input must be numeric. Got num={type(num)}")
        raise InvalidInputError("Input must be numeric for square root operation.")
    
    if num < 0:
        logging.error(f"ValueError in sqrt: Cannot calculate square root of a negative number. Got num={num}")
        raise ValueError("Cannot calculate square root of a negative number for real results.")

    # Convert to Decimal for precise calculations if input is float or Decimal
    if isinstance(num, float):
        return math.sqrt(num)
    if isinstance(num, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return num.sqrt() # Decimal type has its own sqrt method

    return math.sqrt(num) # For int, it will return float

def percent(num: Numeric) -> Numeric:
    """
    Converts a number to its percentage equivalent (e.g., 50 returns 0.5).

    Args:
        num (Numeric): The number to convert.

    Returns:
        Numeric: The percentage equivalent (num / 100).

    Raises:
        InvalidInputError: If num is not a valid numeric type.
    """
    if not _is_numeric(num):
        logging.error(f"InvalidInputError in percent: Input must be numeric. Got num={type(num)}")
        raise InvalidInputError("Input must be numeric for percentage conversion.")
    
    # Convert to Decimal for precise calculations if input is float or Decimal
    if isinstance(num, float):
        return num / 100.0
    if isinstance(num, Decimal):
        getcontext().prec = 28  # Ensure sufficient precision for Decimal operations
        return num / Decimal('100')
    
    return num / 100

def add_percent(value: Numeric, percentage: Numeric) -> Numeric:
    """
    Adds a percentage of a value to the value itself (e.g., add_percent(200, 10) returns 220).

    Args:
        value (Numeric): The base value.
        percentage (Numeric): The percentage to add (e.g., 10 for 10%).

    Returns:
        Numeric: The value plus the calculated percentage.

    Raises:
        InvalidInputError: If either value or percentage is not a valid numeric type.
    """
    if not _is_numeric(value) or not _is_numeric(percentage):
        logging.error(f"InvalidInputError in add_percent: Both inputs must be numeric. Got value={type(value)}, percentage={type(percentage)}")
        raise InvalidInputError("Both inputs must be numeric for add_percent operation.")
    
    # Calculate the percentage amount
    percentage_amount = multiply(value, percent(percentage))

    # Add the percentage amount to the original value
    return add(value, percentage_amount)
