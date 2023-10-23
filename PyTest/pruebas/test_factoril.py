import pytest
from factorial import factor

@pytest.mark.parametrize(
"num, cont , inicio , guarda , expected",
[
    (1,1),
    (3,6),
    (7,5040),
    (5,120), 
    (9,362880)
])
def test_factorial_params(num, expected):
    assert factor(num) == expected