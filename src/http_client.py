import socket
from src.models import HTTPResponse, HTTPRequest
from src.logger import logger


def send_request(request: HTTPRequest, host: str, port: int) -> HTTPResponse:
    """
    Отправляет HTTP запрос на сервер и получает HTTP ответ

    :param request: HTTP запрос
    :param host: ip сервера
    :param port: порт сервера
    :return: HTTP ответ
    """

    try:
        with socket.create_connection((host, port)) as sock:
            sock.sendall(request.to_bytes())
            response_data = sock.recv(4096)

        logger.info("HTTP response received")
        return HTTPResponse.from_bytes(response_data)

    except Exception as e:
        logger.error(f"Error sending request: {e}")
        return HTTPResponse(
            status_code=500,
            status_message="Internal server error",
            headers={},
            body='{"error": "Internal server error"}'
        )
