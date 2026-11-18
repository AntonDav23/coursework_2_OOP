from unittest.mock import patch

from main import main


def test_main_empty_country():
    """Проверяет обработку пустого названия старны."""
    with patch("builtins.input", return_value=""):
        with patch("builtins.print") as mock_print:
            main()
        mock_print.assert_called_once_with("Название страны не может быть пустым.")


def test_main_connection_error():
    """Проверяет обработку ошибки подключения."""
    with patch("builtins.input", side_effect=["Russia", "5"]):
        with patch("main.NominatimAPI") as mock_api:
            mock_api.return_value.get_data.side_effect = ConnectionError("Ошибка подкючения к Nominatim API")

            with patch("builtins.print") as mock_print:
                main()
    mock_print.assert_called_once_with("Ошибка подключения: Ошибка подкючения к Nominatim API")


def test_main_country_not_found():
    """Проверяет обработку ситуации, когда страна не найдена."""
    with patch("builtins.input", side_effect=["UnknownCountry", "5"]):
        with patch("main.NominatimAPI") as mock_api:
            mock_api.return_value.get_data.side_effect = ValueError("Страна не найдена")

            with patch("builtins.print") as mock_print:
                main()

    mock_print.assert_called_once_with("Ошибка обработки данных: Страна не найдена")


def test_main_success():
    """Проверяет успешное выполнение main()."""
    with patch("builtins.input", side_effect=["Russia", "5", "Russia"]):
        with patch("main.NominatimAPI") as mock_nominatim:
            mock_nominatim.return_value.get_data.return_value = ["1", "2"]

            with patch("main.OpenSkyAPI") as mock_opensky:
                mock_opensky.return_value.get_data.return_value = {"states": []}

                with patch("main.JsonSaver.save"):
                    with patch("builtins.print") as mock_print:
                        main()

    assert mock_print.call_count == 5
