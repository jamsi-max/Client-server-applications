import sys

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
        if len(addr.split('.')) != 4 and addr != 'localhost':
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
