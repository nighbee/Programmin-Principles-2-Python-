import random

print("Winning rules of game rock, paper, scissors: "
      + "Rock<Paper<Scissors")

while True:
    print("enter ur choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    choice= int(input())

    while choice >3 or choice<1:
        choice= int(input("invalid number of choice, choice should be between 1 and 3!"))

    if choice==1:
        choice_name= 'Rock'
    elif choice==2:
        choice_name= 'Paper'
    elif choice == 3:
        choice_name= 'Scissors'

    print("Your choice is: " + choice_name)

    print("Now it is computers turn....")

    comp_choice= random.randint(1,3)

    while comp_choice==choice:
        comp_choice= random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name= 'rocK'
    elif comp_choice==2:
        comp_choice_name= 'papeR'
    elif comp_choice==3:
        comp_choice_name='scissorS'

    print("Comp choice is: "+ comp_choice_name)
    print("your choice VS computers choice: ")

    if choice== comp_choice:
        print("its Draw", end="")
        result="DRAW"
    if (choice==1 and comp_choice==2):
        print('paper wins =>', end="")
        result="papeR"
    elif choice==2 and comp_choice==1:
        print("paper wins =>", end="")
        result='Paper'
    if choice ==1 and comp_choice==3:
        print("Rock wins =>", end="")
        result='Rock'
    elif choice==3 and comp_choice==1:
        print("Rock wins =>", end="" )
        result='rocK'
    if choice==2 and choice==3:
        print("Scissors wins =>", end="")
        result="scissorS"
    elif choice ==3 and comp_choice==2:
        print("Scissors wins =>", end="")
        result='Rock'

    if result == 'DRAW':
        print(" <= Its a Tie =>")
    elif result == choice_name:
        print(" <= User wins =>")
    else:
        print(" <= Computer wins =>")
    print("do you wanna play again? (Y/N)")

    ans= input().lower
    if ans == 'n':
        break

print("Thanks for playing and wasting your time! ")


