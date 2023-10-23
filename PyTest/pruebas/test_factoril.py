import pytest
from prueba1 import suma

@pytest.mark.parametrize(
"num1 , num2 , expected",
[
    (1,1,2),
    (3,6,9),
    (7,5,12),
    (5,1,6), 
    (9,3,12)
])
def test_factorial_params(num1 , num2 , expected):
    assert suma(num1,num2) == expected