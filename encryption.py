text = input("enter the text:")
shift = int(input("enter the shift no:"))
encrypted_text =""

for char in text:
    if char.isalpha():
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift)%26+ord('A'))
        else:
            encrypted_char = chr((ord(char) - ord('a') + shift)%26+ord('a'))
            encrypted_text += encrypted_char
    else:
        encrypted_text +=char
print("encrypted text",encrypted_text) 

decrypted_text =""
for char in encrypted_text:
    if char.isalpha():
        if char.isupper():
            decrypted_char = chr((ord(char)-ord('A')-shift)%26+ord('A'))
        else:
            decrypted_char = chr((ord(char)-ord('a')-shift)%26+ord('a'))
            decrypted_text += decrypted_char
    else:
        decrypted_text +=char  
print("decrypted text",decrypted_text)  




     