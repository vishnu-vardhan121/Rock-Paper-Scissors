import random

while True:
    cpu_choice = random.randint(0, 2)
    user_choice = input('Enter your choice (rock/paper/scissors): ').strip().lower()

    if cpu_choice == 0:
        cpu_chose = 'rock'
    elif cpu_choice == 1:
        cpu_chose = 'paper'
    else:
        cpu_chose = 'scissors'

    print(f'CPU chose: {cpu_chose}')
    print(f'You chose: {user_choice}')

    if user_choice == 'rock':
        if cpu_chose == 'rock':
            print('Oops!! TIE 😁😀😀😁')
        elif cpu_chose == 'paper':
            print('You lose 😥😥😥')
        elif cpu_chose == 'scissors':
            print('You win 😀😀')
    
    elif user_choice == 'paper':
        if cpu_chose == 'paper':
            print('Oops!! TIE 😁😀😀😁')
        elif cpu_chose == 'rock':
            print('You win 😀😀')
        elif cpu_chose == 'scissors':
            print('You lose 😥😥😥')
    
    elif user_choice == 'scissors':
        if cpu_chose == 'scissors':
            print('Oops!! TIE 😁😀😀😁')
        elif cpu_chose == 'paper':
            print('You win 😀😀')
        elif cpu_chose == 'rock':
            print('You lose 😥😥😥')
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
