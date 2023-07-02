import bitarray

def is_parity_even(byte: bitarray):
    if (byte.count(1) % 2 == 0):
        return True
    else:
        return False

def retrieve_col_parity_bits(data: bitarray) -> bitarray:
    total_bits: int = data.count(0) + data.count(1)
    # Get the last 9 bits, 8 parity bits and 1 parity bit of the col parity bits.
    return bitarray.bitarray(data[total_bits - 9 : ])

def get_column(index: int, data: bitarray) -> bitarray:
    tmp: bitarray = data[index: ]
    total_bits: int = data.count(0) + data.count(1)
    groups: int = int(total_bits / 9) # parity bit is on the calculation.
    col: bitarray = bitarray.bitarray(endian='big')
    for curr in range(groups - 1):
        col.append(tmp[curr * 9])
    return col

def perform_ecc(row_bits: bitarray, parity_col: bitarray, data: bitarray) -> bitarray:
    fixed: bitarray = bitarray.bitarray(endian='big')
    tmp: bitarray = bitarray.bitarray(endian='big')
    tmp_col: bitarray = bitarray.bitarray(endian='big')
    for row in range(8):
        tmp.append(row_bits[row])
        tmp.append(parity_col[row])
        if (not is_parity_even(tmp) and not is_parity_even(get_column(row, data))):
            # if not even, then here is the error
            # perform the error correction by inverting in the row, whitch was fliped
            row_bits[row] = not row_bits[row]

        tmp.clear()
        fixed.append(row_bits[row])
    return fixed

def decode_information(src: bytearray) -> bitarray:
    data: bitarray = bitarray.bitarray()
    data.frombytes(src)
    col_parity_bits: bitarray = retrieve_col_parity_bits(data)
    curr_row: bitarray = bitarray.bitarray(endian='big')
    total_bits: int = data.count(0) + data.count(1) 
    decoded: bitarray = bitarray.bitarray(endian='big')
    # total_bits - 9, because we do not want to calculate column bits.
    total_bits -= 9

    for row_start in range(1, total_bits, 9):
        curr_row = data[row_start - 1 : row_start + 8] # Get the current row, including parity bit.
        if (not is_parity_even(curr_row)):
            curr_row = perform_ecc(curr_row, col_parity_bits, data)
        for bit in range(8):
            decoded.append(curr_row[bit])
    return decoded
