"""
   This function decompress a compressed message.
   @param src The LZ78 based compressed message.
   @return A string that represent the decompressed message.
"""
def decompress(src: dict) -> str:
    comp_tmp:dict  = src # do not change the data of the original dictionary
    dcomp:str      = str() # The decoded message.
    next_dcomp:str = str()
    next_ref:str   = str() # The reference that the next compressed entry hold to an entry back. 

    if (len(comp_tmp) > 0):
        for index in range(1, len(comp_tmp) + 1):
            if (comp_tmp[index][0] == 0):
                dcomp += comp_tmp[index][1] # add the character.
            else:
                next_ref           = comp_tmp[index][0]
                next_dcomp         = comp_tmp[next_ref][1]
                comp_tmp[index][1] = next_dcomp + comp_tmp[index][1] # update the entry, which had a reference, to it's decompressed version.
                dcomp             += comp_tmp[index][1]
    else:
        raise Exception("Empty dictionary")

    return dcomp

def build_dict(src: str) -> dict:
    tmp_dict: dict  = dict() # The dictionary to build.
    curr_index: int = 0 # current index in the dictionary.
    curr_entry: str = str() # The current found entry.
    curr_ref: str   = str() # current reference.
    was_ref: bool   = True # check if the previous character was reference.

    for byte in src:
        if (ord(byte) >= 48 and ord(byte) <= 57):
            if (was_ref == 0):
                tmp_dict[curr_index] = [int(curr_ref), curr_entry]
                curr_ref = str()
                curr_entry = str()
                curr_index += 1
            curr_ref += byte
            was_ref = True
        else:
            was_ref = 0
            curr_entry += byte
    if (len(curr_ref) > 0 and len(curr_entry) == 0):
        tmp_dict[curr_index] = [int(curr_ref), ""]
    else:
        tmp_dict[curr_index] = [int(curr_ref), curr_entry]

    return tmp_dict
    



# remove the lines below - test only - gianni, I just let it here so you can also verify the algorithm, if you want to.
# compressed messege reference: https://archive.ph/20130107200800/http://oldwww.rasip.fer.hr/research/compress/algorithms/fund/lz/lz78.html

"""
characters = {
    1: [0, "A"],
    2: [0, "B"],
    3: [2, "C"],
    4: [3, "A"],
    5: [2, "A"]
}

test_init_seq = "ABBCBCABA"
comp: str = str()
for i in range(1, len(characters) + 1):
    comp += characters[i][1]

print("Init sequence: ", test_init_seq)
print("Compressed:    ", comp)
print("Decompressed:  ", decompress(characters))
"""

print("0A0B4C3C6A3S0D8D8K0S2")
print(build_dict("0A0B4C3C6A3S0D8D8K0S2"))

