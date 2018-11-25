import random
def roll_dice(numbers=3,points=None):
    print('<<<<<<< ROLL THE DICE! >>>>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 < total < 18
    isSmall = 3 < total < 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    your_money = 1000
    while your_money > 0:
        print('<<<<<<< GAME STARTS! >>>>>>>')
        print('You have {} now'.format(your_money))
        choices = ['Big','Small']
        your_choice = input('Big or Small:')
        if your_choice in choices:
            your_bet = int(input('How much you wanna bet ? - '))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points is',points,'You win !')
                print('You gained {},you have {} now'.format(your_bet,your_money + your_bet))
                your_money = your_money + your_bet
            else:
                print('The pionts is',points,'You lose !')
                print('You lost {},you have {} now'.format(your_bet,your_money - your_bet))
                your_money = your_money - your_bet
        else:
            print('Invalid words')
    else:
        print('GAME OVER')

start_game()
