#!/opt/anaconda3/bin/python



from classes import Player
from classes import Deck
from classes import Dealer

def initialise():
    """Sets up the game."""
    player = Player(10)
    dealer = Dealer()

    new_deck = Deck()
    new_deck.reset()
    return player, dealer, new_deck

def player_turn(player, new_deck):
    """The (human) player's go in the game."""
    player_sum = 0
    print(f"Okay, {player.name}, let's play!")
    print(f"Your current sum is {player_sum}")
    play_choice = input("Would you like to draw your first card? y/n: ")
    while play_choice == 'y':
        drawn_card = new_deck.deal_one()
        player_sum += drawn_card.value
        if player_sum >= 21:
            break

        else: 
            play_choice = input(f"Your score is {player_sum}. Would you like to draw another card? y/n: ")


    
    print(f"Your final score is {player_sum}.")

    return player_sum

def dealer_turn(player, dealer, new_deck):
    """ The (NPC) dealer's go."""
    score_to_beat = player_turn(player, new_deck)
    dealer_sum = 0
    while dealer_sum < 21 and dealer_sum <= score_to_beat:
            drawn_card = new_deck.deal_one()
            dealer_sum += int(drawn_card.value)
    newlist = [score_to_beat, dealer_sum]        
    return newlist



def play_game(player,dealer,new_deck):
    """The game happens here."""
    game_on = True
    bust_score = 21
    while game_on:
        pot = int(player.bet()) # The chips on offer in this go.
        player_sum, dealer_sum = dealer_turn(player, dealer, new_deck) 
        
        if player_sum >= bust_score:
            print(f'{player.name} has gone bust! Dealer collects the cash, {pot}! Bad luck!')
            print(f'{player.name} now has {player.bankroll} chips, oh no!')

        elif dealer_sum >= bust_score:
            print(f'Dealer has scored {dealer_sum}, and has gone bust! {player.name} collects the cash, {pot*2} chips! Yay!')
            player.bankroll += pot*2
            print(f'{player.name} now has {player.bankroll} chips, nice job!')

        elif dealer_sum > player_sum:
            print(f'The dealer has scored {dealer_sum}, which is closer to 21! Dealer collects the cash, {pot}! Bad luck!')
            print(f'{player.name} now has {player.bankroll} chips, oh no!')

        else:
            print(f'The dealer scored {dealer_sum}, so player has scored closer to 21! {player.name} collects the cash, {int(player.bet())*2} chips! Yay!')
            player.bankroll += pot*2
            print(f'{player.name} now has {player.bankroll} chips, nice job!')


        
        play_again = input(f"Want to play another go? A reminder that your remaining cash is now {player.bankroll}. Answer with y/n")
      
        if play_again == "y":
            pass    
        else:
            print(f"Thanks so much for playing, {player.name}. I hope you enjoyed the game!")
            game_on = False
            break

    

if __name__ == "__main__":
    player, dealer, new_deck = initialise()
    play_game(player,dealer,new_deck)
    

