#ENCRYPTING METHOD USING INCREMENTING ASCII 
def encrypt(passedString,key):
    encryptedString = ""
    for ch in passedString:
        encryptedString = encryptedString + chr(ord(ch)+key)

    return encryptedString

def decrypt(passedString,key):
    decryptedString = ""
    for ch in passedString:
        decryptedString = decryptedString + chr(ord(ch)-key)

    return decryptedString

def main():
    myKey=29
    myString = encrypt("abc def ghi jkl",myKey)
    print(myString)
    print(decrypt(myString,myKey))

if __name__ == "__main__":
    main()