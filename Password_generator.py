import random

def generatePassword(n):
    characters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chosenLetter = random.sample(characters, n)

    password = "".join(chosenLetter)

    return password
if __name__ == "__main__":
    n = int(input("Enter the length of the password: "))
    password = generatePassword(n)
    print("A randomly selected password is:", password)
