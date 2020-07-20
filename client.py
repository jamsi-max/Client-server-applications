import threading
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
    )

from common.variables import (
    DEFAULT_PORT,
    DEFAULT_ADDR,
    DEFAULT_ENCODING,
    MAX_SIZE_RECEIVE_DATA
    )
from common.utils import (
    args_validation
    )

from common.decorators import LogInfo

event = threading.Event()


@LogInfo('full')
def client(addr=DEFAULT_ADDR, port=DEFAULT_PORT):
    nickname = input('Input your nickname: ')

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(args_validation(addr, port))

    send_message_thread = threading.Thread(
        target=send_message,
        args=(nickname, client_socket),
        daemon=True
        )
    receive_thread = threading.Thread(
        target=receive,
        args=(nickname, client_socket),
        daemon=True
        )

    receive_thread.start()
    send_message_thread.start()

    receive_thread.join()
    send_message_thread.join()


@LogInfo('full')
def receive(nickname, client_socket):
    while True:
        try:
            message = client_socket.recv(MAX_SIZE_RECEIVE_DATA).decode(DEFAULT_ENCODING)
            if message == 'GET_NICK':
                client_socket.send(nickname.encode(DEFAULT_ENCODING))
            else:
                print(message)
                event.set()
                # event.clear()
        except Exception:
            print('An error occured!')
            client_socket.close()
            break


@LogInfo('full')
def send_message(nickname, client_socket):
    event.wait()
    while True:
        # event.wait()
        # message = f'{nickname}: {input(nickname+": ")}'
        # message = f'{nickname}: {input()}'
        message = f'{input()}'
        client_socket.send(message.encode(DEFAULT_ENCODING))


if __name__ == '__main__':
    client()
