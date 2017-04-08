#!/usr/bin/env python2
# coding: utf-8

import sys
import getpass
import socket
from struct import pack, unpack

try:
    input = raw_input
except NameError:
    pass

DEFAULT_PORT = 25575

class MinecraftClient():

    def __init__(self, host, port=DEFAULT_PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(True)
        self.socket.connect((host, port))

    def disconnect(self):
        if self.socket:
            self.socket.close()

    def authenticate(self, password):
        self.send_request(3, password)
        self.read_response()

    def command(self, command):
        self.send_request(2, command)
        return self.read_response()

    def send_request(self, type_command, data):
        size = 4 * 2 + len(data) + 2
        self.socket.send(pack('<Iii%isxx' % len(data), size, 42, type_command, data))

    def read_response(self):
        data = self.socket.recv(4)
        response_size, = unpack('<I', data)
        response = self.socket.recv(response_size)
        command_size = response_size - (4 * 2 + 2)
        if command_size == 0:
            rc_id, type_resp = unpack('<iixx', response)
        else:
            rc_id, type_resp, data = unpack('<ii%isxx' % command_size, response)

        if rc_id != 42:
            raise Exception("Error")

        return data

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.disconnect()

if __name__ == "__main__" :
    args = sys.argv[1:]

    if len(args) == 0:
        sys.exit(1)
    host = args[0]

    port = DEFAULT_PORT
    if len(args) > 1:
        port = int(args[1])

    with MinecraftClient(host, port) as c:
        c.authenticate(getpass.getpass())
        while 1:
            line = input(">> ")
            if line == 'quit':
                break
            print(c.command(line))
