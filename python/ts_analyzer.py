from Tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import build_database as bd
import get_data as q
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



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
		canvas.create_text(width/2, height/3, text="Select an image to analyze", font="Helvetica 24")
		canvas.create_text(width/2, height/2, text=canvas.data.imageName, font="Helvetica 18")
		canvas.data.rectWidth = 100
		rectWidth = canvas.data.rectWidth
		canvas.create_rectangle(width/2-rectWidth/2, 2*height/3-50, width/2+rectWidth/2, 2*height/3, fill = '#D64937', outline="#D64937")
		canvas.create_text(width/2, 2*height/3-22, text="BROWSE", font="Helvetica 14", fill="white")
		if canvas.data.imageName != "":
			canvas.create_rectangle(width/2-rectWidth/2, 3*height/4, width/2+rectWidth/2, 3*height/4+50, fill = '#49BC54', outline="#49BC54")
			canvas.create_text(width/2, 3*height/4+25, text="DONE", font="Helvetica 18", fill="white")
    else:
		canvas.create_text(width/2, height/3, text=canvas.data.image, font="Arial 24")

def drawGraph():
    global ax, toolbar, graph
    #graph stuff
    try:
    	ax = fig.add_subplot(111)
    	ax.set_xlabel('time')
    	ax.set_ylabel('Work amount')
    	y = canvas.data.y
    	x = canvas.data.x
    	rect = ax.bar(x, y, width = 0.9, color = 'r')
    	#canvas.data.done = True
    	print x
    	if(canvas.data.done == False):    	
    		graph = FigureCanvasTkAgg(fig, master=canvas)
    	graph.show()
    	if(canvas.data.done == False):
    		graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    	if(canvas.data.done == False):
    		toolbar = NavigationToolbar2TkAgg( graph, canvas )
    	toolbar.update()
    	if(canvas.data.done == False):
    		canvas.data.done = True
    		graph._tkcanvas.pack(side=TOP, fill=BOTH, expand=1) 
    except:
    	pass
    	
def reset():
    canvas.data.year = (canvas.data.minYear, canvas.data.maxYear)
    canvas.data.month = (1, 12)
    canvas.data.weekDay = (0,6)
    canvas.data.day = (1, 31)
    canvas.data.hour = (1, 24)

def getYear():
    reset()
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, 0, array)
    try:
    	fig.clear()
    except:
    	pass
    drawGraph()

def getMonth():
    reset()
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, 1, array)
    fig.clear()
    drawGraph()

def getWeek():
    reset()
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, 2, array)
    fig.clear()
    drawGraph()

def getDay():
    reset()
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, 3, array)
    fig.clear()
    drawGraph()

def getHour():
    reset()
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, 4, array)
    fig.clear()
    drawGraph()

def _quit():
    canvas.data.year = (int(canvas.data.yMin.get()), int(canvas.data.yMax.get()))
    canvas.data.month = (int(canvas.data.mMin.get()), int(canvas.data.mMax.get()))
    canvas.data.week = (int(canvas.data.wMin.get()), int(canvas.data.wMax.get()))
    canvas.data.day = (int(canvas.data.dMin.get()), int(canvas.data.dMax.get()))
    canvas.data.hour = (int(canvas.data.hMin.get()), int(canvas.data.hMax.get()))
    array = [canvas.data.year, canvas.data.month, canvas.data.weekDay, canvas.data.day, canvas.data.hour]
    (canvas.data.x, canvas.data.y) = q.getTimeStampValues(canvas.data.imageName, canvas.data.radio.get(), array)
    fig.clear()
    drawGraph()
    r.destroy()

