import pytest

def test_total_num_divisible_By5(input_total):
    assert input_total % 5 == 0

def test_total_num_divisible_By10(input_total):
    assert input_total % 10 == 0

def test_total_num_divisible_By9(input_total):
    assert input_total % 9 == 0