
import random
rock = '''
      _____
-----'  ___)
        (___)
        (____)
        (___)
 ---'__ (__)
'''
paper = '''
    _______
---'   ____)___
         ______)
         _______)
         ______)
---'_________)

'''
scissors = '''
    _____
---' ____)___
        _____)
     ________)
    (____)
---'_(__)
'''
choices = [rock,paper,scissors]
select = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n")
select_int = int(select)
if select_int > 2 or select_int < 0:
    print("Typed a wrong number you lose")
else:
    print(choices[int(select)])
    computer_select = random.randint(0,2)
    print("Computer chose")
    print(choices[computer_select])

    if select_int == computer_select:
        print("Draw")
    elif select_int == 0 and computer_select == 1:
        print("You Lose")
    elif select_int == 0 and computer_select == 2:
        print("You win")
    elif select_int == 1 and computer_select == 0:
        print("You Win")
    elif select_int == 1 and computer_select == 2:
        print("You Lose")
    elif select_int == 2 and computer_select == 0:
        print("You lose")
    elif select_int == 2 and computer_select == 1:
        print("You Win")
