from Tkinter import*
from PIL import ImageTk, Image
explore = {"look around","explore", "look", "adventure","search", "EXPLORE", "investagate", "Explore", 'try to pass the figure','Try to pass the figure', 'pass'}
stand = {"sit","Do nothing", "do nothing", "STAND", 'nothing', 'sit still', }
yes = {'yup', 'yea', 'Yes', 'yeah','yes', 'si'}
no = {'naw', 'No','nope', 'no', 'nay'}
walk = {'walk away', 'WALK', 'go away', 'Walk', 'leave', 'leave the man', 'leave him'}
open = {'open','open the door', 'OPEN', 'try', 'Try', 'Try to open the door', 'try to open the door'}
help = {'help', 'help the man', 'help him'}


def story():
 root = Tk()

 canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
 canvas.grid()

 message = canvas.create_text(300,50, text='The Asylum', font=('Arial', -50))
 message = canvas.create_text(320, 100, text='By Avery Fisher and Ryan Baraloto', font=('Arial', -25))
 backdrop = canvas.create_rectangle(50,150,550,550, fill='grey', outline='#888888')
 post = canvas.create_rectangle(75, 400,60, 550, fill ='black', outline='black')
 post = canvas.create_rectangle(350, 500,60, 480, fill ='black', outline='black')
 post = canvas.create_rectangle(350, 550,325, 500, fill ='black', outline='black')
 window = canvas.create_rectangle(200, 180,80, 375, fill ='light blue', outline='black')
 window = canvas.create_rectangle(350, 180,475, 375, fill ='light blue', outline='black')
 windowbar = canvas.create_rectangle(100, 375, 110, 180, fill ='black', outline= 'black')
 windowbar = canvas.create_rectangle(142, 375, 130, 180, fill ='black', outline= 'black')
 windowbar = canvas.create_rectangle(175, 375, 165, 180, fill ='black', outline= 'black')
 windowbar = canvas.create_rectangle(450, 375, 440, 180, fill ='black', outline= 'black')
 windowbar = canvas.create_rectangle(410, 375, 420, 180, fill ='black', outline= 'black')
 windowbar = canvas.create_rectangle(380, 375, 390, 180, fill ='black', outline= 'black')
 root.mainloop()
story()
print "The Asylum"
print "By Avery Fischer and Ryan Baraloto."
print "You have woken up in a abandend asylum."
print "What course of action would you like to take? Explore or Do nothing."
root = Tk()
image = Image.open('room.jpg')
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.pack()
root.mainloop()
action = raw_input("What do you want to do?(Explore/Nothing)\n")
if action in explore:
    print 'You explore the asylum, you hear screaming, do you chose to investigate?'
    action = raw_input("(yes or No)\n")
    #DONE
    if action in no:
        root = Tk()
        image = Image.open('Black_Mold_Room.jpg')
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.pack()
        root.mainloop()
        print "You choose not to investagate the screaming, you continue, you find your self in a dark and musty boiler room."
        action = raw_input("do you explore the dark room, or do you walk away?\n")
        if action in explore:
            print 'You explore the room, as you are walking you you hear a crack in the floor, \na few moments later you fall threw the floor to your death,\n The end'
        elif action in walk:
            print 'You chose to walk away from the room, \nas you are walking away from the room, \na figure exist a room in the hallway, \nyou try to run but you trip on a pipe, \nthe figure bends down and chokes you to death.'

    #DONE
    elif action in yes:
        root = Tk()
        image = Image.open('locked.jpg')
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.pack()
        root.mainloop()
        print 'You choose to investigate the screaming, you find that the screamimg is behind a locked door.'
        action = raw_input("Try to Open the door or walk away?")
        if action in walk:
            root = Tk()
            image = Image.open('Black_Mold_Room.jpg')
            photo = ImageTk.PhotoImage(image)
            label = Label(image=photo)
            label.image = photo
            label.pack()
            root.mainloop()
            print 'you have chosen to walk away from the door, you find your self in a dark and musty boiler room.'
            action = raw_input('Do you choose to explore or leave the room?\n')
            if action in explore:
                root = Tk()
                image = Image.open('Hole_in_Barn_Floor.png')
                photo = ImageTk.PhotoImage(image)
                label = Label(image=photo)
                label.image = photo
                label.pack()
                root.mainloop()
                print "You explore the room, as you are walking you you hear a crack in the floor, \na few moments later you fall threw the floor to your death,\n The end"
            elif action in walk:
                print "You chose to walk away from the room, \nas you are walking away from the room, \na figure exist a room in the hallway, \nyou try to run but you trip on a pipe, \nthe figure bends down and chokes you to death."
        #DONE
        elif action in open:
            root = Tk()
            image = Image.open('straight.jpg')
            photo = ImageTk.PhotoImage(image)
            label = Label(image=photo)
            label.image = photo
            label.pack()
            root.mainloop()
            print 'you have chosen to try to open the door, you find a key on the ground, you open the door and find a man on a table in a straight jacket tied to the table, it is evident that the man cannot see or hear.'
            action = raw_input('Do you help the man or do you leave him alone?')
            if action in walk:
                print 'you chose to leve the man alone , as you are leaving the room, the man breaks free and stabs you to death.'
                print 'The End'
            elif action in help:
                print 'you try to help the man however, as you approch him, he breaks free from his strapps and kills you.'
                print 'The End'

