from card import *
import random

class Deck:
    pile = []
    discard = []
    
    def __init__(self):
        for i in range(4):
            color = Color(i)
            for j in range(13):
                detail = Detail(j)

                if detail == Detail.ZERO:
                    self.pile.append(Card(color, detail))
                    
                if detail.value > 0 and detail.value < 13:
                    for i in range(2):
                        self.pile.append(Card(color, detail))

        for i in range(4):
            self.pile.append(Card(Color.ALL, Detail.WILD))
            self.pile.append(Card(Color.ALL, Detail.WILD_DRAW_FOUR))
        
    def draw_card(self):
        if(len(self.pile) < 108*.25):
            self.pile.extend(self.discard)
        
        if(self.pile.__len__() > 0):
            card = random.choice(self.pile)
            self.pile.remove(card)
            return card            

    def __iter__(self):
        while(self.pile.__len__() > 0):
            yield self.draw_card()
        

                    

            