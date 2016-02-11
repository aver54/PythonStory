
explore = {"look around","explore", "look", "adventure","search", "EXPLORE", "investagate", "Explore"}
stand = {"sit","Do nothing", "do nothing", "STAND"}
yes = {'yup', 'yea', 'Yes', 'yeah', 'si'}
no = {'naw', 'No','nope', 'nay'}
walk = {'walk away', 'WALK', 'go away', 'Walk'}
open = {'open','open the door', 'OPEN'}


def story():
    print "The Asylum"
    print "By Avery Fischer and Ryan Baraloto."
    print "You have woken up in a abandend asylum."
    print "What course of action would you like to take? Explore or Do nothing."
    action = raw_input("What do you want to do?(Explore/Nothing)")
    if action in explore:
        print 'You explore the asylum, you hear screaming, do you chose to investigate?'
        action = raw_input("(yes or No)")
    elif action in no:
        print "You choose not to investagate the screaming"
        if action in yes:
            print 'You choose to investigate the screaming, you find that the screamimg is behind a locked door.'
            action = raw_input("Open the door or walk away?")
            if action in
    elif action in stand:
        print 'You chose to sit where you have woken, you hear a faint screaming.'
        action = raw_input()

story()