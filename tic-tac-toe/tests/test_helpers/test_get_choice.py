import pytest
from helpers import get_choice


# @pytest.fixture
# def my_fixture():
#     return [1, 2, 3]
#
#
# def test_get_choice(my_fixture):
#     print('my_fixture', my_fixture)


# def test_get_choice(monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "2")
#
#     available_choices = list(range(1, 10))
#     choice = get_choice(available_choices)
#     assert choice == 2


# def test_get_choice(monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "abc")
#
#     available_choices = list(range(1, 10))
#
#     with pytest.raises(ValueError):
#         get_choice(available_choices)

# def test_get_choice(monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "12")
#
#     available_choices = list(range(1, 10))
#
#     with pytest.raises(ValueError):
#         get_choice(available_choices)


# @pytest.mark.parametrize("user_input", ("abc", "12"))
# def test_get_choices_invalid_input(monkeypatch, user_input, available_choices):
#     monkeypatch.setattr("builtins.input", lambda *args, **kwargs: user_input)
#
#     with pytest.raises(ValueError):
#         get_choice(available_choices)
#
#
# def test_get_choices_valid_input(monkeypatch, available_choices):
#     monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "2")
#
#     choice = get_choice(available_choices)
#     assert choice == 2

@pytest.mark.parametrize(("user_input", "exception_type"), (
    ("2", None),
    ("abc", ValueError),
    ("12", ValueError),
))
def test_get_choices(monkeypatch, available_choices, user_input, exception_type):
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: user_input)

    if exception_type:
        with pytest.raises(exception_type):
            get_choice(available_choices)
    else:
        choice = get_choice(available_choices)
        # assert choice == int(user_input)
        assert type(choice) == int
        assert str(choice) == user_input
