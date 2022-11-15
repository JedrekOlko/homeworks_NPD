def encrypt(text, code):
    dict = {}
    if( len(code)%2 != 0 ):
        return "Invalid length of code"
    for i in range(0, len(code), 2):
        if( dict.get( code[i] ) is not None or dict.get( code[i+1]) is not None ):
            return "Code is not unequivocal"
        dict[ code[i] ] = code[i+1]
        dict[ code[i+1] ] = code[i]

    wynik = ""
    for letter in text:
        if( dict.get(letter) is not None):
            wynik = wynik + dict[letter]
        else:
            wynik = wynik + letter
    return wynik

print( encrypt("SZYFR", "GADERYPOLUKI") )
print( encrypt("SZYFR CEZARA", "POLITYKARENU") )
print( encrypt("SZYFR KRÓLa", "GADERYPOLUKIGADERYPOLUKI") )

