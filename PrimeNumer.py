inputNumber = input("Please Enter A Number:")
try:
    inputNumber = int(inputNumber)
except:
    print("Not a valid Number.")
    quit()

if inputNumber > 1:
    for number in range(2,inputNumber):
        if (inputNumber%number) == 0:
            print(inputNumber,"is not a prime number.")
            break
    else:
        print(inputNumber,"is a prime number.")

else:
    print(inputNumber,"is a prime number.")
