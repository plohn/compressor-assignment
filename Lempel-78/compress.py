def compress(phrase: str) -> dict:
    dictionary:dict  = dict()
    encoded:dict    = dict()
    entry:str       = str()
    index:int       = 1
    phrase          = str(phrase)
    phrase         += "\0" #Add endline character
    
    for char in phrase:
        entry += char
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
                refence = list(filter(
                    lambda index:
                        index[1] == entry[:-1], dictionary.items()
                ))[0][0]
                encoded[index] = [refence,entry[-1:]]
            else:
                encoded[index] = [0,entry]
            dictionary[index] = entry
            entry = str()
        index+=1
    return encoded

def createFile(encodedmsg: list):
    data: str() = str()
    for value in encodedmsg:
        for item in value:
            data+=str(item)
    with open("output.cmp","wb") as f:
        f.write(bytes(data, 'utf-8'))
    return data

with open("sample.txt","rb") as input:
    createFile(
        list(
            compress(input.read()).values()
        )
    )

    
    
