##Ryder McDowell

global inputPassword
global encodedPassword
def encode():
    global inputPassword
    inputPassword = input("Please enter your password to encode:")
    global encodedPassword
    encodedPassword = " "
    for i in range(8):
        addedChar = str(3 + int(inputPassword[i]))
        encodedPassword = encodedPassword + addedChar
    encodedPassword = encodedPassword.lstrip()
    print("Your password has been encoded and stored!")
    print(" ")
def decode():
     
    decodedPassword = " "
    for i in range(8):
        addedChar = str(int(inputPassword[i])+3*-1)
        decodedPassword = decodedPassword + addedChar
    decodedPassword = decodedPassword.lstrip()
    print(f"The encoded password is {encodedPassword}, and the original password is {inputPassword}.")
    print(" ")
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print(" ")
    menuChoice = int(input("Please enter an option:"))
    return menuChoice
    
menuChoice = 0   
while menuChoice < 3:
    menuChoice = menu()
    if menuChoice == 1: encode()
    if menuChoice == 2: decode()
    if menuChoice == 3: quit()

