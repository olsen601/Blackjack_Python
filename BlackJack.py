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

def draw_card():
    card = deck.pop(0)

    return card

def deal():
    hand = []

    for i in range(0,2):
        newCard = draw_card()
        hand.append(newCard)

    return hand

def hit(currentHand):
    hand = currentHand
    newCard = draw_card()

    hand.append(newCard)

    return hand

def evaluate(hand, dealer):
    evaluationDeck = {}
    cvalue = {'Ace': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
    csuit = ['Clubs','Diamonds','Hearts','Spades']

    for s in csuit:
        for k,v in zip(cvalue.keys(), cvalue.values()):
            card = {""+k+" of "+s+"": v}
            evaluationDeck.update(card)

    evaluateHand = hand
    total = 0

    for key, value in evaluationDeck.items():
        if key in evaluateHand:
            if int(value) == 1 and dealer != True:
                AceValue = int(input('would you like this to be a 1 or 11: '))
                total = total + AceValue -1
            elif int(value) == 1 and dealer == True:
                total += 10

            total += int(value)

    return total

def compareScore(playerScore, dealerScore, dealerHand, playerHand):
    ds = dealerScore
    ps = playerScore
    scored = False

    while scored != True:
        if ps == 21 and ds != 21:
            print("Blackjack!")
            scored = True
        elif ps == 21 and ds ==21:
            print("Push")
            scored = True
        elif ds == 21 and ps != 21:
            print("Dealer Wins")
            scored = True
        elif ds < 16:
            updatedHand = hit(dealerHand)
            evaluate(updatedHand, True)
        elif ds > 21 and ps <= 21:
            print("Dealer Busted Player Wins")
            scored = True
        elif ps > 21:
            print("Player Busted Dealer Wins")
            scored = True
        elif ps == ds:
            print("Push")
            scored = True
        elif ps > ds:
            print("You win")
            scored = True
        elif ds > ps:
            print("You lose")
            scored = True

        return scored

def display(dealerHand, playerHand, scored):
    if scored == False:
        print("Dealers Hand: ")
        for i in range(1, len(dealerHand)):
            print(dealerHand[i])
        print("Your Hand: ","\n",playerHand)
    elif scored == True:
        print("Dealers Hand: ","\n",dealerHand,"\n","Your Hand: ","\n",playerHand)

def main():

    dealerHand = deal()
    playerHand = deal()
    scored = False
    hitAgain = True

    while scored != True:
        display(dealerHand, playerHand, scored)
        if hitAgain != False:
            playerHit = input("Would you like to hit(y/n): ")
        else:
            playerHit =="n"
        if playerHit == "y":
            hit(playerHand)
            display(dealerHand, playerHand, scored)
        elif playerHit == "n":
            hitAgain = False
            playerScore = evaluate(playerHand, False)
            dealerScore = evaluate(dealerHand, True)
            scored = compareScore(playerScore, dealerScore, dealerHand, playerHand)

    if scored == True:
        display(dealerHand, playerHand, scored)


main()
