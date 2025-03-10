from src.config_loader import load_config
import tempfile


def test_load_config():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".toml", delete=False) as tmp_file:
        tmp_file.write("""
        [server]
        host = "localhost"
        port = 4010

        [auth]
        username = "your_username"
        password = "your_password"

        [logging]
        level = "INFO"
        path = "../log/app.log"
        """)
        tmp_file_path = tmp_file.name


    config = load_config(tmp_file_path)


    assert config["server"]["host"] == "localhost"
    assert config["server"]["port"] == 4010
    assert config["auth"]["username"] == "your_username"
    assert config["auth"]["password"] == "your_password"
    assert config["logging"]["level"] == "INFO"
    assert config["logging"]["path"] == "../log/app.log"
