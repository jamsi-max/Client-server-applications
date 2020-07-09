import socket
import click
import sys
import errno

from common.variables import (
    MAX_SIZE_RECEIVE_DATA,
    DEFAULT_PORT,
    DEFAULT_ADDR,
    DEFAULT_ENCODING,
    HEADER_LENGHT
    )
# from common.utils import (
#     args_validation,
#     # get_request,
#     # generate_request
#     )
# from common.decorators import LogInfo


# @LogInfo('full')
@click.command()
@click.option(
    "-a",
    "--addr",
    type=str,
    default=DEFAULT_ADDR,
    help="Server address to connect")
@click.option(
    "-p",
    "--port",
    default=DEFAULT_PORT,
    help="Port number for connecting to the server")
def client_run(addr, port):
    my_username = input('Username: ')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((addr, port))
        sock.setblocking(False)

        username = my_username.encode(DEFAULT_ENCODING)
        username_header = f'{len(username):<{HEADER_LENGHT}}'.encode(DEFAULT_ENCODING)
        sock.send(username_header + username)

        while True:
            message = input(f'{my_username}: ')

            if message:
                message = message.encode(DEFAULT_ENCODING)
                message_header = f'{len(message):<{HEADER_LENGHT}}'.encode(DEFAULT_ENCODING)
                sock.send(message_header+message)

            try:
                while True:
                    username_header = sock.recv(MAX_SIZE_RECEIVE_DATA)
                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit(1)
                    username_lenght = int(username_header.decode(DEFAULT_ENCODING).strip())
                    username = sock.recv(username_lenght).decode(DEFAULT_ENCODING)

                    message_header = sock.recv(HEADER_LENGHT)
                    message_lenght = int(message_header.decode(DEFAULT_ENCODING).strip())
                    message = sock.recv(message_lenght).decode(DEFAULT_ENCODING)

                    print(f'{username}: {message}')

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Error: ', str(e))
                    sys.exit(1)
                continue

            except Exception as e:
                print('Error', str(e))
                sys.exit(1)
                pass


        # while True:
        #     msg = sock.recv(MAX_SIZE_RECEIVE_DATA).decode(DEFAULT_ENCODING)
        #     print(msg)
        #     msg = input('Enter your massege: ')
        #     if msg == 'q' or not len(msg):
        #         break
        #     sock.send(msg.encode(DEFAULT_ENCODING))
        #     response = sock.recv(
        #         MAX_SIZE_RECEIVE_DATA
        #         ).decode(DEFAULT_ENCODING)
        #     print(f'Response: {response}')


if __name__ == '__main__':
    client_run()
