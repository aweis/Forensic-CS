from Tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt

def mousePressed(event):
    redrawAll()

def keyPressed(event):
    redrawAll()

def timerFired():
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def browse():
    print "in browse"
    file = tkFileDialog.askopenfile(parent=canvas,mode='rb',title='Choose an image')
    if file!=None:
        canvas.data.image = file
    else:
        print "none"

def redrawAll():
    canvas.delete(ALL)
    width = canvas.data.width
    height = canvas.data.height
    imageName = canvas.data.image.split("/")[-1]
    if(canvas.data.init):
        canvas.create_text(width/2, height/3, text="Select an image to analyze", font="Arial 24")         
        canvas.create_text(width/2, height/2, text=imageName, font="Arial 18")
    else:
      canvas.create_text(width/2, height/3, text=canvas.data.image, font="Arial 24")
    x = np.arange(0, 5, 0.1);
    y = np.sin(x)
    plt.plot(x, y) 
    canvas.data.initButtons = b

def browse():
    print "in browse"    
    file = tkFileDialog.askopenfile(parent=canvas,mode='rb',title='Choose an image')
    if file!=None:
        canvas.data.image = file.name
    else:
        print "none"

def done():
    canvas.data.init = False
    canvas.data.initButtons1.place_forget()
    canvas.data.initButtons2.place_forget()

def init():
    width = canvas.data.width
    height = canvas.data.height
    canvas.data.init = True;
    canvas.data.image = ""  
    canvas.data.initButtons1 = Button(canvas, text="Browse", command=browse)
    canvas.data.initButtons1.place(x=width/2, y=2*height/3)
    canvas.data.initButtons2 = Button(canvas, text="Go!", command=done) 
    canvas.data.initButtons2.place(x=width/2, y=3*height/4) 

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    width = 800
    height = 600
    canvas = Canvas(root, widt=width, height=height)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = width
    canvas.data.height = height
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
