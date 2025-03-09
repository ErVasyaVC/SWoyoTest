import logging
from  config_loader import load_config

config = load_config("../config/config.toml")

logging.basicConfig(
    filename=config["logging"]["path"],
    level=config["logging"]["level"],
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)