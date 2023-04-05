import pytest
from main import get_current_player


@pytest.mark.parametrize(("value", "expected_result"), (
    (4, "X"),
    (3, "O"),
))
def test_get_current_player(value, expected_result):
    result = get_current_player(value)
    assert result == expected_result
