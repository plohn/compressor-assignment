import socket
import sys
import bitarray
import pickle
import base64
import math

sys.path.insert(0, '../Lempel-78')
sys.path.insert(0, '../Encoding')

import decompress
import decoder

def recvall(sock):
    BUFF_SIZE = 1024
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            break
    return data

class Compressor_Server():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def recieve_requested_file(self):
        transfered_data: bytearray = bytearray()
        recieved_data: dict = dict()
        decoded_data: bitarray = bitarray.bitarray()
        decompressed_data: bytearray = bytearray()
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((self.host, self.port))  
            except Exception as e:
                print(e)
                
            while True:
                sock.listen()
                conn, addr = sock.accept()
                try:
                    with conn:
                        transfered_data = recvall(conn)
                except Exception as e:
                    raise e
                    return
            
                recieved_data = pickle.loads(transfered_data)
                print("Used compression algorithm is: ", recieved_data['compression_algorithm'])
                print("Used encoding is: " + recieved_data['encoding'])
                print("Used parameters: " + str(recieved_data['parameters']))
                print("Errors: " + str(int.from_bytes(base64.b64decode(recieved_data['errors']))))
                print("SHA256: " + str(recieved_data['sha256'].hex()))
            
                # decode Transferred data.
                decoded_data = decoder.decode_information(recieved_data['encoded_message'])
                try:
                    # decompress the transfered data
                    decompressed_data = decompress.get_decompress(bytearray(decoded_data))
                    print("Transferred data: " + str(decompressed_data))
                except:
                    print("Can't decompress the transferred data due to high number of errors")

server: Compressor_Server = Compressor_Server('127.0.0.1', 64632)
server.recieve_requested_file()