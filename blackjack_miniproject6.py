# Mini-project #6 - Blackjack
# codeskulptor link
#http://www.codeskulptor.org/#user45_iIQ63QVg0dxcptK_72.py

# Relevant examples
#http://www.codeskulptor.org/#examples-blackjack_template.py
#http://www.codeskulptor.org/#examples-tips6.py
#http://www.codeskulptor.org/viz/#examples_points.py
#http://www.codeskulptor.org/#examples-tiled_images.py
#http://www.codeskulptor.org/#examples-blackjack.py
#http://www.codeskulptor.org/#examples-particle_testing_template.py
#http://www.codeskulptor.org/#examples-particle_class.py
#http://www.codeskulptor.org/#examples-oo-ball.py
#http://www.codeskulptor.org/#examples-oo-character.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        ans = "Hand contains"
        for i in range(len(self.cards)):
            ans += " " + str(self.cards[i])
        return ans

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        has_ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        if not has_ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
            
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        dx = 0
        for c in self.cards:
            c.draw(canvas, [pos[0] + dx, pos[1]])
            dx += 75
         
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)    # use random.shuffle()

    def deal_card(self):
        return self.cards.pop()	# deal a card object from the deck
    
    def __str__(self):
        # return a string representing the deck
        ans = "Deck contains"
        for i in range(len(self.cards)):
            ans += " " + str(self.cards[i])
        return ans

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score, message
    
    if in_play:
        outcome = ""
        #print "You lose."
        score -= 1
        in_play = False
        #print "Score is " + str(score)
        message = "New deal?"
        #print message

    # your code goes here
    deck = Deck()
    deck.shuffle()
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    #print ""
    #print "New game!"
    #print ""
    #print "Dealer " + str(dealer_hand)
    #print "Player " + str(player_hand)
    #print "Player has " + str(player_hand.get_value())
    #print ""
    message = "Hit or stand?"
    #print message
    #print ""
    outcome = ""
    in_play = True

def hit():
    # replace with your code below
    global in_play, deck, player_hand, score, message, outcome
 
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        #print "Player " + str(player_hand)
        #print "Player has " + str(player_hand.get_value())
        #print ""
        if player_hand.get_value() <= 21:
            message = "Hit or stand?"
            #print message
        else:
            outcome = "You went bust and lose."
            #print outcome
            in_play = False
            score -= 1
            #print "Score is " + str(score)
            message = "New deal?"
            #print message
        #print ""    
                
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play, deck, dealer_hand, player_hand, outcome, score, message
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            #print "Dealer " + str(dealer_hand)
            #print "Dealer has " + str(dealer_hand.get_value())
            #print ""

    # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() >= player_hand.get_value() and dealer_hand.get_value() <= 21:
            outcome = "You lose."
            score -= 1
        else:
            outcome = "You win."
            score += 1
        in_play = False
        #print outcome
        #print "Score is " + str(score)
        message = "New deal?"
        #print message
        #print ""

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    # Draw text
    canvas.draw_text('Blackjack', (100, 75), 48, 'Aqua')
    canvas.draw_text('Score: ' + str(score), (400, 75), 36, 'Black')
    canvas.draw_text('Dealer', (50, 150), 36, 'Black')
    canvas.draw_text(outcome, (200, 150), 36, 'Black')
    dealer_hand.draw(canvas, [50, 200])
    
    canvas.draw_text('Player', (50, 400), 36, 'Black')
    canvas.draw_text(message, (200, 400), 36, 'Black')
    player_hand.draw(canvas, [50, 450])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_CENTER[0]+50, CARD_CENTER[1]+200], CARD_SIZE)
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric