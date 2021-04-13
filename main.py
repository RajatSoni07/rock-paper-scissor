import random
import time
a1 = input('How many round do you want\n==> ')
ai = int(a1)

if ai%2 == 0:
    ai=ai+1

win_point = (ai+1)/2

player_point = 0
bot_point = 0

while True:
    playerin = input('What do you want to Make Rock Paper or Scissors\n=>> ')
    playerin = playerin.lower()
    
    print('3...')
    time.sleep(0.5)
    print('2..')
    time.sleep(0.5)
    print('1.')
    time.sleep(0.5)
    print('Go')
    
    botrand = random.randint(1,3)
    if botrand==1:
        botin = 'rock'
    elif botrand==2:
        botin = 'paper'
    else:
        botin = 'scissors'
        
    print(f'\nYou made a {playerin.capitalize()}, Bot made a {botin.capitalize()}\n')
    
    if playerin == 'rock':
        if botin == 'rock':
            print("It's a Tie")
        elif botin =='paper':
            print('Bot won')
            bot_point = bot_point+1  
        else:
            print('You won')
            player_point = player_point+1
    elif playerin == 'paper':
        if botin == 'rock':
            print('You won')
            player_point = player_point+1
        elif botin =='paper':
            print("It's a Tie")
        else:
            print('Bot won')
            bot_point = bot_point+1 
    else:
        if botin == 'rock':
            print('Bot won')
            bot_point = bot_point+1
        elif botin =='paper':
            print('You won')
            player_point = player_point+1
        else:
            print("It's a Tie")
    
    print('\n')
    if bot_point == win_point:
        print('Bot won the match')
        break
    elif player_point == win_point:
        print('Player won the match')
        break
    print(f'You points were {int(player_point)} and bot\'s points were {int(bot_point)}')
    
print(f'You points were {int(player_point)} and bot\'s points were {int(bot_point)}')
print('\n\nGame Over!!!!')
print('\n\nThanks for playing this project was made by rajat soni')
        

        
    