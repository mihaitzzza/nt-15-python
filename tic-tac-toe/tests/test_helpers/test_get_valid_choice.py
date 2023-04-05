from helpers import get_valid_choice
from unittest.mock import MagicMock, call


def test_get_valid_choice_valid_choice(monkeypatch, available_choices):
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "2")

    result = get_valid_choice(available_choices)
    assert result == 2


def test_get_valid_choice_invalid_choice(monkeypatch, available_choices):
    # mocked_input = MagicMock(return_value="2")
    mocked_input = MagicMock(side_effect=("abc", "12", "4"))
    mocked_print = MagicMock()

    monkeypatch.setattr("builtins.input", mocked_input)
    monkeypatch.setattr("builtins.print", mocked_print)

    result = get_valid_choice(available_choices)
    assert result == 4
    assert mocked_print.call_count == 2
    mocked_print.assert_has_calls([
        call("Your choice is not valid."),
        call("Your choice is not valid.")
    ])
