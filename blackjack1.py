import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#Creating card class#

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Creating Deck, shuffle function and single dealing#

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n' + card.__str__() 
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Creating a hand#
        
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces since it can be 1 or 11
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
            
#Creating Chips balance for comeptitor#            

class Chips:
    
    def __init__(self, total):
        self.start = total  #  Find out if player win or lose at the end of the game
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
#Taking bets#

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please place your bet: '))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed {} '.format(chips.total))
            else:
                break      

#Taking hits#

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#Player decides to take hit, stand or ask for tips#

def hit_or_stand(deck,player_hand,dealer_hand,chips):
    global playing
    
    if player_hand.value == 21:
        print("Black jack!!!")
        playing = False
        return
    
    while True:
        x = input("Would you like to Hit, Double down, Stand or Tips? Enter 'h', 'd', 's' or 't' ")
        
        if x[0].lower() == 'h':
            hit(deck,player_hand)  # hit() function defined above
            
        elif x[0].lower() == 'd':
            if chips.total >= chips.bet * 2:
                chips.bet *= 2
                print("Player is double down betting $", chips.bet)
                hit(deck,player_hand)  # Only draw 1 card after double down
                playing = False
            else:
                print("Not enough chip to double down")
                continue

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        
        elif x[0].lower() == 't':
            tips(player_hand, dealer_hand)
            continue

        else:
            print("Sorry, please try again.")
            continue
        break

#Methods to display cards#

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<Hidden card>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
        
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

#functions to handle game scenarios#

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")    
    
def tips(player, dealer):
    # print("dealer value = ", values[dealer.cards[1].rank])
    if player.value <= 11 and values[dealer.cards[1].rank] < 7:
        print("You shall double down")
    elif player.value <= 11:
        print("You shall hit")
    elif player.value >= 17:
        print("You shall stand")
    elif player.value < 17 and values[dealer.cards[1].rank] >= 10:
        print("You shall hit")
    elif player.value > 11 and values[dealer.cards[1].rank] < 7:
        print("You shall stand")
    else:
        print("Either way")
        
# Print an opening statement
print("Welcome to my Blackjack game (school). Good Luck!")

# Set up the Player's chips
player_chips = Chips(int(input('How much do you want to start with? ')))

#Start the game
while True:
    
    if player_chips.total <= 0:
       print("You have $0 chips, game over")
       break
    
    #Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    #Prompt the Player for their bet
    take_bet(player_chips)
    
    #Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  #recall this variable from our hit_or_stand function
        
        #Prompt for Player to Hit, double down, stand or ask for tips
        hit_or_stand(deck, player_hand, dealer_hand, player_chips)
        
        #Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand) 
        
        #If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
        
    
    #Inform Player of their chips total
    print("\nPlayers winnings stand at $", player_chips.total)
    if player_chips.total <= 0:
        print("Game over, better luck next time")
        break
    
    #Ask to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Player cash out $', player_chips.total)
        if player_chips.start > player_chips.total:
            print('Lose $', player_chips.start - player_chips.total)
        else:
            print('Win $', player_chips.total - player_chips.start )
            
        print('Thanks for playing! Come back soon')

        break
