import pytest
from src.calculator.operations import add, subtract, multiply, divide, power, sqrt, percent, add_percent # Add add_percent to import
from src.calculator.exceptions import InvalidInputError
from decimal import Decimal, getcontext

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_floats():
    assert add(2.5, 3.5) == 6.0
    assert add(-2.5, 3.5) == 1.0

def test_add_decimal_numbers():
    getcontext().prec = 28 # Ensure sufficient precision for Decimal tests
    assert add(Decimal('2.5'), Decimal('3.5')) == Decimal('6.0')
    assert add(Decimal('-2.5'), Decimal('3.5')) == Decimal('1.0')

def test_add_invalid_input_type():
    with pytest.raises(InvalidInputError):
        add("a", 3)
    with pytest.raises(InvalidInputError):
        add(2, "b")
    with pytest.raises(InvalidInputError):
        add(None, 5)

# --- Tests for subtract function ---
def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_mixed_numbers():
    assert subtract(5, -2) == 7
    assert subtract(-5, 2) == -7

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0

def test_subtract_floats():
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(-5.5, 2.5) == -8.0

def test_subtract_decimal_numbers():
    getcontext().prec = 28
    assert subtract(Decimal('5.5'), Decimal('2.5')) == Decimal('3.0')
    assert subtract(Decimal('-5.5'), Decimal('2.5')) == Decimal('-8.0')

def test_subtract_invalid_input_type():
    with pytest.raises(InvalidInputError):
        subtract("a", 3)
    with pytest.raises(InvalidInputError):
        subtract(2, "b")

# --- Tests for multiply function ---
def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 2.0) == 5.0
    assert multiply(-2.5, 2.0) == -5.0

def test_multiply_decimal_numbers():
    getcontext().prec = 28
    assert multiply(Decimal('2.5'), Decimal('2.0')) == Decimal('5.0')
    assert multiply(Decimal('-2.5'), Decimal('2.0')) == Decimal('-5.0')

def test_multiply_invalid_input_type():
    with pytest.raises(InvalidInputError):
        multiply("a", 3)
    with pytest.raises(InvalidInputError):
        multiply(2, "b")

# --- Tests for divide function ---
def test_divide_positive_numbers():
    assert divide(6, 3) == 2

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2

def test_divide_mixed_numbers():
    assert divide(-6, 3) == -2

def test_divide_zero_numerator():
    assert divide(0, 5) == 0

def test_divide_floats():
    assert divide(5.0, 2.0) == 2.5
    assert divide(-5.0, 2.0) == -2.5

def test_divide_decimal_numbers():
    getcontext().prec = 28
    assert divide(Decimal('5.0'), Decimal('2.0')) == Decimal('2.5')
    assert divide(Decimal('-5.0'), Decimal('2.0')) == Decimal('-2.5')

def test_divide_invalid_input_type():
    with pytest.raises(InvalidInputError):
        divide("a", 3)
    with pytest.raises(InvalidInputError):
        divide(2, "b")

def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(Decimal('5'), Decimal('0'))

# --- Tests for power function ---
def test_power_positive_numbers():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1
    assert power(0, 0) == 1 # Special case from spec

def test_power_negative_exponent():
    assert power(2, -3) == 0.125
    assert power(4, -0.5) == 0.5

def test_power_floats():
    assert power(2.5, 2.0) == 6.25
    assert power(4.0, 0.5) == 2.0 # Square root

def test_power_decimal_numbers():
    getcontext().prec = 28
    assert power(Decimal('2.5'), Decimal('2.0')) == Decimal('6.25')
    assert power(Decimal('4.0'), Decimal('0.5')) == Decimal('2.0')

def test_power_invalid_input_type():
    with pytest.raises(InvalidInputError):
        power("a", 3)
    with pytest.raises(InvalidInputError):
        power(2, "b")

# --- Tests for sqrt function ---
def test_sqrt_positive_number():
    assert sqrt(9) == 3

def test_sqrt_zero():
    assert sqrt(0) == 0

def test_sqrt_float():
    assert sqrt(6.25) == 2.5

def test_sqrt_decimal_number():
    getcontext().prec = 28
    assert sqrt(Decimal('6.25')) == Decimal('2.5')

def test_sqrt_invalid_input_type():
    with pytest.raises(InvalidInputError):
        sqrt("a")
    with pytest.raises(InvalidInputError):
        sqrt(None)

def test_sqrt_negative_number_error():
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number for real results."):
        sqrt(-9)
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number for real results."):
        sqrt(Decimal('-9'))

# --- Tests for percent function ---
def test_percent_positive_number():
    assert percent(50) == 0.5
    assert percent(Decimal('25')) == Decimal('0.25')

def test_percent_zero():
    assert percent(0) == 0.0

def test_percent_float():
    assert percent(75.5) == 0.755
    assert percent(Decimal('1.25')) == Decimal('0.0125')

def test_percent_invalid_input_type():
    with pytest.raises(InvalidInputError):
        percent("abc")
    with pytest.raises(InvalidInputError):
        percent(None)

# --- Tests for add_percent function ---
def test_add_percent_positive_number():
    assert add_percent(200, 10) == 220
    assert add_percent(Decimal('100'), Decimal('20')) == Decimal('120')

def test_add_percent_zero_value():
    assert add_percent(0, 10) == 0

def test_add_percent_zero_percentage():
    assert add_percent(200, 0) == 200

def test_add_percent_negative_value():
    assert add_percent(-100, 10) == -110.0

def test_add_percent_float():
    assert add_percent(150.0, 5.0) == 157.5

def test_add_percent_invalid_input_type():
    with pytest.raises(InvalidInputError):
        add_percent("abc", 10)
    with pytest.raises(InvalidInputError):
        add_percent(100, "xyz")