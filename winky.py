from Tkinter import *
from time import *

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)
##  The measured screen dimensions are MAX and you should subtract 10 to see edges
##  Screen dimensions are TL = 0,0 (screen_width,screen_height) to BR = screen_width,screen_height
##  For use on multiple monitors keep the images near the top left
##  because there are no scroll bars
##  see:http://effbot.org/tkinterbook/canvas.htm
##  this is just a change
##  Removed a change on this line

class FrameObject(Frame):

    screen_width  = 500
    screen_height = screen_width


    def __init__(self):
        Frame.__init__(self)
        #get the canvas
        self.goblincanvas = Canvas(width=screen_width, height=screen_height, bg="#8DABC3")
        self.goblincanvas.grid()
        print screen_width
        #make the ground and grass
        self.goblincanvas.create_rectangle(10, 100, 1200, 600, fill="#906820", outline="#906820")
        self.goblincanvas.create_line(40, 200, 20, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(40, 200, 40, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(40, 200, 60, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 300, 230, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 300, 250, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 300, 270, 150, width=2, fill="#74BA44")
        self.goblincanvas.create_line(350, 450, 320, 300, width=3, fill="#74BA44")
        self.goblincanvas.create_line(350, 450, 350, 300, width=2, fill="#74BA44")
        self.goblincanvas.create_line(350, 450, 370, 300, width=2, fill="#74BA44")
        #self.goblincanvas.create_line(900, 300, 880, 400, width=2, fill="#74BA44")       
        #self.goblincanvas.create_line(900, 900, 900, 700, width=3, fill="#74BA44")
##        self.goblincanvas.create_line(900, 900, 930, 700, width=2, fill="#74BA44")
##        self.goblincanvas.create_line(900, 900, 860, 700, width=2, fill="#74BA44")       
##        self.goblincanvas.create_line(900, 900, 950, 700, width=3, fill="#74BA44")
        gobograss = self.goblincanvas.create_line(900, 500, 940, 300, width=3, fill="#74BA44")
        gobograss2 = self.goblincanvas.create_line(900, 500, 950, 300, width=3, fill="#74BA44")
        gobograss3 = self.goblincanvas.create_line(900, 500, 960, 300, width=3, fill="#74BA44")
        
        #create base goblin
        #head5
        self.goblincanvas.create_oval(614, 156, 725, 234, fill="#B3CC0D", outline="#574B1B")
        #ears
        self.goblincanvas.create_polygon(631, 182, 587, 149, 609, 217, 633, 190, fill="#889820", outline="#574B1B", width=1)
        self.goblincanvas.create_polygon(705, 182, 749, 149, 727, 217, 704, 190, fill="#889820", outline="#574B1B", width=1)
        self.goblincanvas.create_oval(617, 182, 653, 190, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_oval(682, 182, 718, 190, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_oval(620, 184, 631, 189, fill="#889820", outline="#574B1B")
        self.goblincanvas.create_oval(705, 184, 716, 189, fill="#889820", outline="#574B1B")
        self.goblincanvas.create_rectangle(620, 184, 625, 189, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_rectangle(710, 184, 716, 189, fill="#B3CC0D", outline="#B3CC0D")
        #eyes
        self.goblincanvas.create_oval(648, 190, 657, 194, fill="black")
        self.goblincanvas.create_oval(678, 190, 687, 194, fill="black")
        self.goblincanvas.update()
        #self.goblincanvas.create_oval(648, 590, 657, 594, fill="black")
        #self.goblincanvas.update()
        sleep(0.05)
        #body
        self.goblincanvas.create_line(668, 234, 668, 373, fill="#B3CC0D", width=4)
        #legs
        self.goblincanvas.create_line(668, 373, 645, 385, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(645, 385, 632, 423, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(668, 373, 700, 394, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(700, 394, 720, 426, fill="#B3CC0D", width=3)
        #feet
        self.goblincanvas.create_line(632, 423, 622, 424, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(720, 426, 729, 425, fill="#B3CC0D", width=3)
        #right arm (do not wave)
        self.goblincanvas.create_line(668, 268, 703, 261, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(703, 261, 684, 287, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(680, 283, 686, 290, fill="#B3CC0D", width=3)
        #left arm (wave)
        self.goblincanvas.create_line(668, 268, 634, 266, fill="#B3CC0D", width=3)
        goboarm = self.goblincanvas.create_line(634, 266, 634, 237, fill="#B3CC0D", width=3)
        gobohand = self.goblincanvas.create_line(630, 237, 639, 237, fill="#B3CC0D", width=3)
        for count in range(10):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 266, 634 - increment, 237)
            self.goblincanvas.coords(gobohand, 630 - increment, 237, 639 - increment, 237)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(20):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 266, 624 + increment, 237)
            self.goblincanvas.coords(gobohand, 620 + increment, 237, 629 + increment, 237)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(10):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 266, 644 - increment, 237)
            self.goblincanvas.coords(gobohand, 640 - increment, 237, 649 - increment, 237)
            self.goblincanvas.update()
            sleep(0.05)
        #deleteable stuff testing
        deleteable = self.goblincanvas.create_rectangle(360, 400, 550, 500, fill="#B3CC0D", outline="#B3CC0D")
        deleteabletext = self.goblincanvas.create_text(450,420, font = "arial", justify = "right", text = "Take me to your leader!")
        # note "activefill" and "state" don't work and must be for something else e.g following don't work
        #deleteabletext = self.goblincanvas.create_text(450,410, font = "arial", state = "hidden", activefill = "blue", text = "deleteme")
        self.goblincanvas.update() # seems to be needed before sleep
        sleep(2.5)
        self.goblincanvas.delete (deleteable)
        self.goblincanvas.delete (deleteabletext)
        # goblin wink
        gobowink = self.goblincanvas.create_oval(678, 190, 687, 194, fill="#B3CC0D")
        self.goblincanvas.update()
        sleep(1.15)
        gobowink = self.goblincanvas.create_oval(678, 190, 687, 194, fill="black")
        self.goblincanvas.update()
        sleep(0.15)
        # delete something test
        # self.goblincanvas.delete (deleteable)
        #  grass waving
        bladetop1 = 940
        for count in range(20):
            increment = 1 + count
            speed1 = increment*2
            coord1 = (bladetop - increment)
            self.goblincanvas.coords(gobograss, 900, 500, coord1, 300)
            self.goblincanvas.coords(gobograss2, 900, 500, 950 - increment, 300)
            self.goblincanvas.coords(gobograss3, 900, 500, 960 - increment, 300)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(20):
            increment = 1 + count
            self.goblincanvas.coords(gobograss, 900, 500, 900 + increment, 300)
            self.goblincanvas.coords(gobograss2, 900, 500, 930 + increment, 300)
            self.goblincanvas.coords(gobograss3, 900, 500, 940 + increment*1.5, 300)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(30):
            increment = 1 + count
            self.goblincanvas.coords(gobograss, 900, 500, 920 - increment, 300)
            self.goblincanvas.coords(gobograss2, 900, 500, 950 - increment*1.7, 300)
            self.goblincanvas.coords(gobograss3, 900, 500, 970 - increment, 300)
            self.goblincanvas.update()
            sleep(0.05)
        

# Now call the frame using the mainloop
frame01 = FrameObject()
frame01.mainloop()
