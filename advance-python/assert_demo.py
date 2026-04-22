# ------------------------------------------------------------
# What is assert?
# ------------------------------------------------------------

# The assert statement is used to check whether a condition is True.

x = 10

assert x > 0
# This passes, because x > 0 is True.

assert x == 10
# This also passes, because x is exactly 10.

# If the condition is False, Python raises an AssertionError.

# assert x < 0
# This would fail, because x < 0 is False and
# Python would raise an AssertionError

age = 17

assert age >= 18, "The user must be at least 18 years old"
# This fails and raises:
# AssertionError: The user must be at least 18 years old

def add(a, b):
    return a + b


assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(10, 0) == 10

# These assertions check whether the function gives the expected result.

def add(a, b):
    return a + b


def test_add_two_positive_numbers():
    result = add(2, 3)
    assert result == 5

result = add(2, 3)

assert result == 5
# We check whether the actual result is equal to the expected result.
# If result == 5 is True, the test passes.
# If result == 5 is False, the test fails and Python raises an AssertionError.

# What is a unit test?
# A unit test checks one small part of a program, usually one function or one method.
# The goal is to verify that a small piece of code behaves exactly as expected.
# For example, if we have this function:

def multiply(a, b):
    return a * b

def test_multiply_two_positive_numbers():
    assert multiply(2, 3) == 6


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


def test_multiply_negative_number():
    assert multiply(-2, 3) == -6

# Each test checks one expected behavior.

# Why do we write unit tests?
# Unit tests help us check that our code works correctly.
# They are especially useful because they can be run automatically.
# If we later change the code and accidentally break something, the tests
# can reveal the problem quickly.
# So instead of manually checking everything again and again, we let
# the tests act like
# tiny automated inspectors. Tiny grumpy inspectors, but useful ones.

# Basic pytest example:
# In pytest, test functions usually start with test_.

def is_positive(number):
    return number > 0


def test_positive_number():
    assert is_positive(5)


def test_negative_number():
    assert not is_positive(-3)


def test_zero_is_not_positive():
    assert not is_positive(0)

# Explanation:

assert is_positive(5)

# This means:
# “We expect is_positive(5) to return True.”

assert not is_positive(-3)

# This means:
# “We expect is_positive(-3) to return False.”

# Testing exceptions:
# Sometimes we expect the code to raise an error.

# For example:

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# With pytest, we can test this using pytest.raises():

import pytest


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(10, 0)

# This test passes only if divide(10, 0) raises a ValueError.
# If no error is raised, the test fails.
# If a different type of error is raised, the test also fails.s