def compress(file: bytearray) -> dict:
    dictionary:dict  = dict()
    encoded:dict    = dict()
    entry:bytearray = bytearray()
    index:int       = 1
   
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
                encoded[index] = [reference,entry[-1:]]
            else:
                encoded[index] = [0,entry]
            dictionary[index] = entry
            entry = bytearray()
        index+=1
    return encoded

def createFile(encodedmsg: list):
    data: str() = str()
    for value in encodedmsg:
        for item in value:
            data+=str(item)
    with open("output.cmp","wb") as f:
        f.write(bytes(data))
    return data

compressedFile:bytearray = bytearray()

with open("test.txt","rb") as input:
    entry:bytearray = bytearray(input.read())
    for ref in list(compress(entry).values())
        for symbol in ref:
            if (isinstance(symbol, int)):
                compressedFile.append(symbol)
            else:
                compressedFile.extend(symbol)

with open("output","wb") as f:
    f.write(compressedFile)
    
    
    
    