import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ...,
)
def test_1(solution: Solution, ...):
    pass


@pytest.mark.parametrize(
    ...,
)
def test_2(solution: Solution, ...):
    pass


@pytest.mark.parametrize(
    ...,
)
def test_3(solution: Solution, ...):
    pass
