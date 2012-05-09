from Tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import build_database as bd
import get_data as q
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

def getYear():
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    q.getTimeStampValues(canvas.data.imageName, 0, array)

def getMonth():
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    q.getTimeStampValues(canvas.data.imageName, 1, array)

def getWeek():
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    q.getTimeStampValues(canvas.data.imageName, 2, array)

def getDay():
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    q.getTimeStampValues(canvas.data.imageName, 3, array)

def getHour():
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    q.getTimeStampValues(canvas.data.imageName, 4, array)

def _quit():
    c.quit()

def getRange():
    canvas.data.range = True
    global r
    global c
    r = Tk()
    width = 250
    height = 200
    c = Canvas(r, width=width, height=height)
    c.pack()

    w = Label(c, text="Pick year range:")
    w.grid(row=0, columnspan=4)

    w = Label(c, text="Pick year range:")
    w.grid(row=2, columnspan=4)

    w = Label(c, text="Pick year range:")
    w.grid(row=4, columnspan=4)

    w = Label(c, text="Pick year range:")
    w.grid(row=6, columnspan=4)

    w = Label(c, text="Pick year range:")
    w.grid(row=8, columnspan=4)

    w = Label(c, text="min:")
    w.grid(row=1, column=0)

    w = Label(c, text="max:")
    w.grid(row=1, column=2)

    w = Label(c, text="min:")
    w.grid(row=3, column=0)

    w = Label(c, text="max:")
    w.grid(row=3, column=2)

    w = Label(c, text="min:")
    w.grid(row=5, column=0)

    w = Label(c, text="max:")
    w.grid(row=5, column=2)

    w = Label(c, text="min:")
    w.grid(row=7, column=0)

    w = Label(c, text="max:")
    w.grid(row=7, column=2)

    w = Label(c, text="min:")
    w.grid(row=9, column=0)

    w = Label(c, text="max:")
    w.grid(row=9, column=2)

    yearMin = StringVar(c)
    yearMin.set(canvas.data.minYear)
    yearMinOpt = OptionMenu(c, yearMin, range(canvas.data.minYear, canvas.data.maxYear+1))
    yearMinOpt = apply(OptionMenu, (c, yearMin) + tuple(range(canvas.data.minYear, canvas.data.maxYear+1)))
    yearMinOpt.grid(row = 1, column=1)

    yearMax = StringVar(c)
    yearMax.set(canvas.data.maxYear)
    yearMaxOpt = apply(OptionMenu, (c, yearMax) + tuple(range(canvas.data.minYear, canvas.data.maxYear+1)))
    yearMaxOpt.grid(row=1, column=3)

    w = Label(c, text="Pick month range:")
    w.grid(row=2, columnspan=4)

    monthMin = StringVar(c)
    monthMin.set(1)
    monthMinOpt = apply(OptionMenu, (c, monthMin) + tuple(range(1, 12)))
    monthMinOpt.grid(row=3, column=1)

    monthMax = StringVar(c)
    monthMax.set(12)    
    monthMaxOpt = apply(OptionMenu, (c, monthMax) + tuple(range(1, 12)))
    monthMaxOpt.grid(row=3, column=3)

    weekMin = StringVar(c)
    weekMin.set(0)    
    weekMinOpt = apply(OptionMenu, (c, weekMin) + tuple(range(0, 6)))
    weekMinOpt.grid(row=5, column=1)

    weekMax = StringVar(c)
    weekMax.set(6)       
    monthMaxOpt = apply(OptionMenu, (c, weekMax) + tuple(range(0, 6)))
    monthMaxOpt.grid(row=5, column=3)

    dayMin = StringVar(c)
    dayMin.set(1)    
    dayMinOpt = apply(OptionMenu, (c, dayMin) + tuple(range(1, 32)))
    dayMinOpt.grid(row=7, column=1)

    dayMax = StringVar(c)
    dayMax.set(31)       
    dayMaxOpt = apply(OptionMenu, (c, dayMax) + tuple(range(1, 32)))
    dayMaxOpt.grid(row=7, column=3)

    hourMin = StringVar(c)
    hourMin.set(1)    
    hourMinOpt = apply(OptionMenu, (c, hourMin) + tuple(range(1, 25)))
    hourMinOpt.grid(row=9, column=1)

    hourMax = StringVar(c)
    hourMax.set(24)       
    hourMaxOpt = apply(OptionMenu, (c, hourMax) + tuple(range(1, 25)))
    hourMaxOpt.grid(row=9, column=3)

    doneButton = Button(master=c, text='Done', command=_quit)
    doneButton.grid(row=10, columnspan = 4)

def done():
    canvas.data.init = False
    # go to second page
    canvas.data.initButtons1.place_forget()
    canvas.data.initButtons2.place_forget()
    
    #call adam's code, for now, my test code for adam's code
    timestamps = bd.testCaller()
    
    #call darren's code
    (min_year, max_year) = bd.insert_timestamps(canvas.data.imageName.split(".")[0], timestamps)
    canvas.data.minYear = min_year
    canvas.data.maxYear = max_year

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
 
    canvas.data.year = (min_year, max_year)
    canvas.data.month = (1, 12)
    canvas.data.weekDay = (0,6)
    canvas.data.day = (1, 31)
    canvas.data.hour = (1, 24)    

    #buttons
    buttons = Canvas(canvas, width=canvas.data.width, height=50)
    buttons.pack(side=BOTTOM, fill=BOTH, expand=1)
    button = Button(master=buttons, text='Year', command=getYear)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Month', command=getMonth)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Week', command=getWeek)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Day', command=getDay)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Hour', command=getHour)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Pick Range', command=getRange)
    button.pack(side=LEFT)
    

def init():
    width = canvas.data.width
    height = canvas.data.height
    canvas.data.init = True;
    canvas.data.range = False
    canvas.data.image = ""  
    canvas.data.initButtons1 = Button(canvas, text="Browse", command=browse)
    canvas.data.initButtons1.place(x=width/2, y=2*height/3)
    canvas.data.initButtons2 = Button(canvas, text="Go!", command=done) 
    canvas.data.initButtons2.place(x=width/2, y=3*height/4) 

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    width = 700
    height = 550
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
