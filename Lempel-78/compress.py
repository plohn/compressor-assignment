def compress(phrase):
    dictonary:dict = {}
    encoded:dict = {}
    entry:str =""
    index:int =1
    phrase+="\0" #Add endline character
    for char in phrase:
        entry+=char
        if list(
            filter( 
                lambda index: 
                    index[1] == entry, dictonary.items() 
            )): continue
        else:
            if (len(entry) > 1) :
                #Finds the key corresponding to all characters except the last one
                #and returns an array of the [(key,value)].Based on this format the
                #index of the value is the first element 0 of the returned array.
                refence = list(filter(
                    lambda index:
                        index[1] == entry[:-1], dictonary.items()
                ))[0][0]
                encoded[index] = [refence,entry[-1:]]
            else:
                encoded[index] = [0,entry]
            dictonary[index] = entry
            entry = ""
        index+=1
    return encoded

print(compress("ABCC"))


