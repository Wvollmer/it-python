comp_wins = 0
player_wins = 0

def chose_option():
    user_choice = input("choose rock, paper or scissors: ")
    if user_choice in ['1']:
        user_choice = "rock"
    elif user_choice in ['2']:
        user_choice = "paper"
    elif user_choice in ['3']:
        user_choice = "scissors"
    else:
        print('sorry i didnt understand can u please try again.')
        chose_option()
    return user_choice

def computer_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "rock"
    elif comp_choice == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"
    return comp_choice

while True:
    print("")
    user_choice = chose_option()
    comp_choice = computer_option()
