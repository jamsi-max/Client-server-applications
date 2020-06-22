import socket
import sys
import json
import time


def run_server(arg_addr='-a', addr='', arg_port='-p', port=7777):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # отключаем таймаут переподключения
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((addr, port))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        request = request.decode('utf-8')
        data = json.loads(request)

        if data.get('action'):
            print(data.get('time', 'No data'))
            response = {
                'response': 200,
                'alert': 'The connection is established',
                'time': time.ctime(time.time())
                }
        client_socket.send(json.dumps(response).encode('utf-8'))
        client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_server()

    if '-a' in sys.argv and len(sys.argv) == 3:
        run_server(arg_addr=sys.argv[1], addr=sys.argv[2])

    if '-p' in sys.argv and len(sys.argv) == 3:
        run_server(arg_port=sys.argv[1], port=sys.argv[2])

    if '-a' in sys.argv and '-p' in sys.argv and len(sys.argv) == 5:
        run_server(arg_addr=sys.argv[1], addr=sys.argv[2], arg_port=sys.argv[1], port=sys.argv[2])
    
    if len(sys.argv) > 1:
        print('Arguments are not specified correctly!')
