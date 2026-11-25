"""Convert a user-entered decimal integer into binary and hexadecimal."""


def main() -> None:
    """Prompt for a decimal integer and print its binary and hexadecimal forms."""
    raw_value = input("Enter a decimal number: ").strip()

    try:
        decimal_number = int(raw_value)
    except ValueError:
        print("Invalid input. Please enter a whole decimal number (for example, 25).")
        return

    binary_value = bin(decimal_number)
    hex_value = hex(decimal_number)

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_value}")
    print(f"Hexadecimal: {hex_value}")


if __name__ == "__main__":
    main()
