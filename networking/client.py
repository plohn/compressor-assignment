import socket
import sys
import bitarray
import socket
from hashlib import sha256
import base64
import pickle
import math
import random

sys.path.insert(0, '../Lempel-78')
sys.path.insert(0, '../Encoding')

import compress
import encoder


class Compressor_client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_requested_file(self, file, x_present_errors):
        bits_to_flip: int = []
        already_fliped_bits: int = []
        compressed_file: bytearray = bytearray()
        encoded_file: bitarray = bitarray.bitarray()
        data_to_send: dict = dict()

        # compress file.
        try:
            with open(file, "rb") as to_compress:
                compressed_file = compress.compress_file(to_compress.read()) 
            
        except Exception as e:
            print(e)
            return

        # encode file
        encoded_file = encoder.get_encoded_information(compressed_file)
        bits_to_flip = math.ceil((x_present_errors/len(encoded_file)) * 100)
        # Flip the bits to represent network error
        for flip in range(bits_to_flip):
            bit_to_flip = random.randint(0, len(encoded_file))
            while True:
                if bit_to_flip not in already_fliped_bits:
                    break
                bit_to_flip = random.randint(0, len(encoded_file))
    
            already_fliped_bits.append(bit_to_flip)
            encoded_file[bit_to_flip] = not encoded_file[bit_to_flip]
            
        sha256_rep = sha256()
        sha256_rep.update(encoded_file)
        # The JSON to send
        data_to_send = {
            'encoded_message': bytearray(encoded_file),
            'compression_algorithm': 'Lampel-78',
            'encoding': 'Orthogonal',
            'parameters': [],
            'errors': base64.b64encode(bits_to_flip.to_bytes(4)),
            'sha256': sha256_rep.digest()
        }

        # Send file over the network
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.sendall(pickle.dumps(data_to_send))

        except Exception as e:
            print(e)

input_file   = str(input("File to transfer: "))
input_errors = int(input("Errors to be inserted: "))

client: Compressor_client = Compressor_client("127.0.0.1", 64632)
client.send_requested_file(input_file, input_errors)
