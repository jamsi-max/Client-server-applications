import sys
import json
from random import randint
import socket

from common.variables import (
    DEFAULT_ENCODING,
    RESPONSE_LIST,
    MAX_SIZE_RECEIVE_DATA,
    HEADER_LENGHT
    )
from common.decorators import LogInfo


class PortError(Exception):
    pass


class AddrError(Exception):
    pass


@LogInfo('full')
def args_validation(addr, port):
    '''
    Validation of data entered by the user

    return tuple(addr: str, port: int)
    '''
    try:
        if port < 1024 or port > 65535:
            raise PortError
        if not addr:
            raise AttributeError
        if addr == 'localhost':
            return (addr, port)
        if len([int(_) for _ in addr.split('.')]) != 4 and addr != 'localhost':
            raise AddrError
        return (addr, port)
    except PortError:
        sys.exit(1)
    except ValueError:
        sys.exit(1)
    except AddrError:
        sys.exit(1)
    except AttributeError:
        sys.exit(1)


@LogInfo('full')
def get_request(request):
    '''
    The function gets JSON data as bytes and returns a Python object

    return data: dict
    '''
    if isinstance(request, bytes):
        try:
            data = request.decode(DEFAULT_ENCODING)
            data = json.loads(data)
        except json.JSONDecodeError:
            sys.exit(1)
        if isinstance(data, dict):
            return data
    raise ValueError


@LogInfo()
def generate_response(request_data):
    '''
    The function receives a query in the form of a dictionary and
    returns a response based on the query

    return json: str bytes
    '''
    if hasattr(request_data, 'get'):
        action = request_data.get('action', None)
        if action and request_data.get('user')['username'] == 'Guest':
            response = RESPONSE_LIST[action]
            return json.dumps(response, indent=4).encode(DEFAULT_ENCODING)
        return json.dumps(
            {'response': 400, 'error': 'Bad request'},
            indent=4).encode(DEFAULT_ENCODING)
    raise TypeError


@LogInfo()
def send_message(recv_socket, message):
    '''
    Function for sending messages to the server
    '''
    if not isinstance(message, bytes):
        raise TypeError
    recv_socket.send(message)


@LogInfo()
def generate_request(request_list):
    '''
    Function for preparing requests to the server

    return string: bytes
    '''
    if isinstance(request_list, list):
        request = request_list[randint(0, len(request_list)-1)]
        return json.dumps(request, indent=4).encode(DEFAULT_ENCODING)
    raise TypeError


@LogInfo()
def new_listen_socket(pool):
    '''
    Function create new socket

    return socket
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1)  # disable reloade timeout server
    sock.bind(pool)
    sock.listen()
    sock.settimeout(0.2)

    return sock


def read_request(client_read, client_all):
    '''
    '''
    response = {}

    for sock in client_read:
        try:
            data = sock.recv(MAX_SIZE_RECEIVE_DATA).decode(DEFAULT_ENCODING)
            response[sock.getpeername()] = data
        except Exception:
            print(f'Client {sock} disconnected')
            client_all.remove(sock)

    return response


def write_response(request, client_write, client_all):
    '''
    Function send message
    '''
    print(request)
    for sock in client_all:
        try:
            response = request[sock.getpeername()].encode(DEFAULT_ENCODING)
            sock.send(response)
        except Exception:
            print(f'Client {sock} disconnected')
            sock.close()
            client_all.remove(sock)


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)

        if not len(message_header):
            return False

        message_lenght = int(message_header.decode(DEFAULT_ENCODING).strip())
        return {
            'header': message_header,
            'data': client_socket.recv(message_lenght)
            }

    except Exception:
        return False