class HTTPRequest:
    def __init__(self, method: str, path: str, headers: dict, body: str):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body


    def to_bytes(self) -> bytes:
        """
        Преобразует HTTP-запрос в последовательность байтов

        :return: Последовательность байтов
        """
        request_line = f"{self.method} {self.path} HTTP/1.1\r\n"
        for key, value in self.headers.items():
            request_line += f"{key}: {value}\r\n"
        request_line += f"Content-Length: {len(self.body)}\r\n"
        request_line += "\r\n"
        request_line += self.body
        return request_line.encode('utf-8')


    @classmethod
    def from_bytes(cls, binary_data: bytes) -> "HTTPRequest":
        """
        Преобразует последовательность байтов в объект HTTP-запроса.

        :param binary_data: Последовательность байтов
        :return: объект HTTP-запроса
        """
        data = binary_data.decode('utf-8')
        header_section, body = data.split("\r\n\r\n")
        lines = header_section.split("\r\n")
        method, path = lines[0].split(" ", 2)[:2]
        headers = dict()
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                if key != "Content-Length":
                    headers[key] = value
        return cls(method, path,  headers, body)


class HTTPResponse:
    def __init__(self, status_code: int, status_message: str, headers: dict, body: str):
        self.status_code = status_code
        self.status_message = status_message
        self.headers = headers
        self.body = body


    def to_bytes(self) -> bytes:
        """
        Преобразует HTTP-ответ в последовательность байтов

        :return: Последовательность байтов
        """
        request_line = f"HTTP/1.1 {self.status_code} {self.status_message}\r\n"
        for key, value in self.headers.items():
            request_line += f"{key}: {value}\r\n"
        request_line += "\r\n"
        request_line += self.body
        return request_line.encode('utf-8')


    @classmethod
    def from_bytes(cls, binary_data: bytes) -> "HTTPResponse":
        """
        Преобразует последовательность байтов в объект HTTP-ответа.

        :param binary_data: Последовательность байтов
        :return: объект HTTP-ответа
        """
        data = binary_data.decode('utf-8')
        header_section, body = data.split("\r\n\r\n")
        lines = header_section.split("\r\n")
        status_code, status_message = lines[0].split(" ", 2)[1:]
        headers = dict()
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key] = value
        return cls(int(status_code), status_message,  headers, body)
