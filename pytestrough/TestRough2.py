import pytest
@pytest.mark.skip
def test_total_num_divisible_By3(input_total):
    assert input_total % 3 == 0

@pytest.mark.skip
def test_total_num_divisible_By6(input_total):
    assert input_total % 6 == 0