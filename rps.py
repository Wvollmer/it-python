import random

def generateRandomNumber():
    randomnumber=random.randint( 1, 3 )
    return randomnumber

def getComputerChoice(randomnumber):
    if randomnumber == 1:
        computerChoice = "rock"
    elif randomnumber == 2:
        computerChoice = "paper"
    elif randomnumber == 3:
        computerChoice = "scissors"
    return computerChoice

def getUserChoice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    userChoice = int(input("please enter your choice: "))
    return userChoice

def DeterminWinner(userChoice, computerChoice):
    rockMessage = 'The rock smashes the scisscor'
    scissorsMessage = "scissers cuts paper"
    paperMessage = 'Paper wraps rock'
    winner = 'no winner'
    message = ""
    if computerChoice == "rock" and userChoice == 3:
        winner = 'Computer'
        message = rockMessage
    elif computerChoice == 'scissors' and userChoice == 1:
        winner = 'you'
        message = rockMessage
    elif computerChoice == "paper" and userChoice == 1:
        winner = 'Computer'
        message = paperMessage
    elif computerChoice == 'rock' and userChoice == 2:
        winner = 'you'
        message = paperMessage
    elif computerChoice == "scissors" and userChoice == 2:
        winner = 'Computer'
        message = scissorsMessage
    elif computerChoice == 'paper' and userChoice == 3:
        winner = 'you'
        message = scissorsMessage
    return (winner, message)


def startAgain():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print('The computer chose', computerChoice)
    winner, message = DeterminWinner(computerChoice, userChoice)

    if winner != 'no winner':
       print(f"{winner} won, {message} ")

    return winner

def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice( randomNumber )
    userChoice = getUserChoice()
    print( 'The computer chose', computerChoice )
    winner, message = DeterminWinner(userChoice, computerChoice)

    if winner != 'no winner':
       print(f"{winner} won, {message}")
    else:
        print("It's a tie!")



print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗")
print(" ▏ Rock,Paper,Scissors ▕")
print(" ▏ by william vollmer  ▕")
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

print("hello i heard rock paper scissors is fun so let's play that first to 3 wins good luck =)")
main()