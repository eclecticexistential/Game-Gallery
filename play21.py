from random import shuffle


def play_again():
    answer = input("Would you like to play again? ").lower()
    if answer == 'yes':
        play_game()
    elif answer == 'no':
        import Gallery

def deck():
    deck = []
    for suit in ["\u2660", "\u2661", "\u2662", "\u2663"]:
        for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            deck.append(suit+rank)
    shuffle(deck)
    return deck

def pointCount(myCards):
    myCount = 0
    aceCount = 0
    for i in myCards:
        if i[1] == 'J' or i[1] == 'Q' or i[1] == "K" or i[1] == "T":
            myCount += 10
        elif i[1] != "A":
            myCount += int(i[1])
        else:
            aceCount += 1
    if aceCount == 1 and myCount >= 10:
        myCount += 1
    elif aceCount >= 2 and myCount > 21:
        myCount -= 11
    elif aceCount != 0:
        myCount += 11

    return myCount

def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []
    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while pointCount(dealerHand) <= 16:
        dealerHand.append(myDeck.pop())

    return dealerHand, playerHand


def play_BJ(dealer,player,myDeck):
    while True:
        dealerCount = pointCount(dealer)
        playerCount = pointCount(player)

        print("Dealer has: ", dealer[0])
        print("You have: {} \n".format(' '.join(player)))

        if playerCount == 21:
            print("Black Jack! You Win!")
            play_again()
            break
        elif dealerCount == 21:
            print("Dealer Wins With 21!")
            play_again()
            break
        elif playerCount > 21:
            print("Player BUSTS with {} points. Dealer wins!".format(playerCount))
            play_again()
            break
        elif dealerCount > 21:
            print("Dealer BUSTS with {} points. You win!".format(dealerCount))
            play_again()
            break

        game = input("H: Hit me or S: Stand").upper()
        if game == "H":
            player.append(myDeck.pop())
        elif game == "S":
            if playerCount > dealerCount:
                print("Player wins with {} points.".format(playerCount))
                print("Dealer has: {} points with {}.".format(dealerCount,' '.join(dealer)))
                play_again()
                break
            elif playerCount == dealerCount:
                print("Dealer wins in a draw!")
                play_again()
                break
            else:
                print("You had {} with {}.".format(playerCount,' '.join(player)))
                print("Dealer wins!")
                print("Dealer has: {} points with {}".format(dealerCount,' '.join(dealer)))
                play_again()
                break


def play_game():
    myDeck = deck()
    hands = createPlayingHands(myDeck)
    dealer = hands[0]
    player = hands[1]
    play_BJ(dealer, player, myDeck)
