
def compress(file: bytearray) -> dict:
    dictionary:dict  = dict()
    encoded:dict     = dict()
    entry:int        = []
    index:int        = 1
    file.append(1)
    for byte in file:
        entry.append(byte)
        if list(
            filter( 
                lambda index: 
                    index[1] == entry, dictionary.items() 
            )): continue
        else:
            if (len(entry) > 1) :
                #Finds the key corresponding to all characters except the last one
                #and returns an array of the [(key,value)].Based on this format the
                #index of the value is the first element 0 of the returned array.
                reference = list(filter(
                    lambda index:
                        index[1] == entry[:-1], dictionary.items()
                ))[0][0]
                encoded[index] = [reference,entry[-1:][0]]
            else:
                encoded[index] = [0,entry[0]]
            dictionary[index] = entry
            entry = []
        index+=1
    return encoded


def compress_file(file_content) -> bytearray:
    compressed_file: bytearray = bytearray()
    entry: bytearray = bytearray(file_content)
    tmp_comp = compress(entry)
    for entry in tmp_comp.keys():
        ref = tmp_comp[entry][0]
        symbol = tmp_comp[entry][1]
        compressed_file.append(ref)
        compressed_file.append(symbol)

    return compressed_file    
    
    
    
