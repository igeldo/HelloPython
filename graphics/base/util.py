def check_float(value: float, name: str = "value") -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} can only be a float or int")
    return float(value)


def check_float_positive(value: float, name: str = "value") -> float:
    result = check_float(value, name)
    if result <= 0.0:
        raise ValueError(f"{name} must be greater than zero")
    return result
