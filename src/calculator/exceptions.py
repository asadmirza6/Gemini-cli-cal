from typing import Union

class InvalidInputError(TypeError):
    """
    Custom exception raised when an operation receives an invalid input type.
    Inherits from TypeError for consistency with Python's built-in type errors.
    """
    def __init__(self, message: str = "Invalid input type provided."):
        self.message = message
        super().__init__(self.message)

# Define numeric types for type hints
Numeric = Union[int, float]
