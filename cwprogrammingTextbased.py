import random

##buidling classes
class Building:
    ##constructor
    def __init__(self):
        self.floors = 20
        ##building creates lifts
        self.l1 = Lift()
        self.l2 = Lift()
        self.l1Time = []
        self.l2Time = []

    ##methods

    ##What lift and return waiting time
    def whatLift(self, startFloor):
        
        equalLift = random.randint(0, 1)
        
        distL1 = abs(startFloor - self.l1.position)
        distL2 = abs(startFloor - self.l2.position)

        print(self.l2.efficiency)
        print(self.l1.efficiency)

        timeTaken = 0
        
        ##equal lift
        if distL1 == distL2:
            if equalLift == 1:
                if distL2== 0:
                    timeTaken = 0.0
                else:
                    timeTaken = float(((distL2 * 2) + 5) * self.l2.efficiency)
                self.l2.setFloor(startFloor)
                self.l2Time.append(timeTaken)
            else:
                if distL1 == 0:
                    timeTaken = 0.0
                else:
                    timeTaken = float((distL1 * 2) + 5 * self.l1.efficiency)
                self.l1.setFloor(startFloor)
                self.l1Time.append(timeTaken)
        ##diff lift
        elif distL1 > distL2:
            if distL2 == 0:
                timeTaken = 0.0
            else:
                timeTaken = float(((distL2 * 2) + 5) * self.l2.efficiency)
            self.l2.setFloor(startFloor)
            self.l2Time.append(timeTaken)
        else:
            if distL1 == 0:
                timeTaken = 0.0
            else:
                timeTaken = float((distL1 * 2) + 5 * self.l1.efficiency)
            self.l1.setFloor(startFloor)
            self.l1Time.append(timeTaken)
            
        return timeTaken

    ##change lift to dest
    def goDestination(self, startFloor, destination):

        if startFloor == self.l1.position:
            self.l1.setFloor(destination)
        else:
            self.l2.setFloor(destination)

    ##Eff
    def changeEfficiency(self, effChoise):
        if effChoise == 1:
            print('change the efficiency to: ')
            self.l1.setEfficiency(float(input()))
        elif effChoise == 2:
            print('change the efficiency to: ')
            self.l2.setEfficiency(float(input()))
        else:
            pass

    ##Time average
    def timeAverage(self, listAv):
        return sum(listAv) / len(listAv)

##lift classes   
class Lift:
    ##constructor
    def __init__(self):
        self.position = 1
        self.efficiency = 1            
    
    ##sets
    def setFloor(self, newFloor):
        self.position = newFloor

    def setEfficiency(self, difEff):
        self.efficiency = difEff

    

##making object
build = Building()

##variables
startfloor = 0
destination = 0
effChoice = 0

while (effChoice < 3):
    print('Do you want to change the efficiency of the lifts? \n press (1) to change lift 1 \n press (2) to change lift 2 \n press (3) to not change')
    effChoice = float(input())
    build.changeEfficiency(effChoice)

##loop or not
print("do you want to loop the next sequence? \n press (1) if you do not want to loop \n press (2) if you want to loop")
if int(input()) == 1:
    
    ##startfloor request
    print('Press what floor you are on')
    startFloor = int(input())
    while startFloor > build.floors:
        print('ERROR \n this number is to high (max {0}) \n Press what floor you are on'.format(build.floors))
        startFloor = int(input())
    print('The lift takes {0} seconds to arrive at floor {1}'.format(build.whatLift(startFloor), startFloor))

    print('position lift1: ', build.l1.position)
    print('position lift2: ', build.l2.position)

    ##startfloor to destination
    print('Press what floor you want to go to')
    destination = int(input())
    while destination > build.floors:
        print('ERROR \n this number is to high (max {0}) \n Press what floor you want to go to'.format(build.floors))
        destination = int(input())
    while destination == startFloor:
        destination = random.randint(1, build.floors)
    build.goDestination(startFloor, destination)
    print('You have arrived at floor {0}'.format(destination))

    print('position lift1: ', build.l1.position)
    print('position lift2: ', build.l2.position)
        
else:
    print("how many times?")
    loop = input()
    i = 0
    while i < int(loop):
        i +=1        
        ##startfloor request
        print("#", i)
        print('Press what floor you are on')
        startFloor = random.randint(1, build.floors)
        print(startFloor)
        print('The lift takes {0} seconds to arrive at floor {1}'.format(build.whatLift(startFloor), startFloor))

        ##startfloor to destination
        print('Press what floor you want to go to')
        destination = random.randint(1, build.floors)
        while destination == startFloor:
            destination = random.randint(1, build.floors)
        build.goDestination(startFloor, destination)
        print('You have arrived at floor {0}'.format(destination))
    print("Lift 1 took on average of {0} seconds to arrive at the startfloor \nLift 2 took on average of {1} seconds to arrive at the startfloor \n".format(round(build.timeAverage(build.l1Time),2),round(build.timeAverage(build.l2Time),2)))



                                            
         

