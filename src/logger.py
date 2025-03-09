import logging

# Настройка логирования
logging.basicConfig(
    filename="../log/app.log",  # Лог-файл
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, ERROR и т. д.)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщения
)

logger = logging.getLogger(__name__)