#ENCRYPTING METHOD USING INCREMENTING ASCII 
from os import system


def encrypt(passed_string,key,location):
    encrypted_string = ""
    for ch in passed_string:
            encrypted_string = encrypted_string + chr(ord(ch)+key) 
      
    with open(location,'w+',encoding="utf-8") as f:  
        f.writelines(encrypted_string)
        f.seek(0)
        print("ENCRPYTED: ",f.readline())
    
    print("Message Sent...")
    system('pause')


def decrypt(key,location):
    try:
        decrypted_string = ""
        with open(location,'r',encoding="utf-8") as f:
            file_content = f.readline()
            for ch in file_content:
                decrypted_string = decrypted_string + chr(ord(ch)-key)
    except FileNotFoundError:
        return 0 

    return decrypted_string

def sendMessage(location):
    my_string = input("Type Message: ")
    
    while(True):
        try:
            my_key = int(input("Encryption Key (Integer): "))
            if my_key == 0: 
                raise('key must greater than or equal to 1')
            break
        except Exception as e:
            print("Please Enter an Integer greater than 0, for the key.")
            continue

    encrypt(my_string,my_key,location)

def receiveMessage(location):
    my_key = int(input('Encryption Key: '))
    decrypted_string = decrypt(my_key,location)
    if decrypted_string:
        print("ENCRYPTED MESSAGE BASED ON YOUR KEY:")
        print(decrypted_string,"\n\n")
    else:
        print("Location Not Found")

    system('pause')

def main():
    location = 'internet.txt'
    while(True):
        system('cls')
        print("Current Location:",location[:-4])
        print("[1] SEND A MESSAGE\n[2] RECIEVE A MESSAGE\n[3] CHANGE LOCATION NAME\n[4] EXIT")
        choice = input("Please Select Above: ")
        if choice == '1':
            sendMessage(location)
        elif choice == '2':
            receiveMessage(location)
        elif choice == '3':
            temp_location = input("ENTER LOCATION NAME: ")
            location = temp_location+".txt"  
        else:
            continue

   
    

if __name__ == "__main__":
    main()