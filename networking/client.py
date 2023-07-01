import socket
import sys

sys.path.insert(0, '../Lempel-78')
sys.path.insert(0, '../Encoding')

import compress
import encoder


class Compressor_client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_requested_file(self, file):
        with open(file, "rb"):
            pass






