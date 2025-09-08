
def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * 5.0 / 9.0


def _normalize_unit(unit: str) -> str | None:
    """Normalize user-entered unit to 'c' or 'f'. Returns None if unknown."""
    if not unit:
        return None
    u = unit.strip().lower()
    if u in ("c", "celsius"):
        return "c"
    if u in ("f", "fahrenheit"):
        return "f"
    return None


if __name__ == "__main__":
    # Read temperature value
    try:
        raw = input("Enter temperature value: ").strip()
        value = float(raw)
    except ValueError:
        print("Error: please enter a numeric temperature value.")
    else:
        unit = input("Enter unit ('C' for Celsius or 'F' for Fahrenheit): ").strip()
        norm = _normalize_unit(unit)
        if norm == "c":
            converted = c_to_f(value)
            print(f"{value:.2f}°C is {converted:.2f}°F")
        elif norm == "f":
            converted = f_to_c(value)
            print(f"{value:.2f}°F is {converted:.2f}°C")
        else:
            print("Error: unit must be 'C'/'Celsius' or 'F'/'Fahrenheit'.")
