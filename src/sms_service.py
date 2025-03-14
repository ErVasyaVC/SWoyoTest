import json
from src.cli import cli
from src.models import HTTPRequest
from src.http_client import send_request
import base64
from src.logger import logger, config

def main():
    """
    Основная функция программы. Загружает конфигурацию, обрабатывает аргументы
    командной строки, формирует HTTP-запрос и отправляет его на сервер.
    """
    sender, receiver, message = cli()

    logger.info(f"Starting SMS sending: {sender} -> {receiver}, message: {message}")

    credentials = f"{config['auth']['username']}:{config['auth']['password']}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    request = HTTPRequest(
        method="POST",
        path="/send_sms",
        headers={"Host": config['server']['host'],
            "Content-Type": "application/json",
            "Authorization": f"Basic {encoded_credentials}"
                 },
        body=json.dumps(
            {"sender": sender, "recipient": receiver, "message": message},
            ensure_ascii=False
        )
    )

    try:
        response = send_request(request, config['server']['host'], config['server']['port'])
        print(response.status_code, response.body)

        logger.info(f"Server response: {response.status_code} {response.status_message}\n{response.body}")
    except Exception as e:
        logger.error(f"Request failed: {e}")



if __name__ == '__main__':
    main()