def getRange():
    canvas.data.range = True
    global r
    r = Toplevel()
    width = 250
    height = 200
    c = Canvas(r, width=width, height=height)
    c.pack()
    
    w = Label(c, text="Sort by:")
    w.grid(row=0, column=4)
    v = IntVar()
    
    Radiobutton(c, text="", variable=v, value=0).grid(row=1, column=4)
    Radiobutton(c, text="", variable=v, value=1).grid(row=3, column=4)
    Radiobutton(c, text="", variable=v, value=2).grid(row=5, column=4)
    Radiobutton(c, text="", variable=v, value=3).grid(row=7, column=4)
    Radiobutton(c, text="", variable=v, value=4).grid(row=9, column=4)
    canvas.data.radio = v

    w = Label(c, text="Pick year range:")
    w.grid(row=0, columnspan=4)

    w = Label(c, text="Pick month range:")
    w.grid(row=2, columnspan=4)

    w = Label(c, text="Pick day of week range:")
    w.grid(row=4, columnspan=4)

    w = Label(c, text="Pick day range:")
    w.grid(row=6, columnspan=4)

    w = Label(c, text="Pick hour range:")
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
    canvas.data.yMin = yearMin

    yearMax = StringVar(c)
    yearMax.set(canvas.data.maxYear)
    yearMaxOpt = apply(OptionMenu, (c, yearMax) + tuple(range(canvas.data.minYear, canvas.data.maxYear+1)))
    yearMaxOpt.grid(row=1, column=3)
    canvas.data.yMax = yearMax

    monthMin = StringVar(c)
    monthMin.set(1)
    monthMinOpt = apply(OptionMenu, (c, monthMin) + tuple(range(1, 12)))
    monthMinOpt.grid(row=3, column=1)
    canvas.data.mMin = monthMin

    monthMax = StringVar(c)
    monthMax.set(12)    
    monthMaxOpt = apply(OptionMenu, (c, monthMax) + tuple(range(1, 12)))
    monthMaxOpt.grid(row=3, column=3)
    canvas.data.mMax = monthMax

    weekMin = StringVar(c)
    weekMin.set(0)    
    weekMinOpt = apply(OptionMenu, (c, weekMin) + tuple(range(0, 6)))
    weekMinOpt.grid(row=5, column=1)
    canvas.data.wMin = weekMin

    weekMax = StringVar(c)
    weekMax.set(6)       
    monthMaxOpt = apply(OptionMenu, (c, weekMax) + tuple(range(0, 6)))
    monthMaxOpt.grid(row=5, column=3)
    canvas.data.wMax = weekMax

    dayMin = StringVar(c)
    dayMin.set(1)    
    dayMinOpt = apply(OptionMenu, (c, dayMin) + tuple(range(1, 32)))
    dayMinOpt.grid(row=7, column=1)
    canvas.data.dMin = dayMin    

    dayMax = StringVar(c)
    dayMax.set(31)       
    dayMaxOpt = apply(OptionMenu, (c, dayMax) + tuple(range(1, 32)))
    dayMaxOpt.grid(row=7, column=3)
    canvas.data.dMax = dayMax

    hourMin = StringVar(c)
    hourMin.set(1)    
    hourMinOpt = apply(OptionMenu, (c, hourMin) + tuple(range(1, 25)))
    hourMinOpt.grid(row=9, column=1)
    canvas.data.hMin = hourMin

    hourMax = StringVar(c)
    hourMax.set(24)       
    hourMaxOpt = apply(OptionMenu, (c, hourMax) + tuple(range(1, 25)))
    hourMaxOpt.grid(row=9, column=3)
    canvas.data.hMax = hourMax

    doneButton = Button(master=c, text='Done', command=_quit)
    doneButton.grid(row=10, columnspan = 4)
    
def goHome():
	canvas.data.init = True
	canvas.data.buttons.destroy
	canvas.data.graph._tkcanvas.destroy
	canvas.data.graph.get_tk_widget().destroy

def getHelp():
	global h
	h = Toplevel()
	width = 250
	height = 200
	c = Canvas(h, width=width, height=height)
	c.pack()
	
def first():
	global fig
	canvas.data.init = False
	
	#call adam's code, for now, my test code for adam's code
	timestamps = bd.testCaller()
	
	#call darren's code
	(min_year, max_year) = bd.insert_timestamps(canvas.data.imageName.split(".")[0], timestamps)
	canvas.data.minYear = min_year
	canvas.data.maxYear = max_year
	
	
	fig = plt.figure()
	
	getYear()
	
	
	
def done():
    #buttons
    buttons = Canvas(canvas, width=canvas.data.width, height=50)
    buttons.pack(side=BOTTOM, fill=BOTH, expand=1)
    button = Button(master=buttons, text='Help', command=getHelp)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Year', command=getYear)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Month', command=getMonth)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Day of Week', command=getWeek)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Day', command=getDay)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Hour', command=getHour)
    button.pack(side=LEFT)
    button = Button(master=buttons, text='Pick Range', command=getRange)
    button.pack(side=LEFT)
    canvas.data.buttons = buttons
    
def browse():
    print "in browse"    
    file = tkFileDialog.askopenfile(parent=canvas,mode='rb',title='Choose an image')
    if file!=None:
        canvas.data.image = file.name
    else:
        print "none"

def mousePressed(event):
    width = canvas.data.width
    height = canvas.data.height
    if ((event.x > width/2-canvas.data.rectWidth/2) and (event.x <width/2+canvas.data.rectWidth/2)):
	    if(event.y > 2*height/3-50 and event.y < 2*height/3):
	        browse()
	    if(event.y > 3*height/4 and event.y < 3*height/4+50):
	    	first()
	        done()
    redrawAll()

def init():
    width = canvas.data.width
    height = canvas.data.height
    canvas.data.init = True
    canvas.data.range = False
    canvas.data.done = False
    canvas.data.image = ""  
    """
    canvas.data.initButtons1 = Button(canvas, text="Browse", command=browse)
    canvas.data.initButtons1.place(x=width/2, y=2*height/3)
    canvas.data.initButtons2 = Button(canvas, text="Go!", command=done) 
    canvas.data.initButtons2.place(x=width/2, y=3*height/4) 
    """

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    width = 650
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
