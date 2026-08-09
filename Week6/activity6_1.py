# activity6_1.py - Activity 6.1: Refactoring the Week 2 Number Classifier lab using functions

def is_positive_negative_zero(num):
    """Classifies a number as positive, negative, or zero."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def is_even_odd(num):
    """Classifies a number as even or odd."""
    return "even" if num % 2 == 0 else "odd"


def main():
    num = float(input("Enter a number to classify: "))
    print(f"{num} is {is_positive_negative_zero(num)} and {is_even_odd(num)}.")


if __name__ == "__main__":
    main()
