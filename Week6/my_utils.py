# my_utils.py - Custom module for Lab 6.2

def greet(name):
    """Prints a greeting message to the given name."""
    print(f"Hello, {name}!")


def is_prime(number):
    """Returns True if number is prime, False otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
