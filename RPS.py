import random
while True:
    print("***********WELCOME TO ROCK PAPER SCISSOR GAME************")
    user_score=0
    comp_score=0
    ties=0
    print("""choices are:
    1. Rock
    2. Paper
    3. Scissor""")
    choice =int(input("enter your choice from 1-3: "))
    print()
    while choice >3 or choice <1:
        choice=int(input("enter valid input"))
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scissor"
    print("The user's choice is", user_choice)
    print("Now its computer's turn")
    computer=random.randint(1,3)
    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissor"
    print("the computer's choice is", comp_choice)
        #now we have to make comparisions to deccide who  wins
    if((user_choice=="paper" and comp_choice=="Rock") or (user_choice=="Rock" and comp_choice=="Paper")):
        print("paper wins")
        result="Paper"
    elif((user_choice=="Rock" and comp_choice=="Scissor") or (user_choice=="scissor" and comp_choice=="Rock")):
        print("Rock wins")
        result="Rock"
    elif(user_choice==comp_choice):
        print("its a tie")
        result="Tie"
    else:
        print("scissor wins")
        result="Scissor"
    if result=="Tie":
        ties +=1
    elif result ==user_choice:
        print("user wins")
        user_score+=1
    else:
        print("computer wins")
        comp_score+=1
        print("scores are")
        print("user's score is", user_score)
        print("computer's score is", comp_score)
        print("ties are", ties)


    repeat= input("DO YOU WANT TO PLAY THE GAME AGAIN?")
    if repeat=="No" or repeat=="No":
       break
    print("GAME OVER!!!")
    print("THANKS FOR PLAYING")
