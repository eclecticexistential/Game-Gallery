from random import shuffle
import Gallery

def play_again():
    answer = input("Would you like to play again? ").lower()
    if answer == 'yes':
        blackJack()
    elif answer == 'no':
        Gallery.gallery()


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
        if(i[1] == 'J' or i[1] == 'Q' or i[1] == "K" or i[1] == "T"):
            myCount += 10
        elif(i[1] != "A"):
            myCount += int(i[1])
        else:
            aceCount += 1
    if(aceCount == 1 and myCount >= 10):
        myCount += 11
    elif(aceCount != 0):
        myCount += 1

    return myCount

def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []
    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while(pointCount(dealerHand) <= 16):
        dealerHand.append(myDeck.pop())

    return(dealerHand, playerHand)


def play_BJ(dealer,player,myDeck):
    while True:
        dealerCount = pointCount(dealer)
        playerCount = pointCount(player)

        print("Dealer has: ", dealer[0])
        print("Player1, you have: ", ' '.join(player))

        if(playerCount == 21):
            print("Black Jack! Player Wins!")
            play_again()
            break
        elif(dealerCount == 21):
            print("Dealer Wins With 21!")
            play_again()
            break
        elif(playerCount > 21):
            print("Player BUSTS with ", str(playerCount), " points. Dealer wins!")
            play_again()
            break
        elif(dealerCount > 21):
            print("Dealer BUSTS with ", str(dealerCount), " points. Player wins!")
            play_again()
            break

        print(playerCount,dealerCount)
        game = input("H: Hit me or S: Stand").upper()
        if(game == "H"):
            player.append(myDeck.pop())
        elif(game == "S"):
            if(playerCount > dealerCount):
                print("Player wins with ", str(playerCount), " points")
                print("Dealer has: ", str(' '.join(dealer)), " and ", str(dealerCount), " points.")
                play_again()
                break
            else:
                print("You busted with ", str(playerCount), '. Your cards : ',str(' '.join(player)) )
                print("Dealer wins!")
                print("Dealer has: ", str(' '.join(dealer)), " and ", str(dealerCount), " points.")
                play_again()
                break


def blackJack():
    myDeck = deck()
    createPlayingHands(myDeck)
    hands = createPlayingHands(myDeck)
    dealer = hands[0]
    player = hands[1]
    play_BJ(dealer, player, myDeck)