import sys
import socket
import json
import time


def client_run(addr, port=7777):
    client_socket = socket.socket()
    msg = {
        'action': 'presence',
        'time': time.ctime(time.time())
        }
    client_socket.connect((addr, port))
    client_socket.send(json.dumps(msg).encode('utf-8'))

    data = client_socket.recv(1024)
    data = json.loads(data.decode('utf-8'))
    client_socket.close()

    if data.get('response') == 200:
        print(data['alert'])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Arguments are not specified correctly!')
    
    if len(sys.argv) == 3:
        client_run(addr = sys.argv[1], port = sys.argv[2])

    if len(sys.argv) == 2:
        client_run(addr = sys.argv[1])