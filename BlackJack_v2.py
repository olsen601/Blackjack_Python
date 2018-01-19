import random

def deck_generator():
    deck = []
    card_value = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    card_suit = ['Clubs','Diamonds','Hearts','Spades']

    for csuit in card_suit:
        for cvalue in card_value:
            card = ""+cvalue+" of "+csuit+""
            deck.append(card)

    return deck

def deck_shuffler(deck):
    for i in range(0, len(deck)-1):
        index = random.randint(i, len(deck)-1)
        deck[index], deck[i] = deck[i], deck[index]

    return deck

def maximum_shuffle(deck):
    #shuffles the number of times specified in the secound parameter of the range
    for i in range(0, 7):
        deck = deck_shuffler(deck)

    return deck

deck = maximum_shuffle(deck_generator())

def deal_card():
    try:
        card = deck.pop(0)
    except IndexError as err:
        msg = ("Out of Cards")
        display_banner(msg)
        print(err)

    return card

def hand():
    cards = []

    for i in range(0,2):
        newCard = deal_card()
        cards.append(newCard)

    return cards

def score(hand):
    evaluationDeck = {}
    card_value = {'Ace': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
    card_suit = ['Clubs','Diamonds','Hearts','Spades']

    for suit in card_suit:
        for key,value in zip(card_value.keys(), card_value.values()):
            card = {""+key+" of "+suit+"": value}
            evaluationDeck.update(card)

    total = 0
    Hand = hand

    for key, value in evaluationDeck.items():
        if key in Hand:
            total += int(value)

    allAces = 0

    for suit in card_suit:
        Ace = "Ace of "+suit
        allAces += Hand.count(Ace)

    if allAces >= 1 and total <= 11:
        total += 10

    return total

def hit(Hand):
    cards = Hand
    newCard = deal_card()

    cards.append(newCard)

    return cards

def evaluate(dealerHand, playerHand):
    dealerScore = score(dealerHand)
    playerScore = score(playerHand)
    msg = ""
    scored = False

    while scored == False:
        if dealerScore < 17 and playerScore <= 21 and dealerScore != 0:
            dealerHand = hit(dealerHand)
            display(dealerHand, playerHand, True)
            dealerScore = score(dealerHand)
        elif dealerScore > 21:
            msg = "Dealer Busts, Player Wins"
            scored = True
        elif dealerScore > playerScore:
            msg = "Dealer Wins"
            scored = True
        elif dealerScore == playerScore:
            msg = "Push, Dealer Wins"
            scored = True
        elif dealerScore < playerScore and playerScore <= 21:
            msg = "Player Wins"
            scored = True
        elif playerScore > 21:
            msg = "Player Busts, Dealer Wins"
            scored = True

    return msg

def blackjack(dealerHand, playerHand):
    dealerScore = score(dealerHand)
    playerScore = score(playerHand)
    msg = ""

    if playerScore == 21 and len(playerHand) == 2:
        msg = "Player BlackJack"

    return msg

def display(dealerHand, playerHand, scored):
    if scored == False:
        print("\n","Dealers Hand: ")
        for i in range(1, len(dealerHand)):
            print(" [",dealerHand[i],"]")
        print("\n","Your Hand: ","\n",playerHand,"\n")
    elif scored == True:
        print("\n","Dealers Hand: ","\n",dealerHand,"\n","\n","Your Hand: ","\n",playerHand,"\n")

def display_banner(msg):
    '''Display Result Message'''
    message = msg
    stars = '*' * len(message)
    print('\n', stars, '\n', message, '\n', stars, '\n')

def game():
    play = True

    while len(deck) >= 4 and play == True:
        dealerHand = hand()
        playerHand = hand()
        bjcheck = blackjack(dealerHand,playerHand)
        scored = False

        while scored == False:

            display(dealerHand, playerHand, scored)

            if bjcheck == "Player BlackJack":
                display_banner(bjcheck)
                scored = True
            elif bjcheck == "":
                playerHit = input("Would you like to hit(y/n): ")
                if playerHit == "y" or playerHit == "Y":
                    playerHand = hit(playerHand)
                    s = 0
                    s = score(playerHand)
                    if s > 21:
                        msg = "Player Busts"
                        display(dealerHand, playerHand, True)
                        display_banner(msg)
                        scored = True
                elif playerHit == "n" or playerHit == "N":
                    display(dealerHand, playerHand, True)
                    msg = evaluate(dealerHand, playerHand)
                    display_banner(msg)
                    scored = True

        playAgain = input("Would you like to play again(y/n): ")
        if playAgain == "n" or playAgain == "N":
            play = False
        elif playAgain == "y" or playAgain == "Y":
            if len(deck) < 4:
                print("Out of Cards")
                play = False

def main():
    game()

main()
