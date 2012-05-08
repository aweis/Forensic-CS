from Tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import build_database as bd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

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
    canvas.data.imageName = canvas.data.image.split("/")[-1]
    if(canvas.data.init):
	canvas.create_text(width/2, height/3, text="Select an image to analyze", font="Arial 24")    	    
    	canvas.create_text(width/2, height/2, text=canvas.data.imageName, font="Arial 18")
    else:
	canvas.create_text(width/2, height/3, text=canvas.data.image, font="Arial 24")

def browse():
    print "in browse"    
    file = tkFileDialog.askopenfile(parent=canvas,mode='rb',title='Choose an image')
    if file!=None:
        canvas.data.image = file.name
    else:
        print "none"

def done():
    canvas.data.init = False
    # go to second page
    canvas.data.initButtons1.place_forget()
    canvas.data.initButtons2.place_forget()
    
    #call adam's code, for now, my test code for adam's code
    timestamps = bd.testCaller()
    
    #call darren's code
    (min_year, max_year) = bd.insert_timestamps(canvas.data.imageName.split(".")[0], timestamps)

    #call to yearly graph
    """ it should return:
         array of x values (e.g. all the years/hours...)
         array of y values
    
    setting fake ones for now.
    """
    
    #graph stuff
    y = []
    x = [1, 5, 2, 7, 3, 9, 4, 6, 8, 10]
    for i in range(0, 10):
        y += [float(i+5)]
        #x += [2000+i]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('time')
    ax.set_ylabel('Work amount')
    rect = ax.bar(x, y, width = 0.9, color = 'r')
    
    #place graph on canvas
    graph = FigureCanvasTkAgg(fig, master=canvas)
    graph.show()
    graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg( graph, canvas )
    toolbar.update()
    graph._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    
    #buttons
    buttons = Canvas(canvas, width=canvas.data.width, height=50)
    buttons.pack(side=BOTTOM, fill=BOTH, expand=1)
    button = Button(master=buttons, text='Year', command=browse)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Month', command=browse)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Week', command=browse)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Day', command=browse)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Hour', command=browse)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Pick Range', command=browse)
    button.pack(side=LEFT)
    

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
    canvas = Canvas(root, width=width, height=height)
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
