Explore = {"look around","explore" "look", "adventure","search", "EXPLORE"}
stand = {"sit","Do nothing", "do nothing", "STAND"}
yes = {'yup', 'yea', 'Yes', 'yeah', 'si'}
no = {'naw', 'No','nope', 'nay'}



print "The Asylum"
print "By Avery Fischer and Ryan Baraloto."
print "You have woken up in a abandend asylum."
print "What course of action would you like to take? Explore or Do nothing."
action = raw_input("What do you want to do?(Explore/Nothing)")
if action in Explore:
    print 'You explore the asylum, you hear screaming, do you chose to investigate? (Yes or No)'
    action = raw_input()
    if action in yes:
        print 'You choose to investigate the screaming, you find that the screamimg is behind a locked door.'
elif action in stand:
    print 'You chose to sit where you have woken, you hear a faint screaming, do you investigate? (Yes or No)'
    action = raw_input()