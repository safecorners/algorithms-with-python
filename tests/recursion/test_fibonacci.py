import pytest

from recursion.fibonacci import fib


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_fibonacci(n: int, expected: int) -> None:
    assert fib(n) == expected
