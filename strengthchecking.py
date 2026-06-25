password = input("enter the password:")

found_upper = False
found_lower = False
found_number = False
found_special = False

special_chars="!@#$%^&*()_+{}:.,';][\=/<>?|"
 
for char in password:
    if(char.isupper()):
        found_upper = True
    elif(char.islower()):
        found_lower = True
    elif(char.isdigit()):
        found_number = True
    elif (char in special_chars):
        found_special = True

strength = 0
if(len(password)>8):
    strength += 1
if(found_upper):
    strength += 1
if (found_lower):
    strength += 1
if (found_number):
    strength += 1
if (found_special):
    strength += 1

if (strength <= 2):
    print("weak password")
elif(strength <= 4):
    print("medium password")
else:
    print("strong password") 



                                                                                                                                                                