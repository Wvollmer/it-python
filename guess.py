import random

print("==========================")
print("   GUESS MY NUMBER >:)    ")
print("==========================")
print("")
name = input("What is your name?")
the_number = random.randint(0,100000)

print("")
print("im thinking of a integer between 0 and =). can you guess it")

guess = -1

while guess != the_number:
    guess_text = input("what is your guess")
    guess = int(guess_text)
    if guess < the_number:
        print(f"no, {name}, higher... ")
    elif guess > the_number:
        print(f"no, {name}, lower... ")
    else:
        print(f"={name}={name}={name}={name}={name}={name}={name}={name}=")
print('thanks for play')