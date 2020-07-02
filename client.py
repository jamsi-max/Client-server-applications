import socket
import click

from common.variables import (
    MAX_SIZE_RECEIVE_DATA,
    DEFAULT_PORT,
    ACTION
    )
from common.utils import (
    args_validation,
    get_request,
    generate_request
    )
from settings.client_log_config import logger


@click.command()
@click.option(
    "-a",
    "--addr",
    type=str,
    help="Server address to connect")
@click.option(
    "-p",
    "--port",
    default=DEFAULT_PORT,
    help="Port number for connecting to the server")
def client_run(addr, port):
    clear_addr, clear_port = args_validation(addr, port)

    client_socket = socket.socket()
    request = generate_request(ACTION)

    client_socket.connect((clear_addr, clear_port))
    client_socket.send(request)

    data = client_socket.recv(MAX_SIZE_RECEIVE_DATA)
    request_data = get_request(data)
    # print(request_data)
    logger.debug(request_data)
    client_socket.close()


if __name__ == '__main__':
    client_run()
