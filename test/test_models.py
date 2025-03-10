from src.models import HTTPRequest, HTTPResponse


def test_http_request_to_bytes():
    request = HTTPRequest(
        method="POST",
        path="/send_sms",
        headers={"Content-Type": "application/json"},
        body='{"message": "Test"}'
    )

    assert request.to_bytes() == (
        b'POST /send_sms HTTP/1.1\r\n'
        b'Content-Type: application/json\r\n'
        b'Content-Length: 19\r\n\r\n'
        b'{"message": "Test"}'
    )


def test_http_request_from_bytes():
    request_bytes = (
        b'POST /send_sms HTTP/1.1\r\n'
        b'Content-Type: application/json\r\n'
        b'Content-Length: 19\r\n\r\n'
        b'{"message": "Test"}'
    )

    request = HTTPRequest.from_bytes(request_bytes)
    assert request.method == "POST"
    assert request.path == "/send_sms"
    assert request.headers == {"Content-Type": "application/json"}
    assert request.body == '{"message": "Test"}'


def test_http_response_to_bytes():
    response = HTTPResponse(
        status_code=200,
        status_message="OK",
        headers={"Content-Type": "application/json"},
        body='{"status": "success"}'
    )

    assert response.to_bytes() == (
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: application/json\r\n\r\n'
        b'{"status": "success"}'
    )


def test_http_response_from_bytes():
    response_bytes = (
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: application/json\r\n\r\n'
        b'{"status": "success"}'
    )
    response = HTTPResponse.from_bytes(response_bytes)
    assert response.status_code == 200
    assert response.status_message == "OK"
    assert response.headers == {"Content-Type": "application/json"}
    assert response.body == '{"status": "success"}'