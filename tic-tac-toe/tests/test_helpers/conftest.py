import pytest


@pytest.fixture
def available_choices():
    return list(range(1, 10))
