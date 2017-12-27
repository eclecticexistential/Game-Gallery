import black_jack

def play_black_jack():
    myDeck = black_jack.deck()
    hands = black_jack.createPlayingHands(myDeck)
    dealer = hands[0]
    player = hands[1]
    black_jack.play_BJ(dealer, player, myDeck)

play_black_jack()