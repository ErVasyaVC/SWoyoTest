from cli import cli
from models import HTTPRequest
from http_client import send_request
from config_loader import load_config
import base64
from logger import logger

def main():
    sender, receiver, message = cli()
    config = load_config("../config/config.toml")

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
        body=f'{{"sender": "{sender}", "recipient": "{receiver}", "message": "{message}"}}'

    )

    try:
        response = send_request(request, config['server']['host'], config['server']['port'])
        print(response.status_code, response.body)

        logger.info(f"Server response: {response.status_code} {response.status_message}\n{response.body}")
    except Exception as e:
        logger.error(f"Request failed: {e}")



if __name__ == '__main__':
    main()