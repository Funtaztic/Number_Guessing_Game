import random
found = False
randomNumber = random.randint(1,100)

while not found:
    UserGuess = int(input("Your guess: "))
    if UserGuess == randomNumber:
        print("You guessed it!!")
        found = True
    elif UserGuess < randomNumber:
        print("Guess higher!!")
    else:
        print("Guess lower!!")
