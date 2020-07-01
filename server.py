import json
import socket
import click

from common.variables import (
    MAX_COUNT_CONNECTIONS,
    MAX_SIZE_RECEIVE_DATA,
    DEFAULT_PORT
    )
from common.utils import (
    args_validation,
    get_request,
    generate_response,
    send_message
    )


@click.command()
@click.option(
    "-a",
    "--addr",
    default='localhost',
    help="Server network address")
@click.option(
    "-p",
    "--port",
    default=DEFAULT_PORT,
    help="The port number of the server")
def run_server(addr, port):
    clear_addr, clear_port = args_validation(addr, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        True)  # disable timeout server
    server_socket.bind((clear_addr, clear_port))
    server_socket.listen(MAX_COUNT_CONNECTIONS)

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(MAX_SIZE_RECEIVE_DATA)
        try:
            request_data = get_request(request)
            print(request_data)

            response = generate_response(request_data)
            send_message(client_socket, response)
            client_socket.close()
        except ValueError:
            print('Unknown message format!')
            client_socket.close()


if __name__ == '__main__':
    run_server()
