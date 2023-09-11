from pydantic import validate_arguments

@validate_arguments
def sum(x: float, y: float) -> float:
    return x + y
