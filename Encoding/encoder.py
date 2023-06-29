import bitarray


def is_parity_even(byte: bitarray):
    if (byte.count(1) % 2 == 0):
        return True
    else:
        return False

def ecc_build_row_parity_bits(data: bytearray) -> bitarray:
    row_parity: bitarray = bitarray.bitarray(endian = 'big')
    tmp: bitarray = bitarray.bitarray(endian = 'big')
    
    for byte in data:
        tmp.frombytes(byte.to_bytes(1))
        
        if (is_parity_even(tmp)):
            tmp.append(0)
        else:
            tmp.append(1)
        row_parity.extend(tmp)
        tmp.clear()
    return row_parity

def ecc_build_col_parity_bits(data: bytearray) -> bitarray:
    col_parity: bitarray = bitarray.bitarray(endian = 'big')
    tmp: bitarray = bitarray.bitarray(endian = 'big')
    curr_col: bitarray = bitarray.bitarray(endian = 'big')
    tmp.frombytes(data)
    total_bits:int = tmp.count(0) + tmp.count(1)
    col_bits_step:int = int(total_bits / 8)

    for curr_bit in range(8):
        for step in range(col_bits_step):
            curr_col.append(tmp[curr_bit + (step * 8)])
        if (is_parity_even(curr_col)):
            col_parity.append(0)
        else:
            col_parity.append(1)
        curr_col.clear() 
    return col_parity

def get_encoded_information(msg: bytearray) -> bitarray:
    encoded_msg: bitarray = ecc_build_row_parity_bits(msg)
    col_bits: bitarray    = ecc_build_col_parity_bits(msg)
    total_col_bits: int = col_bits.count(1) + col_bits.count(0)
    for col_bit in range(total_col_bits):
        encoded_msg.append(col_bits[col_bit])
    return encoded_msg


