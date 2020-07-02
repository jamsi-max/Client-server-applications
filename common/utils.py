import sys
import json
from random import randint

from common.variables import (
    DEFAULT_ENCODING,
    RESPONSE_LIST
    )


class PortError(Exception):
    pass


class AddrError(Exception):
    pass


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
        print('The port is out of range 1024...65535.\
        \nTry "server.py --help" for help')
        sys.exit(1)
    except ValueError:
        print('The IP address cannot contain "str".\
        \nTry "server.py --help" for help')
        sys.exit(1)
    except AddrError:
        print('Invalid ip address format.\nTry "server.py --help" for help')
        sys.exit(1)
    except AttributeError:
        print('The required "addr" attribute is missing.\
        \nTry "server.py --help" for help')
        sys.exit(1)


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
            print('Unknown message format!')
            sys.exit(1)
        if isinstance(data, dict):
            return data
    raise ValueError


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


def send_message(recv_socket, message):
    '''
    Function for sending messages to the server
    '''
    if not isinstance(message, bytes):
        raise TypeError
    recv_socket.send(message)


def generate_request(request_list):
    '''
    Function for preparing requests to the server

    return string: bytes
    '''
    if isinstance(request_list, list):
        request = request_list[randint(0, len(request_list)-1)]
        return json.dumps(request, indent=4).encode(DEFAULT_ENCODING)
    raise TypeError
