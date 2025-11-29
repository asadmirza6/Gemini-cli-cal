# Feature Specification: Basic Calculator Library

**Feature Branch**: `001-basic-calculator-spec`
**Created**: 2025-11-29
**Status**: Draft
**Input**: User description: "building calculator for basic operation. let's use the above discussion as our specification requirements"

## Summary

A Python library providing core mathematical operations for numerical calculations. It aims for precision, robustness in handling edge cases, and a clear, extensible interface for basic arithmetic.

## User Scenarios & Testing

### User Story 1 - Basic Arithmetic (Priority: P1)
*Description:* As a developer, I want to perform basic arithmetic operations (addition, subtraction, multiplication, division) on numbers and get accurate results.

*Acceptance Scenarios:*
1.  **Given** two valid numbers, **When** I use the `add` function, **Then** it returns their sum.
2.  **Given** two valid numbers, **When** I use the `subtract` function, **Then** it returns their difference.
3.  **Given** two valid numbers, **When** I use the `multiply` function, **Then** it returns their product.
4.  **Given** two valid numbers (divisor not zero), **When** I use the `divide` function, **Then** it returns their quotient with defined precision.

### User Story 2 - Advanced Operations (Priority: P2)
*Description:* As a developer, I want to use advanced mathematical operations like power, square root, and percentage with reliable results.

*Acceptance Scenarios:*
1.  **Given** a base and an exponent, **When** I use the `power` function, **Then** it returns the base raised to the exponent.
2.  **Given** a non-negative number, **When** I use the `sqrt` function, **Then** it returns its square root with defined precision.
3.  **Given** a number and a percentage, **When** I use the `percentage` function, **Then** it returns the calculated percentage value based on the specified behavior.

### Edge Cases (Priority: P1 - Critical for Robustness)
*Description:* The library must handle common mathematical and input-related edge cases gracefully, providing clear error signals.

*Acceptance Scenarios:*
1.  **Given** a division operation, **When** the divisor is zero, **Then** it raises a `ZeroDivisionError`.
2.  **Given** an operation with non-numeric input, **When** the function is called, **Then** it raises a `TypeError` or `InvalidInputError`.
3.  **Given** a `sqrt` operation, **When** the input is negative (and complex numbers are not supported), **Then** it raises a `ValueError`.
4.  **Given** specific limits of floating-point representation, **When** an operation exceeds them, **Then** it handles overflow/underflow according to Python's `float` behavior or `Decimal` context.
5. Given `0^0`, **When** the `power` function is called, **Then** it returns `1`.
6.  **Given** percentage operations, **When** the specific context is unclear (e.g., `50%` alone vs. `200 + 10%`), **Then** it adheres to the pre-defined behavior for each scenario (e.g., `percent(50)` returns `0.5`; `add_percent(value, percentage)`).

## Requirements

### Functional Requirements
*   **FR-001**: The library MUST provide functions for addition, subtraction, multiplication, and division.
*   **FR-002**: The library MUST provide functions for exponentiation (`power`), square root (`sqrt`), and percentage (`percent`).
*   **FR-003**: All functions MUST accept numeric inputs (integers and floats).
*   **FR-004**: Division by zero MUST raise a `ZeroDivisionError`.
*   **FR-005**: Invalid input types (e.g., strings) MUST raise a `TypeError` or a custom `InvalidInputError`.
*   **FR-006**: Square root of negative numbers (for real results) MUST raise a `ValueError`.
*   **FR-007**: The percentage function MUST operate as a direct conversion (e.g., `percent(50)` returns `0.5`) and as an operator when combined (e.g., `add_percent(value, percent)`).

### Key Entities
*   **Number**: Any valid Python integer or floating-point number.

## Success Criteria

### Measurable Outcomes
*   **SC-001**: All core arithmetic operations (`add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `percent`) MUST return results that are accurate within a defined `epsilon` tolerance of `1e-9` when using standard floats, or exact when using `Decimal` if that is chosen.
*   **SC-002**: All specified edge cases (division by zero, invalid input types, negative square root) MUST raise the appropriate, documented Python exceptions.
*   **SC-003**: The library's public API MUST consist of clearly named functions (e.g., `add`, `subtract`, etc.) that are easily callable and predictable.
*   **SC-004**: The library MUST utilize Python's `decimal` module for all calculations requiring high precision, with a default precision of at least 28 decimal places (or other specified precision).
*   **SC-005**: All functions dealing with floating-point numbers MUST include a mechanism for comparison using a specified tolerance (epsilon) rather than direct equality.
*   **SC-006**: The calculator MUST operate correctly according to PEMDAS/BODMAS rules when chained operations are involved (if applicable to the chosen API design, e.g., expression parsing).
