import pytest
from main_code import sum_strings


@pytest.mark.parametrize('x, y, expected', [
    ('1', '5', '6'),
    ('123', '321', '444'),
    ('999', '111', '1110'),
    ('123456789', '987654321', '1111111110'),
    ('1', '123', '124'),
])
def test_convert_positive(x, y, expected):
    assert sum_strings(x, y) == expected
