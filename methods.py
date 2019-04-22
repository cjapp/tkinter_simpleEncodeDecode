

class Method():

    def __init__(self, name, encode, decode):
        self.name = name
        self.encode = encode
        self.decode = decode


#
# METHODS FUNCTIONS BELOW
#
#

def ceasarMethod(offset, content):
    encrypted = []
    c = 'i'

    if not isinstance(content, str):
        print("Error in Encrypt_Ceasar: Text is not a str.")
        return ''

    for i in content:
        #determine if i is a letter
        if i.isalpha():
            if i.isupper():
                c = chr(((ord(i)-65)+offset)%26 + 65)
            else:
                c = chr(((ord(i)-97)+ offset)%26 + 97)
        else:
            c = i

        encrypted.append(c)

    return encrypted


def enCeasar(content):
    return ceasarMethod(1,content)

def deCeasar(content):
    return ceasarMethod(-1,content)

def enRot(content):
    return ceasarMethod(10,content)

def deRot(content):
    return ceasarMethod(-10,content)

