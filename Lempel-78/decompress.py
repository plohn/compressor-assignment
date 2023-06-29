"""
   This function decompress a compressed message.
   @param src The LZ78 based compressed message.
   @return A string that represent the decompressed message.
"""
def decompress(src: dict) -> str:
    comp_tmp:dict   = src # do not change the data of the original dictionary
    dcomp:bytearray = bytearray() # The decoded message.
    next_dcomp:int  = int()
    next_ref:int    = int() # The reference that the next compressed entry hold to an entry back. 
    tmp_bytes:int = []

    if (len(comp_tmp) > 0):
        for index in range(1, len(comp_tmp) + 1):
            if (comp_tmp[index][0] == 0):
                dcomp.append(comp_tmp[index][1]) # add the character.
            else:
                next_ref           = comp_tmp[index][0]
                next_dcomp         = comp_tmp[next_ref][1]
                tmp_bytes.append(next_dcomp)
                tmp_bytes.append(comp_tmp[index][1])
                comp_tmp[index][1] = tmp_bytes
                dcomp.extend(tmp_bytes);
                tmp_bytes.clear()
    else:
        raise Exception("Empty dictionary")

    dcomp.pop()
    return dcomp

def build_dict(src: bytearray) -> dict:
    tmp_dict: dict  = dict() # The dictionary to build.
    curr_index: int = 1 # current index in the dictionary.
    curr_entry: int = int() # The current found entry.
    last_byte: int  = 0

    for byte in range(1, len(src) - 1, 2):
        tmp_dict[curr_index] = [src[byte - 1], src[byte]]
        curr_index += 1
        last_byte = byte

    if ((len(src) - 1) % 2 == 1):
        tmp_dict[curr_index] = [src[last_byte + 1], src[last_byte + 2]]

    return tmp_dict


builded_dict = {}
with open("output", "rb") as input:
    
    builded_dict = build_dict(input.read())
    print(decompress(builded_dict))

#with open("output2.out", "wb") as output:
    #output.write(decompress(builded_dict))
