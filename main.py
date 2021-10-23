def encrypt():
    pass

def decrypt():
    pass


def main():
    myString = "abc def ghi jkl"
    encryptedString = ""
    for ch in myString:
        encryptedString = encryptedString + chr(ord(ch)+1)
    
    print(encryptedString)

if __name__ == "__main__":
    main()