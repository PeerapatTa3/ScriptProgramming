# lab6_1.py - Lab 6.1: Simple Calculator Functions

def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the result of a minus b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """Returns a divided by b, or an error message if b is zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    """Returns base raised to exponent (defaults to squaring)."""
    return base ** exponent


def get_float(prompt, allow_blank=False):
    """Prompts for a float, re-prompting on invalid input. Returns None if blank and allow_blank."""
    while True:
        value = input(prompt)
        if allow_blank and value == "":
            return None
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (base ** exponent, default exponent=2)")
        print("6. Quit")
        choice = input("Choose an operation (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice. Please try again.")
            continue

        num1 = get_float("Enter the first number: ")

        if choice == "5":
            exponent = get_float(
                "Enter an exponent (leave blank for default 2): ", allow_blank=True
            )
            result = power(num1) if exponent is None else power(num1, exponent)
        else:
            num2 = get_float("Enter the second number: ")
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
