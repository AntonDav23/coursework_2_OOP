import pytest

from src.base_saver import BaseSaver


def test_base_saver_is_abstract():
    """Проверяем, что BaseSaver нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseSaver()
