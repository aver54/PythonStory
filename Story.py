
explore = {"look around","explore", "look", "adventure","search", "EXPLORE", "investagate", "Explore"}
stand = {"sit","Do nothing", "do nothing", "STAND", 'nothing'}
yes = {'yup', 'yea', 'Yes', 'yeah','yes', 'si'}
no = {'naw', 'No','nope', 'no', 'nay'}
walk = {'walk away', 'WALK', 'go away', 'Walk', 'leave', 'leave the man', 'leave him'}
open = {'open','open the door', 'OPEN', 'try', 'Try', 'Try to open the door', 'try to open the door'}


def story():
    print "The Asylum"
    print "By Avery Fischer and Ryan Baraloto."
    print "You have woken up in a abandend asylum."
    print "What course of action would you like to take? Explore or Do nothing."
    action = raw_input("What do you want to do?(Explore/Nothing)\n")
    if action in explore:
        print 'You explore the asylum, you hear screaming, do you chose to investigate?'
        action = raw_input("(yes or No)\n")
    if action in no:
        print "You choose not to investagate the screaming, you continue, you find your self in a dark and musty boiler room."
        action = raw_input("do you explore the dark room, or do you walk away")
    elif action in yes:
        print 'You choose to investigate the screaming, you find that the screamimg is behind a locked door.'
        action = raw_input("Try to Open the door or walk away?")
        if action in walk:
            print 'you have chosen to walk away from the door, you find your self in a dark and musty boiler room.'
            action = raw_input('Do you choose to explore or leave the room?\n')
            if action in explore:
                print "you explore the dark room, an intense smell enters you naustrals but you cant quite tell what it is, do you continue?"
                action = raw_input('explore or turn back?')
        elif action in open:
            print 'you have chosen to tey to open the door, you find a key on the ground, you open the door and find a man on a table in a straight jacket tied to the table, it is evident that the man cannot see or hear.'
            action = raw_input('Do you help the man or do you leave him alone?')
            if action in walk:
                print 'you chose to leve the man alone '
    elif action in stand:
        print 'You chose to sit where you have woken, you hear a faint screaming. do you chose to investa gate?'
        action = raw_input('Yes or No?\n')
        if action in yes:
            print 'you walk twards the sound, and you gind the screaming is behind a locked door. Try to open the door?'

story()