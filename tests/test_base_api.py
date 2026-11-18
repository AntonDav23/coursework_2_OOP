import pytest

from src.base_api import BaseAPI


def test_base_api_is_abstract():
    """Проверяем, что BaseAPI нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseAPI()
