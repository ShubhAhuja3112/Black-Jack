import random

print('WELCOME TO BLACKJACK')

suits = ['♠', '♥', '♦', '♣']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

points = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '1': 10, # Sasta Jugaad
    'J': 10,
    'Q': 10,
    'K': 10
}

cards = []

for i in suits:
    for j in values:
        cards.append(j + i)
        
random.shuffle(cards)
        
dealer_card_1 = cards[0]
dealer_card_2 = cards[1]

player_cards = [cards[2]]
lv = 3
player_sum = points[cards[2][0]]

print('Dealer Cards: ', dealer_card_1, '?')

while True:
    print('Your Cards: ', player_cards)
    print('Press H to hit and S to stand')
    choice = input()
    if choice == 'S' or choice == 's':
        break
    elif choice == 'H' or choice == 'h':
        player_cards.append(cards[lv])
        player_sum += points[cards[lv][0]]
        lv += 1
        if player_sum > 21:
            print('Your Cards: ', player_cards)
            print('YOU LOOOOOOOOOSSSSEEEEEEEE NOOOOOBBBBBBBBBB')
            exit(0)
        if player_sum == 21:
            print('Your Cards: ', player_cards)
            print('BLACKJACK WIN')
            exit(0)
    else:
        print('Choose again')
       
dealer_sum = points[dealer_card_1[0]] + points[dealer_card_2[0]]
dealer_cards = [dealer_card_1, dealer_card_2]        

while True:
    print('Dealer Cards: ', dealer_cards)
    if dealer_sum < player_sum:
        dealer_cards.append(cards[lv])
        dealer_sum += points[cards[lv][0]]
        lv += 1
        if dealer_sum > 21:
            print('Dealer Cards: ', dealer_cards)
            print('YOU WIN')
            exit(0)
    else:
        print('DEALER WINS')
        exit(0)
