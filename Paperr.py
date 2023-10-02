import random

while True:
    print("Enter your choice\n1 - Rock\n2 - Paper\n3 - Scissors\n")

    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺'))

    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissors'

    print('User choice is:', user_choice)
    print('Now it\'s Computer\'s Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(f'{user_choice} Vs {comp_choice_name}')

    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock'
    else:
        result = 'Scissors'

    if result == 'DRAW':
        print("<== It's a tie ==>")
    elif result == user_choice:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing")