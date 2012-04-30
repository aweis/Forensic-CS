from Tkinter import *

def mousePressed(event):
    redrawAll()

def keyPressed(event):
    redrawAll()

def timerFired():
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)

def init():
    pass

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=300, height=200)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