#DONE
elif action in stand:
    print 'You chose to sit where you have woken, you hear a faint screaming. do you chose to investa gate?'
    action = raw_input('Yes or No?\n')
    if action in yes:
        root = Tk()
        image = Image.open('locked.jpg')
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.pack()
        root.mainloop()
        print 'you walk twards the sound, and you find the screaming is behind a locked door. Try to open the door?'
        action = raw_input('Yes or No?')
        if action in yes:
            print"you open the door just buy kicking it, once open, you trip on a slab and imply yourself on a metal rod."
            print 'the end'
        elif action in no:
            print 'You turn away from the door, as you are walking away you come to a door in the hallway with light shining threw.'
            action = raw_input('Try to open the door? (yes or no)')
            if action in yes:
                print 'You open the door with ease, the door leads to the outside world.'
                print
                print 'Congrats, you beat our game'
            elif action in no:
                root = Tk()
                image = Image.open('Hole_in_Barn_Floor.png')
                photo = ImageTk.PhotoImage(image)
                label = Label(image=photo)
                label.image = photo
                label.pack()
                root.mainloop()
                print 'You turn away from the door, as you are walking you fall threw a hole to your death.'
                print 'The end'



    #DONE
    elif action in no:
        print 'You dont investigate the screaming, it becoms louder, do you investagate?'
        action = raw_input('yes or no?\n')
        if action in no:
            print "you see a figure in the hallway shuffling twards your room, \nscreeaming uncontrolably it looks as though it sees you and is blocking your only exit."
            action = raw_input("Do you sit still or try to pass the figure?\n")
            if action in stand:
                print 'The figure approaches and it appears to be a man in a straight jacket, he walks closer, \nstill screaming he breaks lose from the jacket and starts walking faster twards you.\nTraped you make an effort to leave the room but he grabs ahold of you and strangles you to death.'
                print
                print
                print "The end"
            elif action in explore:
                print 'you make an effort to pass the figure and it grabs ahold of you and rips you in half'
                print
                print
                print "The end"
        elif action in yes:
            print "you see a figure in the hallway shuffling twards your room, \nscreeaming uncontrolably it looks as though it sees you and is blocking your only exit."
            action = raw_input("Do you sit still or try to pass the figure?\n")
            if action in stand:
                print 'The figure approaches and it appears to be a man in a straight jacket, he walks closer, \nstill screaming he breaks lose from the jacket and starts walking faster twards you.\nTraped you make an effort to leave the room but he grabs ahold of you and strangles you to death.'
                print
                print
                print "The end"
            elif action in explore:
                print 'you make an effort to pass the figure and it grabs ahold of you and rips you in half.'
                print
                print
                print "The end"





story()