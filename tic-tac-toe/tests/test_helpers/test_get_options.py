import pytest
from main import get_options


@pytest.mark.parametrize(("board", "expected_result"), (
    (
        [[None, None, None], [None, None, None], [None, None, None]],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ),
    (
        [["X", None, None], [None, None, None], [None, None, None]],
        [2, 3, 4, 5, 6, 7, 8, 9]
    ),
    (
        [["X", None, None], [None, "O", None], [None, None, None]],
        [2, 3, 4, 6, 7, 8, 9]
    )
))
def test_get_options(board, expected_result):
    result = get_options(board)
    assert result == expected_result
