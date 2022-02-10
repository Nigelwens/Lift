import random
from tkinter import *

##back
################################################################################################################## 

##buidling classes
class Building:
    ##constructor
    def __init__(self):
        self.floors = 9
        ##building creates lifts
        self.l1 = Lift()
        self.l2 = Lift()

    ##methods

    ##What lift and return waiting time
    def whatLift(self, startFloor):
        
        equalLift = random.randint(0, 1)
        
        distL1 = abs(startFloor - self.l1.position)
        distL2 = abs(startFloor - self.l2.position)

        timeTaken = 0
        
        ##equal lift
        if distL1 == distL2:
            if equalLift == 1:
                if distL2== 0:
                    timeTaken = 0.0
                else:
                    timeTaken = float(((distL2 * 2) + 5) * self.l2.efficiency)
                self.l2.setFloor(startFloor)
                self.l2.setReady(1)
                self.l1.setReady(0)
            else:
                if distL1 == 0:
                    timeTaken = 0.0
                else:
                    timeTaken = float((distL1 * 2) + 5 * self.l1.efficiency)
                self.l1.setFloor(startFloor)
                self.l1.setReady(1)
                self.l2.setReady(0)
        ##diff lift
        elif distL1 > distL2:
            if distL2 == 0:
                timeTaken = 0.0
            else:
                timeTaken = float(((distL2 * 2) + 5) * self.l2.efficiency)
            self.l2.setFloor(startFloor)       
            self.l2.setReady(1)
            self.l1.setReady(0)
        else:
            if distL1 == 0:
                timeTaken = 0.0
            else:
                timeTaken = float((distL1 * 2) + 5 * self.l1.efficiency)
            self.l1.setFloor(startFloor)
            self.l1.setReady(1)
            self.l2.setReady(0)
            
        return timeTaken
    

    ##change lift to destination
    def goDestination(self, destination):
        if self.l1.ready == 1:
            print(self.l1.ready)
            self.l1.setFloor(destination)
        else:
            self.l2.setFloor(destination)

##lift classes   
class Lift:
    ##constructor
    def __init__(self):
        self.position = 1
        self.efficiency = 1
        self.ready = 0
    
    ##sets
    def setFloor(self, newFloor):
        self.position = newFloor

    def setEfficiency(self, difEff):
        self.efficiency = float(difEff.get())

    def setReady(self, startflready):
        self.ready = startflready

##front
##################################################################################################################


##window destroyer
def destroy(self):
    self.root.destroy()

build = Building()

##efficiency page
#############################

##window
effwindow=Tk()
effwindow.title = ("Efficiency")
effwindow.geometry("300x300")

effLab1 = Label(effwindow,text="BEFORE YOU START")
effLab2 = Label(effwindow,text="change the effiency:")
effLabel = Label(effwindow)

##l1 efficiency
effLab3 = Label(effwindow,text="Lift1: ")
effEntry1 = Entry(effwindow, width = 4)
effEntry1.insert(0, build.l1.efficiency)
##l2 efficiency
effLab4 = Label(effwindow,text="Lift2: ")
effEntry2 = Entry(effwindow, width = 4)
effEntry2.insert(0, build.l2.efficiency)

##button 
effButton5 = Button(effwindow, text = "done", command = lambda: [build.l1.setEfficiency(effEntry1),
                                                                 build.l2.setEfficiency(effEntry2),
                                                                 effwindow.destroy()])


##placement
effLab1.grid(row=0, column = 0, sticky = W)
effLab2.grid(row=1, column = 0, sticky = W)
effLab3.grid(row=2, column = 0, sticky = W)
effLab4.grid(row=3, column = 0, sticky = W)

effLabel.grid(row = 4)

effEntry1.grid(row=2, column = 3, sticky = W)
effEntry2.grid(row=3, column = 3, sticky = W)

effButton5.grid(row=4, column = 1)

effwindow.mainloop()

###################################################################################################################

##efficiency page
#############################
strtfloor = 1

##creation window
floorswindow=Tk()

floorswindow.geometry("300x500")

##lifts
floorlab1 = Label(floorswindow, text = "lift 1 is on: " + str(build.l1.position))
floorlab2 = Label(floorswindow, text = "lift 2 is on: " + str(build.l2.position))
floorlab1.grid(row = 0, column = 0, sticky = W)
floorlab2.grid(row = 0, column = 4, sticky = W)

floorlab3 = Label(floorswindow, text = "What floor")
floorlab4 = Label(floorswindow, text = "are you on?")
floorlab3.grid(row = 3, column = 0, sticky = W)
floorlab4.grid(row = 4, column = 0, sticky = W)

floorlab3 = Label(floorswindow, text=" ")
floorlab3.grid(row = 0, column = 2, sticky = W)

##return timetaken
floorlab5 = Label(floorswindow)
floorlab5.grid(row = build.floors+1, column = 4)
floorlab6 = Label(floorswindow)
floorlab6.grid(row = build.floors+2, column = 4)
strtfloorlab = Label(floorswindow)
strtfloorlab.grid(row = build.floors+2, column = 5)

##manipulate window methods
def updatefloor(startFloor):
    floorlab5["text"] = "it takes the lift {0}".format(build.whatLift(startFloor))
    floorlab6["text"] = "seconds to arrive at floor"
    strtfloorlab["text"] = "{0}".format(startFloor)
    floorlab1["text"] = "lift 1 is on: " + str(build.l1.position)
    floorlab2["text"] = "lift 2 is on: " + str(build.l2.position)


##button maker + methods
button = []
for i in range(build.floors):
    button.append(Button(text = str(i+1), width = 5 ,command=lambda i=i: updatefloor(i+1)))
    button[i].grid(row=build.floors-i, column=3, sticky=W)

floorlab7 = Label(floorswindow, text=" ")
floorlab7.grid(row = 10+1, column=2, sticky = W)
floorlab8 = Label(floorswindow, text=" ")
floorlab8.grid(row = 10+2, column=2, sticky = W)
floorbutton = Button(floorswindow, text="done", command = floorswindow.destroy)
floorbutton.grid(row = build.floors+3, column=3, sticky = W)
   
floorswindow.mainloop()

###################################################################################################################

##destination page
#############################

##creation window
destwindow=Tk()

destwindow.geometry("300x500")

destlab1 = Label(destwindow, text = "lift 1 is on: " + str(build.l1.position))
destlab2 = Label(destwindow, text = "lift 2 is on: " + str(build.l2.position))
destlab1.grid(row = 0, column = 1, sticky = W)
destlab2.grid(row = 0, column = 3, sticky = W)

destlab3 = Label(destwindow, text = "What floor do you")
destlab4 = Label(destwindow, text = "want to go to?")
destlab3.grid(row = 3, column = 0, sticky = W)
destlab4.grid(row = 4, column = 0, sticky = W)

destlab3 = Label(destwindow, text=" ")
destlab3.grid(row = 0, column = 2, sticky = W)

destlab5 = Label(destwindow, text=" ")
destlab5.grid(row = 10+1, column=2, sticky = W)
destbutton = Button(destwindow, text="done", command = destwindow.destroy)
destbutton.grid(row = 10+2, column=2, sticky = W)

def updatedest():
    destlab1["text"] = "lift 1 is on: " + str(build.l1.position)
    destlab2["text"] = "lift 2 is on: " + str(build.l2.position)


button = []
for i in range (10):
    button.append(Button(text = str(i+1), width = 5 ,command=lambda i=i: [build.goDestination(i+1), updatedest()]))
    button[i].grid(row=10-i, column=2, sticky=W)



    
destwindow.mainloop()
      

