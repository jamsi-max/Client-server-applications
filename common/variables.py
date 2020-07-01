import time


MAX_COUNT_CONNECTIONS = 5
MAX_SIZE_RECEIVE_DATA = 4096
DEFAULT_ENCODING = 'utf-8'

# Response server
RESPONSE_LIST = {
    'presence': {
        'status': 200,
        'alert': 'OK'
        },
    'msg': {
        'status': 200,
        'alert': 'Message received'
        },
    'quit': {
        'status': 200,
        'alert': 'By-by'
        },
    'no_action': {
        'status': 400,
        'error': 'Bad request'
        }
}
# Request client
ACTION = [
    {
        'action': 'presence',
        'time': time.ctime(),
        'user': {
            'username': 'Guest'
            }
    },
    {
        'action': 'msg',
        'time': time.ctime(),
        'msg': 'Hello!',
        'user': {
            'username': 'Guest'
            }
    },
    {
        'action': 'quit',
        'time': time.ctime(),
        'user': {
            'username': 'Guest'
            }
    }
]
