#!/opt/anaconda3/bin/python

import random


class Deck:
    """
    Class for a deck of cards.
    """
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':None}

    def __init__(self):
        """Initialises a deck of cards."""  
        self.all_cards = []
        
        
    def reset(self):
        """
        Fills the deck out with 52 cards, and shuffles it.
        """

        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.ace_value()        
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

        self.shuffle()

    
    
    def shuffle(self):
        """Shuffles the cards."""
        return random.shuffle(self.all_cards)
    
    
    def deal_one(self):
        """Selects the last card in the deck."""
        try:
            topcard = self.all_cards.pop()
        except IndexError:
            print("End of pack! The deck will be reshuffled.") 
            self.reset()
            topcard = self.all_cards.pop()


        return topcard
    
    def run_once(f):
        """
        A decorator to restrict a function to run only once.
        Used so that the ace_value function runs only the first
        time the pack is reset during a game.
        """
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return f(*args, **kwargs)
        wrapper.has_run = False
        return wrapper

    @run_once
    def ace_value(self):
        """Let's the user choose whether the Ace is worth 1 or 11."""
        while True:
            try:
                self.values["Ace"] = int(input("Before we start, decide on the value of the Ace card. Please enter either 1 or 11: "))
                if self.values["Ace"] == 1 or self.values["Ace"] == 11:
                    break
                print("The value chosen needs to be either 1 or 11. Please try again.")
            except KeyboardInterrupt: # In case of exit.
                exit()
            except ValueError:
                print("Input must be an integer!")

class Dealer:
    """
    Class for the (NPC) Dealer.
    """
    
    def __init__(self):
        """
        Initialises the dealer's hand, and chips.
        """
        self.dealer_cards = []
        self.bankroll = 0 # The dealer starts with no chips.
        
        
    
    def hit_one(self,new_cards):
        """ Adds a card to the dealers hand""" 
        self.dealer_cards.append(new_cards)

    def __str__(self):
        """Displays the current card score of the dealer."""
        return f'The dealer currently has {sum(dealer_cards)} points.'

class Card(Deck):
    """
    Class for a single card. Inherits from Deck class.
    """
    def __init__(self, suit, rank):
        """
        Initialises a card.  
        """
        super().__init__()
        self.suit = suit
        self.rank = rank
        self.value = Deck.values[rank]
        
    def __str__(self):
        """ Displays the current card. """
        return self.rank + " of " + self.suit



class Player:
    """ Class for the (human) player."""
    def __init__(self, bankroll):
        self.bankroll = bankroll
        self.name = self.define_name()
        self.player_cards = []
        
    def bet(self):
        """Allows the player to bet their chips."""
        print(f"Your bank balance starts at: {self.bankroll}")
        
        while True:
            try:
                bet = input( self.name + ", please enter an amount to bet: ")
                if int(bet) <= self.bankroll:
                    break
                print("Insufficient funds! Please try again.")
            except ValueError:
                print("Please enter an integer value.")
            
        self.bankroll -= int(bet)
        print(f"""Thanks! Your balance is now: {self.bankroll}. 
            Win, and your bet is returned doubled!""")
        return bet
        
    def hit_one(self,new_cards): 
        """Adds a card to the player's hand."""       
        self.player_cards.append(new_cards) 
    
    def define_name(self):
        """ Allows the player to choose a name."""
        name = input("Please enter your name: ")
        print(f"Welcome to the pain station, {name}, of Blackjack!")
        return name
