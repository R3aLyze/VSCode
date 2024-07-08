#Simple Black Jack python text game

#Imports
import random

#Arrays
Cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suits = ['H', 'D', 'C', 'S']
deck = []
dealer = []
player = []

#Build Deck of Cards
def build_deck():
    for suit in Suits:
        for card in Cards:
            deck.append(f'{card}{suit}')

#Deal Card
def deal_card(p):
    p.append(deck[random.randint(0, len(deck)-1)])

#Show Hands
def show_hands(p):
    #Show Dealer's hand
    if(p == True):
        #Print Cards
        print("Dealer's Hand:")
        print(*dealer)

        print("Player's Hand:")
        print(*player)
    #Hide Dealer's second card
    else:
        #Print Cards
        print("Dealer's Hand:")
        print(dealer[0] + ' *')

        print("Player's Hand:")
        print(*player)

#Card Values
def card_value(p):
    val = 0
    aces = 0
    
    #Extract rank of each card
    temp = [x[:-1] for x in p]

    for y in temp:
        if(y == 'A'):
            aces += 1
            val += 11
        elif(y == 'J' or y == 'Q' or y == 'K'):
            val += 10
        else:
            val += int(y)
            
    while val > 21 and aces:
        val -= 10
        aces -= 1

    return val

#Play
def play():
    #Clear Hands
    player.clear()
    dealer.clear()

    #Deal card to each player
    deal_card(player)
    deal_card(dealer)
    deal_card(player)
    deal_card(dealer)

    #Check Card Values of Dealt Hands
    if(card_value(player) == 21):
        show_hands(True)
        print('BLACK JACK!')
        print('Player Wins!')
        return
    elif(card_value(dealer) == 21):
        show_hands(True)
        print('DEALER BLACK JACK!')
        print('Dealer Wins!')
    else:
        show_hands(False)

    #Prompt User
    print("=====================================")
    print("Would you like to Hit or Stay?")
    print("Please Select an Option")
    print("1. Hit")
    print("2. Stay")
    print("=====================================")
    inp = input()

    #Loop until result has been returned
    while True:
        #If player stays
        if(inp == '2'):
            #Check Card Value of dealer's hand and if it is less than 16 deal cards
            while(card_value(dealer) <= 16):
                deal_card(dealer)
            
            #Check Values
            if(card_value(dealer) > 21):
                show_hands(True)
                print('Player Wins!')
                return
            elif(card_value(dealer) == 21):
                show_hands(True)
                print('Dealer Wins!')
                return
            elif(card_value(player) > card_value(dealer)):
                show_hands(True)
                print('Player Wins!')
            else:
                show_hands(True)
                print('Dealer Wins!')
            return
        
        #If player hits
        elif(inp == '1'):
            #Deal Card and check value
            deal_card(player)
            show_hands(False)
            if(card_value(player) > 21):
                show_hands(True)
                print('Dealer Wins!')
                return
            
            #Prompt Again if less than 21
            print("=====================================")
            print("Would you like to Hit or Stay?")
            print("Please Select an Option")
            print("1. Hit")
            print("2. Stay")
            print("=====================================")
            inp = input()

        #Invalid Input
        else:
            print("ERROR: INVALID INPUT")
            print("=====================================")
            print("Would you like to Hit or Stay?")
            print("Please Select an Option")
            print("1. Hit")
            print("2. Stay")
            print("=====================================")
            inp = input()

#Starting Menu
def menu():
    #Initialize Deck
    build_deck()
    #Prompt
    print("=====================================")
    print("Welcome to BlackJack")
    print("Please Select an Option")
    print("1. Play")
    print("2. Quit")
    print("=====================================")
    inp = input()
    #Loop till quit
    while True:
        #Quit
        if(inp == '2'):
            print("Thank You! Please Come Again")
            print("=====================================")
            return
        #Play
        elif(inp == '1'):
            play()
            print("=====================================")
            print("Please Select an Option")
            print("1. Play")
            print("2. Quit")
            print("=====================================")
            inp = input()
        #Invalid Input
        else:
            print("ERROR: INVALID INPUT")
            print("=====================================")
            print("Please Select an Option")
            print("1. Play")
            print("2. Quit")
            print("=====================================")
            inp = input()

#Main
def main():
    menu()
    
main()