
def user_input():
    global validInput
    global inputNumber
    inputNumber = input("Please Enter A Number:")
    try:
        inputNumber = int(inputNumber)
        validInput = True
    except:
        print("Not a valid Number.")
        validInput = False
    return inputNumber

validInput = False
inputNumber = 0
while not validInput:
    user_input()

if inputNumber > 1:
    for n in range(2,inputNumber):
        if (inputNumber%n) == 0:
            print(inputNumber,"is not a prime number.")
            break
    else:
        print(inputNumber,"is a prime number.")

else:
    print(inputNumber,"is a prime number.")
