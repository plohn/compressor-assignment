
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

compressedFile:bytearray = bytearray()

with open("a.out","rb") as input:
    entry:bytearray = bytearray(input.read())
    file = compress(entry) 
    for entry in file.keys():
        ref = file[entry][0]
        symbol = file[entry][1]
        compressedFile.append(ref)
        compressedFile.append(symbol)

with open("output","wb") as f:
    f.write(compressedFile)
    
    
    
    
