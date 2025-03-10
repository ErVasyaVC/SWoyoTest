import logging
from pathlib import Path
from  src.config_loader import load_config

"""Модуль логирования"""

base_dir = Path(__file__).resolve().parent.parent
config_path = base_dir / "config" / "config.toml"
config = load_config(str(config_path))

log_path = base_dir / config["logging"]["path"]

logging.basicConfig(
    filename=log_path,
    level=config["logging"]["level"],
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)