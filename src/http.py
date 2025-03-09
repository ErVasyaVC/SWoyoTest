import socket
from models import HTTPResponse, HTTPRequest


def send_request(request: HTTPRequest, host: str, port: int) -> HTTPResponse:
    with socket.create_connection((host, port)) as sock:
        sock.sendall(request.to_bytes())
        response_data = sock.recv(4096)
    return HTTPResponse.from_bytes(response_data)