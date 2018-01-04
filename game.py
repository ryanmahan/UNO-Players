from deck import Deck 
from dumb_player import DumbPlayer
from card import Detail
import copy

deck = Deck()
players = []

PLAYER_AMOUNT = 4
HAND_SIZE = 7

for i in range(PLAYER_AMOUNT):
    hand = []
    for j in range(HAND_SIZE):
        hand.append(deck.draw_card())
    players.append(DumbPlayer(hand, deck))

last_played = deck.draw_card()
forward = True
draw = 0

while(True):

    i = i%PLAYER_AMOUNT

    if draw is not 0: #if player before sets draw to nonzero value
        for d in range(draw):
            players[i].add_to_hand(deck.draw_card())
        draw = 0
        if forward:
            i += 1
        else:
            i -= 1
        #TODO: insert draw two stacking logic here

    #play card and add to discard pile
    else:

        print("Card down: ")
        print(last_played)
        print(str(i) + " Player Hand: ")
        print(players[i])

        played_card = players[i].play_card(last_played)
        
        while not played_card:
            new_card = deck.draw_card()
            played_card = players[i].check_card(new_card, last_played)

        last_played = copy.deepcopy(played_card)
        deck.discard.append(played_card)

        #check for win
        if players[i].has_won():
            print("PLAYER " + str(i) + " WINS!")
            break

        #do special actions
        if last_played.detail.value > 9:
            if last_played.detail == Detail.REVERSE:
                forward = not forward
            
            elif last_played.detail == Detail.SKIP:
                if forward:
                    i += 1
                else:
                    i -= 1
            
            elif last_played.detail == Detail.DRAW_TWO:
                draw = 2

            elif last_played.detail == Detail.WILD:
                last_played.color = players[i].choose_color()
            
            elif last_played.detail == Detail.WILD_DRAW_FOUR:
                last_played.color = players[i].choose_color()
                draw = 4

        #iterate
        if forward:
            i += 1
        else:
            i -= 1
        