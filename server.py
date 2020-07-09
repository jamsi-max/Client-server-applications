import click
import select

from common.variables import (
    DEFAULT_PORT,
    WAITE_SELECT,
    HEADER_LENGHT,
    DEFAULT_ENCODING
    )
from common.utils import (
    args_validation,
    new_listen_socket,
    read_request,
    write_response,
    receive_message
    )
# from common.decorators import LogInfo


# @LogInfo('full')
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
    socket_pool = args_validation(addr, port)

    server_socket = new_listen_socket(socket_pool)

    socket_list = [server_socket]
    clients = {}

    while True:
        read_socket, _, exception_sockets = select.select(
            socket_list,
            [],
            socket_list
            )

        for sock in read_socket:
            if sock == server_socket:
                client_socket, client_addr = server_socket.accept()

                user = receive_message(client_socket)
                if user is False:
                    continue

                socket_list.append(client_socket)

                clients[client_socket] = user

                print(f'Accepted new connection fron\
{client_addr[0]}:{client_addr[1]} username:\
{user["data"].decode(DEFAULT_ENCODING)}')

            else:
                message = receive_message(sock)

                if message is False:
                    print('Closed connection from {clients[sock]["data"].decode(DEFAULT_ENCODING)}')
                    socket_list.remove(sock)
                    del clients[sock]
                    continue

                user = clients[sock]
                print(f'Received message from {user["data"].decode(DEFAULT_ENCODING)}: {message["data"].decode(DEFAULT_ENCODING)}')

                for client_socket in clients:
                    if client_socket != sock:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])


        for sock in exception_sockets:
            socket_list.remove(sock)
            del clients[sock]


        # try:
        #     client_socket, addr = server_socket.accept()
        # except OSError:
        #     pass
        # else:
        #     print(f'Received the connection request from {addr}')
        #     clients.append(client_socket)
        # finally:
        #     r = []
        #     w = []
        #     try:
        #         r, w, e = select.select(clients, clients, [], WAITE_SELECT)
        #     except Exception:
        #         pass

        #     request = read_request(r, clients)
        #     if request:
        #         write_response(request, w, clients)


if __name__ == '__main__':
    run_server()
