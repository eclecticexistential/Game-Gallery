import random

def convo():
    gender = input("Male or Female?")
    if gender.lower() == "male":
        print("Hey there handsome.")
        response = ["Yes.", "No.", "Maybe.", "Possibly.", "Who knows?", "Absolutely not."]
        reason = ["Why?", "What?", "Where?", "How?", "Who?"]
        sassy = ["Look at you.", "Care for more?", "Eager to tease.", "Come again?"]
        sall = ["I mean...", "Leprechauns are better.", "Sail away.", "They'll need a crane."]
        def answers():
            word = random.choice(response)
            sword = random.choice(reason)
            fight = word + " " + sword
            print(fight)
        def sass():
            option = random.choice(sassy)
            coption = random.choice(sall)
            join = option + " " + coption
            print(join)
        def theMood():
            question = input("Entertain me. ")
            word = " bar"
            if len(question) > 0:
                if word in question:
                    print("I'd love to buy you a drink at the bar ;)")
                    theMood()
                elif len(question) % 2 == 0 and question != "exit":
                    answers()
                    theMood()
                elif len(question) % 2 != 0 and question != "exit":
                    sass()
                    theMood()
                elif question == "exit":
                    print("Goodbye")
        theMood()
    elif gender.lower() == "Female":
        print("Why hello there!")
        response = ["Yes sweetie.","Not on your life.","Maybe.","Possibly dear.","Who knows?","Absolutely not."]
        reason = ["Why?", "What?", "Where?", "How?", "Who?"]
        def answers():
            word = random.choice(response)
            sword = random.choice(reason)
            fight = word + " " + sword
            print(fight)

        question = input("Ask me a question ")

        if len(question) > 0:
            if len(question) % 2 != 0:
                answers()
            elif len(question) % 2 == 0 and question != "exit":
                answers()
            elif question == "exit":
                print("Goodbye")
    else:
        print("NOOOO")
