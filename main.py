#ENCRYPTING METHOD USING INCREMENTING ASCII 
def encrypt(passed_string,key,location):
    encrypted_string = ""
    for ch in passed_string:
            encrypted_string = encrypted_string + chr(ord(ch)+key) 

    # print("ECRYPTED: ",encrypted_string)        
    with open(location,'w+',encoding="utf-8") as f:  
        f.writelines(encrypted_string)
        f.seek(0)
        print("ENCRPYTED: ",f.readline())


def decrypt(key,location):
    decrypted_string = ""
    with open(location,'r',encoding="utf-8") as f:
        file_content = f.readline()

    for ch in file_content:
        decrypted_string = decrypted_string + chr(ord(ch)-key)

    return decrypted_string


def main():
    my_key=29
    location = 'internet.txt'
    encrypt("abc def ghi 6kl",my_key,location)
    decrypted_string = decrypt(my_key,location)
    print("DECRYPTED: ",decrypted_string)

if __name__ == "__main__":
    main()