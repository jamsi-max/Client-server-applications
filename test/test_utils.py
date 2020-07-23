import unittest
import sys
import os

sys.path.append(os.getcwd())
from common.utils import (
    args_validation,
    get_request,
    generate_response,
    send_message,
    generate_request
    )
from common.variables import DEFAULT_ENCODING


class TestArgsValidation(unittest.TestCase):
    def test_args_validation_raises_port_error(self):
        with self.assertRaises(SystemExit):
            args_validation('0.0.0.0', 123)

    def test_args_validation_raises_attribute_error(self):
        with self.assertRaises(SystemExit):
            args_validation('1.2', 1234)

    def test_args_validation_localhost_ok(self):
        result = args_validation('localhost', 1234)
        self.assertEqual(result, ('localhost', 1234))

    def test_args_validation_return_type_tuple(self):
        result = args_validation('127.0.0.1', 1234)
        self.assertIsInstance(result, tuple)

    def test_args_validation_ok(self):
        result = args_validation('127.0.0.1', 1234)
        self.assertEqual(result, ('127.0.0.1', 1234))


class TestRunServer(unittest.TestCase):
    def test_get_request_raises_type_error(self):
        with self.assertRaises(ValueError):
            get_request('')

    def test_get_request_raises_json_decode_error(self):
        with self.assertRaises(SystemExit):
            get_request('abc'.encode(DEFAULT_ENCODING))

    def test_get_request_return_type_dict(self):
        result = get_request('{"test": "test"}'.encode(DEFAULT_ENCODING))
        self.assertIsInstance(result, dict)

    def test_get_request_ok(self):
        result = get_request('{"test": "test"}'.encode(DEFAULT_ENCODING))
        self.assertEqual(result, {"test": "test"})


class TestSendMessage(unittest.TestCase):
    def test_send_message_raises_type_error(self):
        with self.assertRaises(TypeError):
            send_message(1, '')


class TestGenerateRequest(unittest.TestCase):
    def test_generate_request_return_str_bytes(self):
        result = generate_request([{'test': 'test'}])
        self.assertIsInstance(result, bytes)

    def test_generate_request_raise_type_error(self):
        with self.assertRaises(TypeError):
            generate_request('abc')


class TestGenerateResponse(unittest.TestCase):
    def test_generate_response_raise_type_error(self):
        with self.assertRaises(TypeError):
            generate_response('abc')

    def test_generate_response_return_str_bytes(self):
        result = generate_response({'test': 'test'})
        self.assertIsInstance(result, bytes)


if __name__ == '__main__':
    unittest.main()
