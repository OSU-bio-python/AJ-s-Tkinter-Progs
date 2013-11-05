from Tkinter import *
from time import *



class FrameObject(Frame):

    screen_width  = 500
    screen_height = screen_width
    ground_height = int(screen_height*0.4)

    def __init__(self):
        Frame.__init__(self)
        #get the canvas
        self.goblincanvas = Canvas(width=screen_width, height=screen_height, bg="#8DABC3")
        self.goblincanvas.grid()
        #make the ground
        self.goblincanvas.create_rectangle(0, ground_height, 1000, 1000, fill="#906820", outline="#906820")
        self.goblincanvas.create_line(40, 800, 20, 750, width=2, fill="#74BA44")
        self.goblincanvas.create_line(40, 800, 40, 750, width=2, fill="#74BA44")
        self.goblincanvas.create_line(40, 800, 60, 750, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 700, 230, 650, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 700, 250, 650, width=2, fill="#74BA44")
        self.goblincanvas.create_line(250, 700, 270, 650, width=2, fill="#74BA44")
        #create base goblin
        #head
        self.goblincanvas.create_oval(614, 556, 725, 634, fill="#B3CC0D", outline="#574B1B")
        #ears
        self.goblincanvas.create_polygon(631, 582, 587, 549, 609, 617, 633, 590, fill="#889820", outline="#574B1B", width=1)
        self.goblincanvas.create_polygon(705, 582, 749, 549, 727, 617, 704, 590, fill="#889820", outline="#574B1B", width=1)
        self.goblincanvas.create_oval(617, 582, 653, 590, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_oval(682, 582, 718, 590, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_oval(620, 584, 631, 589, fill="#889820", outline="#574B1B")
        self.goblincanvas.create_oval(705, 584, 716, 589, fill="#889820", outline="#574B1B")
        self.goblincanvas.create_rectangle(620, 584, 625, 589, fill="#B3CC0D", outline="#B3CC0D")
        self.goblincanvas.create_rectangle(710, 584, 716, 589, fill="#B3CC0D", outline="#B3CC0D")
        #eyes
        self.goblincanvas.create_oval(648, 591, 657, 594, fill="black")
        self.goblincanvas.create_oval(678, 591, 687, 594, fill="black")
        #body
        self.goblincanvas.create_line(668, 634, 668, 773, fill="#B3CC0D", width=4)
        #legs
        self.goblincanvas.create_line(668, 773, 645, 785, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(645, 785, 632, 823, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(668, 773, 700, 794, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(700, 794, 720, 826, fill="#B3CC0D", width=3)
        #feet
        self.goblincanvas.create_line(632, 823, 622, 824, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(720, 826, 729, 825, fill="#B3CC0D", width=3)
        #right arm (do not wave)
        self.goblincanvas.create_line(668, 668, 703, 661, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(703, 661, 684, 687, fill="#B3CC0D", width=3)
        self.goblincanvas.create_line(680, 683, 686, 690, fill="#B3CC0D", width=3)
        #left arm (wave)
        self.goblincanvas.create_line(668, 668, 634, 666, fill="#B3CC0D", width=3)
        goboarm = self.goblincanvas.create_line(634, 666, 634, 637, fill="#B3CC0D", width=3)
        gobohand = self.goblincanvas.create_line(630, 637, 639, 637, fill="#B3CC0D", width=3)
        for count in range(10):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 666, 634 - increment, 637)
            self.goblincanvas.coords(gobohand, 630 - increment, 637, 639 - increment, 637)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(20):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 666, 624 + increment, 637)
            self.goblincanvas.coords(gobohand, 620 + increment, 637, 629 + increment, 637)
            self.goblincanvas.update()
            sleep(0.05)
        for count in range(10):
            increment = 1 + count
            self.goblincanvas.coords(goboarm, 634, 666, 644 - increment, 637)
            self.goblincanvas.coords(gobohand, 640 - increment, 637, 649 - increment, 637)
            self.goblincanvas.update()
            sleep(0.05)

# Now call the frame using the mainloop
frame01 = FrameObject()
frame01.mainloop()
