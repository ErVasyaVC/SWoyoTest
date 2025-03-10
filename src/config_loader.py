import tomllib


def load_config(config_path: str) -> dict:
    """
    Функция загружает конфигурацию из TOML-файл и возвращает данные в виде словаря.

    :param config_path: Файл конфигурации
    :return: словарь с данными конфигурации
    """
    with open(config_path, 'rb') as f:
        return tomllib.load(f)