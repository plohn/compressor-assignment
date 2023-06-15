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

# remove the lines below - test only - gianni, I just let it here so you can also verify the algorithm, if you want to.
# compressed messege reference: https://archive.ph/20130107200800/http://oldwww.rasip.fer.hr/research/compress/algorithms/fund/lz/lz78.html
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

