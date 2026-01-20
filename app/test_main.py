from app.main import get_human_age


def test_bottom_value_for_first_15_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_top_value_for_first_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_bottom_value_for_next_9_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_top_value_for_next_9_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_bottom_value_for_every_4_cat_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_top_value_for_every_4_cat_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_bottom_value_for_every_5_next_dog_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_top_value_for_every_5_next_dog_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
