# Data Model: Basic Calculator Library

## Entities

### Number

**Description**: Represents any numeric value used in calculator operations.

**Attributes**:
- **value**: The actual numeric value. Can be an integer or a floating-point number.
- **type**: Implicitly determined by Python (int, float, or Decimal if used).

**Relationships**:
- None (Numbers are atomic operands in this context).
