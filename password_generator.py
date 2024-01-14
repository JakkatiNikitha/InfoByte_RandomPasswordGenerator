import string
import random

length=int(input("Enter Password Length: "))

print("""Choose character set 
      1. Digits
      2. Lowercase Letters
      3. Uppercase Letters              
      4. Special Characters
      5. Exit""")

PasswordList=""

while(True):
    choice=int(input("Enter your choice:"))
    if(choice==1):
        PasswordList+=string.digits

    elif(choice==2):
       PasswordList+=string.ascii_lowercase

    elif(choice==3):
        PasswordList+=string.ascii_uppercase

    elif(choice==4):
        PasswordList+=string.punctuation

    elif(choice==5):
        break

    else:
        print("Please enter a valid option!")

password=[]

for i in range(length):
    RandomPassword=random.choice(PasswordList)
    password.append(RandomPassword)

print("The random password is: "+"".join(password))
