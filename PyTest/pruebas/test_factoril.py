import pytest
from practica2 import fahren

@pytest.mark.parametrize(
"Celsi , expected",
[
    (1,33.8),
    (3,37.4),
    (7,44.6),
    (5,41.0), 
    (9,48.2)
])
def test_factorial_params(Celsi, expected):
    assert fahren(Celsi) == expected