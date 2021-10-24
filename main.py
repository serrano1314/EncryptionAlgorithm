from os import system

# ENCRYPTING METHOD USING INCREMENTING ASCII 
def encrypt(passed_string,key,location):
    encrypted_string = ""
    for ch in passed_string:
            encrypted_string = encrypted_string + chr(ord(ch)+key) 
      
    with open(location,'w+',encoding="utf-8") as f:  
        f.writelines(encrypted_string)


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
    my_string = input("Type Message: \033[94m")
    print('\033[0m')
    encrypt(my_string,get_key(),location)
    print("\033[92mMessage Sent...\033[0m")
    system('pause')


def receiveMessage(location):
    decrypted_string = decrypt(get_key(),location)
    if decrypted_string:
        print("ENCRYPTED MESSAGE BASED ON YOUR KEY:")
        print("\033[96m",decrypted_string,"\033[0m\n\n")
    else:
        print("\033[93mLocation Not Found\033[0m")

    system('pause')


def get_key():
    while(True):
        try:
            my_key = int(input("Encryption Key (Integer): \033[94m"))
            print('\033[0m')
            if my_key == 0: 
                raise('key must greater than or equal to 1')
            break
        except Exception as e:
            print("Please Enter an Integer greater than 0, for the key.")
            continue

    return my_key


def main():
    location = 'default.txt'
    while(True):
        system('cls')
        print("\033[0mCurrent Location: \033[92m",location[:-4],"\033[0m")
        print("[1] SEND A MESSAGE\n[2] RECIEVE A MESSAGE\n[3] CHANGE LOCATION\n[4] EXIT")
        choice = input("Please Select Above: ")
        if choice == '1':
            sendMessage(location)
        elif choice == '2':
            receiveMessage(location)
        elif choice == '3':
            temp_location = input("ENTER LOCATION NAME: \033[92m")
            location = temp_location+".txt"  
        elif choice == '4':
            return
        else:
            continue


if __name__ == "__main__":
    main()