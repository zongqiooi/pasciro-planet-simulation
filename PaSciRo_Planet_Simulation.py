#
# Author : Ooi Zong Qi
# ID : 20067289 / 700037327
#
# PaSciRo_Planet_Simulation.py - Basic simulation of PaSciRo lifeforms for assignment, S2 2020. 
#
# Revisions: 
#
# 22/9/2019 – Base version for assignment
#

###############################
# Blue monster   = "Rock"     #
# Purple monster = "Paper"    #
# Yellow monster = "Scissors" #
###############################

import math
import time
import random
import winsound
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm 
from texttable import Texttable # "Anaconda prompt" -> "run as administor"-> "py -m pip install -U texttable"
from matplotlib.offsetbox import OffsetImage, AnnotationBbox # for visualization

winsound.PlaySound("backgroundMusic.wav", winsound.SND_LOOP|winsound.SND_ASYNC)
#winsound.PlaySound(None, winsound.SND_ASYNC) # If BGM keeps running, activate this code and press "F5" again

class lifeForms():
    def __init__ (self, x_cord, y_cord, color):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.color = color
        
class lifeForm1(lifeForms): # blue monster
    def stepChange(self, minShift, maxShift):
        # For x_movement
        if self.x_cord == 7: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.x_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.x_cord == 193:
            self.x_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.x_cord += random.randint(minShift, maxShift)
            if self.x_cord < 7:
                self.x_cord = 7 # 7 is to set at bondaries 
            elif self.x_cord > 193:
                self.x_cord = 193 # 193 is to set at boundaries 
        
        # For y_movement
        if self.y_cord == 5: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.y_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.y_cord == 94:
            self.y_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.y_cord += random.randint(minShift, maxShift)
            if self.y_cord < 5:
                self.y_cord = 5  # 5 is to set at bondaries 
            elif self.y_cord > 94:
                self.y_cord = 94  # 94 is to set at boundaries
    
class lifeForm2(lifeForms): # purple monster
    def stepChange(self, minShift, maxShift):
        # For x_movement
        if self.x_cord == 7: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.x_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.x_cord == 193:
            self.x_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.x_cord += random.randint(minShift, maxShift)
            if self.x_cord < 7:
                self.x_cord = 7 # 7 is to set at bondaries 
            elif self.x_cord > 193:
                self.x_cord = 193 # 193 is to set at boundaries 
        
        # For y_movement
        if self.y_cord == 5: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.y_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.y_cord == 94:
            self.y_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.y_cord += random.randint(minShift, maxShift)
            if self.y_cord < 5:
                self.y_cord = 5  # 5 is to set at bondaries 
            elif self.y_cord > 94:
                self.y_cord = 94  # 94 is to set at boundaries
    
class lifeForm3(lifeForms): # yellow monster
    def stepChange(self, minShift, maxShift):
        # For x_movement
        if self.x_cord == 7: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.x_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.x_cord == 193:
            self.x_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.x_cord += random.randint(minShift, maxShift)
            if self.x_cord < 7:
                self.x_cord = 7 # 7 is to set at bondaries 
            elif self.x_cord > 193:
                self.x_cord = 193 # 193 is to set at boundaries 
        
        # For y_movement
        if self.y_cord == 5: # come in and check if it is at boundaries, if it is then straight rebound - CHANGE DIRECTION
            self.y_cord += random.randint(maxShift, maxShift) # will only generate positive number "rebound to right"
        elif self.y_cord == 94:
            self.y_cord += random.randint(minShift, minShift) # will only generate negative number "rebound to left"
        else: # if not at boundaries  
            self.y_cord += random.randint(minShift, maxShift)
            if self.y_cord < 5:
                self.y_cord = 5  # 5 is to set at bondaries 
            elif self.y_cord > 94:
                self.y_cord = 94  # 94 is to set at boundaries

    
    
def introduction():
    design1 = [" __          __  _                            _        \n",
               " \ \        / / | |                          | |       \n",
               "  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___  \n",
               "   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ \n",
               "    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |\n",
               "     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ \n"]
      
    design2 = ["\t\t\t\t        _____       _____      _ _____         _____  _                  _     \n",
               "\t\t\t\t       |  __ \     / ____|    (_)  __ \       |  __ \| |                | |    \n",
               "\t\t\t\t       | |__) |_ _| (___   ___ _| |__) |___   | |__) | | __ _ _ __   ___| |_   \n",
               "\t\t\t\t       |  ___/ _` |\___ \ / __| |  _  // _ \  |  ___/| |/ _` | '_ \ / _ \ __|  \n",
               "\t\t\t\t       | |  | (_| |____) | (__| | | \ \ (_) | | |    | | (_| | | | |  __/ |_   \n",
               "\t\t\t\t       |_|   \__,_|_____/ \___|_|_|  \_\___/  |_|    |_|\__,_|_| |_|\___|\__|  \n"]
    
    for i in design1:
        print(i, end = "")
        time.sleep(0.25)
    
    for i in design2:
        print(i, end = "")
        time.sleep(0.25)
        
    input("Press Enter to Continue...")
    
    print("\n\t\t\t\t\t\t==========================================")
    print("\t\t\t\t\t\t|| Simulation of Life on PaSciRo Planet ||")
    print("\t\t\t\t\t\t==========================================")
    print("\nIn this simulation, there are 3 types of monsters in 3 different colours.")
    print("The colours of the monsters are blue, purple, and yellow.")
    input("Press Enter to Continue...") # wait for user to enter input 
    
    print("\nTo ensure a fair simulation, all of the monsters have the chance to kill each other.")
    print('The different colours of monsters obey the simple "rock-paper-scissors" rule.')
    input("Press Enter to Continue...")
    
    sentence1 = "\nThis is how the monsters look like:"
    for i in sentence1:
        time.sleep(0.1)
        print(i, end = "")
    
    sentence1 = "..."
    for i in sentence1:
        time.sleep(1)
        print(i, end = "")
    time.sleep(1)
    
    plt.gcf().set_size_inches(15, 5)
    plt.gcf().set_facecolor("Grey")
    
    plt.subplot(131)
    imageBlue = plt.imread("BlueMonster.png")
    plt.axis("off")
    plt.imshow(imageBlue)
    
    plt.subplot(132)
    imagePurple = plt.imread("PurpleMonster.png")
    plt.axis("off")
    plt.imshow(imagePurple)
    
    plt.subplot(133)
    imageYellow = plt.imread("YellowMonster.png")
    plt.axis("off")
    plt.imshow(imageYellow)
    
    plt.show()
    
    sentence2 = "\t   Blue Monster \t\t\t\t   Purple Monster \t\t\t\t     Yellow Monster\n"
    sentence3 ="\tCharacterisitc: Calm \t\t  Characterisitc: Normal \t\t    Characterisitc: Energetic\n"
    sentence4 ="\tMovement Speed: Slowest \t  Movement Speed: Moderate \t\t    Movement Speed: Fastest\n"
    sentence5 ='\tRepresentation: "Rock" \t\t  Representation: "Paper" \t\t    Representation: "Scissors"'
    
    for i in sentence2:
        print(i, end = "")
        time.sleep(0.03)
    
    for i in sentence3:
        print(i, end = "")
        time.sleep(0.03)    
    
    for i in sentence4:
        print(i, end = "")
        time.sleep(0.03)
    
    for i in sentence5:
        print(i, end = "")
        time.sleep(0.03)
    
    print("\n\nDifferent colours of monsters have different behaviours and interaction rules.")
    input("Press Enter to read about the Behaviours...")
    
    print("--------------")
    print("| Behaviours |")
    print("--------------")
    print("1) Blue monster is calm and it has the slowest speed. ")
    print('   Blue represents "Rock".\n')
    print('2) Purple monster is normal and it has a moderate speed.')
    print('   Purple represents "Paper".\n')
    print("3) Yellow monster is energetic and it has the fastest speed. ")
    print('   Yellow represents "Scissors".\n')
    input("Press Enter to read about the Interaction Rules...")
    
    print("---------------------")
    print("| Interaction Rules |")
    print("---------------------")
    print("1) There will be death and reproduction of monsters due to a certain collision.\n")
    print("2) Reproduction: When the same colours of monsters collide with each other, ")
    print("                 a new monster with the similar colour will be reproduced.\n")
    print("3) Death       : When the different colours of monsters collide with each other, ")
    print('                 the one who loses the "rock-paper-scissors" will be dead.\n')
    input("Press Enter to enter the PaSciRo Planet simulation!")
    
    for i in tqdm (range (100), desc="Loading", ascii = False, ncols = 75): 
        time.sleep(0.02) 
        
    time.sleep(0.8)    
    print("Completed!\n")
    time.sleep(1)
    
def lifeformsVisualization(cols):
    if cols == 0:
        return OffsetImage(plt.imread("BlueMonster.png"), zoom = 0.17) 
    elif cols == 1:
        return OffsetImage(plt.imread("PurpleMonster.png"), zoom = 0.17)
    else:
        return OffsetImage(plt.imread("YellowMonster.png"), zoom = 0.17)
    
def checkCollision(xvals, yvals, cols): 
    global no_Deaths 
    global no_Reproductions
    no_Deaths = 0
    no_Reproductions = 0
    no_SameCollision0 = 0
    no_SameCollision1 = 0
    no_SameCollision2 = 0
    xcopies = xvals.copy() # create a set of copies for collision checking
    ycopies = yvals.copy() 
    colcopies = cols.copy() 
    
    for x in range(len(xvals)): # cannot use POP because might not be 20 anymore 
        for y in range(len(xvals)):
            if x == y:
                pass
            else:
                distance = math.sqrt(math.pow(xvals[x] - xvals[y], 2) + (math.pow(yvals[x] - yvals[y], 2)))
                if distance < 10.9: # not very accurate
                    # 0 is rock, 1 is paper, 2 is scissors 
                    # 0 is blue, 1 is purple, 2 is yellow
                    if cols[x] == 0 and cols[y] == 1:                          # paper wins -> 1 survived
                        print("Collision detected between blue and purple! Death of blue monster at (", xvals[x], ",", yvals[x], ")!")
                        xcopies[x] = None
                        ycopies[x] = None
                        colcopies[x] = None
                    elif cols[x] == 0 and cols[y] == 2:                        # rock wins -> 0 survived 
                        print("Collision detected between blue and yellow! Death of yellow monster at (", xvals[y], ",", yvals[y], ")!")
                        xcopies[y] = None 
                        ycopies[y] = None 
                        colcopies[y] = None
                    elif cols[x] == 1 and cols[y] == 2:                        # scissors wins -> 2 survived
                        print("Collision detected between purple and yellow! Death of purple monster at (", xvals[x], ",", yvals[x], ")!")
                        xcopies[x] = None
                        ycopies[x] = None
                        colcopies[x] = None
                    elif cols[x] == cols[y]:                                   # same color so reproduce 
                        if cols[x] == 0: 
                            no_SameCollision0 += 1 
                            if no_SameCollision0 != 0 and no_SameCollision0 % 2 == 0:   # because every collision will be CHECKED twice, this is to ensure that each special collision will only add ONE lifeform (add at 2nd time, when even)
                                newX = random.randint(7, XMAX-7) # need match with initial spawn
                                newY = random.randint(5, YMAX-5)
                                print("Collision detected between blue and blue! Reproduction of blue monster at (", newX, ",", newY, ")!")
                                newcols = cols[x]
                                xcopies.append(newX)
                                ycopies.append(newY) 
                                colcopies.append(newcols)
                            else:
                                pass
                        elif cols[x] == 1: 
                            no_SameCollision1 += 1 
                            if no_SameCollision1 != 0 and no_SameCollision1 % 2 == 0:
                                newX = random.randint(7, XMAX-7)
                                newY = random.randint(5, YMAX-5)
                                print("Collision detected between purple and purple! Reproduction of purple monster at (", newX, ",", newY, ")!")
                                newcols = cols[x]
                                xcopies.append(newX)
                                ycopies.append(newY)
                                colcopies.append(newcols)
                            else:
                                pass
                        elif cols[x] == 2: 
                            no_SameCollision2 += 1 
                            if no_SameCollision2 != 0 and no_SameCollision2 % 2 == 0:
                                newX = random.randint(7, XMAX-7)
                                newY = random.randint(5, YMAX-5)
                                print("Collision detected between yellow and yellow! Reproduction of yellow monster at (", newX, ",", newY, ")!")
                                newcols = cols[x]
                                xcopies.append(newX)
                                ycopies.append(newY)
                                colcopies.append(newcols)
                            else:
                                pass
                else:
                    pass
    
    no_Deleted = [i for i in xcopies if i == None] 
    no_Deaths = len(no_Deleted) # calculate death after collision detection
    no_Reproductions = len(xcopies) - len(xvals) # calculate reproduction after collision detection
    
    if no_Deaths == 0 and no_Reproductions == 0 and flag != STEPS - 1: # output this whenever no collision, and last time also won't output this
        print("No collision detected!")
    else:
        pass
    
    xvals2 = [i for i in xcopies if i != None] # xvals2, new one 
    yvals2 = [i for i in ycopies if i != None]
    cols2 = [i for i in colcopies if i != None]
    lifeforms = np.zeros((len(xvals2), 3), dtype=int)
    
    for i in range(len(xvals2)): # cannot use POP, because might not be 20 anymore
        lifeforms [i,0] = xvals2[i]
        lifeforms [i,1] = yvals2[i]
        lifeforms [i,2] = cols2[i]
        
    return lifeforms

introduction()  
XMAX  = 200 # 200, x-axis length
YMAX  = 100 # 100, y-axis length 
print("Before the simulation starts, kindly enter some parameters for the simulation.", end = "")
POP = int(input("Please Enter the Number of Monsters (10 is most recommended): ")) 
STEPS = int(input("Please Enter the Number of Simulation Times (10 is most recommended): ")) 
lifeforms = np.zeros((POP, 3), dtype=int) # create arrays, to plot it, 3 columns, each for x, y, color
totalDeaths = 0
totalReproductions = 0
flag = 0

for i in range(POP):
    randX = random.randint(7, XMAX-7) 
    randY = random.randint(5, YMAX-5) 
    randTYPE = random.randint(0,2) # random assigns color for each points generated
    lifeforms[i,0] = randX # generate first random set of lifeforms
    lifeforms[i,1] = randY
    lifeforms[i,2] = randTYPE
    
for i in range(STEPS):
    print("\n ### TIMESTEP ", i+1, "###")
    objects = [] # list to store all objects
    for l in lifeforms: # this loop is for stepchange (update the movement of the lifeforms)
        if l[2] == 0:
            obj1 = lifeForm1(l[0], l[1], l[2]) # blue
            objects.append(obj1)
            obj1.stepChange(-1, 1)            
        elif l[2] == 1:
            obj2 = lifeForm2(l[0], l[1], l[2]) # purple 
            objects.append(obj2)
            obj2.stepChange(-6, 6)
        else:
            obj3 = lifeForm3(l[0], l[1], l[2]) # yellow 
            objects.append(obj3)
            obj3.stepChange(-15, 15)
            
    xvals = [i.x_cord for i in objects] 
    yvals = [i.y_cord for i in objects]
    cols = [i.color for i in objects]
    
    # Visualziation of Monsters
    fig, ax = plt.subplots()
    for i in range(len(xvals)):
        ab = AnnotationBbox(lifeformsVisualization(cols[i]), (xvals[i], yvals[i]), frameon = False)
        ax.add_artist(ab) 

    # Background image
    img = plt.imread("background.jpg") 
    ax.imshow(img, aspect = "auto", extent = (0,200,0,100)) # aspect prevent the graph from going rectangular, extent is to scale it 
    plt.xlim(0, XMAX)
    plt.ylim(0, YMAX)
    ax.axes.tick_params(color = "white", labelcolor = "white") 
    ax.set_title("PaSciRo Planet Simulation", color = "white") 
    fig.set_facecolor("Black")
    plt.setp(ax.spines.values(), color = "White")
    plt.show()
    
    blueNo = 0 
    purpleNo = 0
    yellowNo = 0
    
    for i in cols:
        if i == 0:
            blueNo += 1
        elif i == 1:
            purpleNo += 1
        else:
            yellowNo += 1
    
    a = Texttable()
    a.add_rows([["Types of Monsters", "Number of Monsters"], ["Blue", blueNo], ["Purple", purpleNo], ["Yellow", yellowNo], ["TOTAL", len(xvals)]])
    print(a.draw())
    print("\n### Collision Information ###")
    
    # Collision
    if flag == STEPS - 1: # last time will not check collision
        print("End of simulation! Collision is no longer considered.")
    else: # check collision every time, except the last time 
        lifeforms = checkCollision(xvals, yvals, cols) # updates the lifeforms values again for new loop
    
    if flag != STEPS - 1: # update the total value, except for the last time, no longer considered
        totalDeaths += no_Deaths 
        totalReproductions += no_Reproductions
    else:
        pass
    """
    sentence1 = "\nSaving simulation figure"
    for i in sentence1:
        time.sleep(0.1)
        print(i, end = "")
                
    sentence1 = "..."
    for i in sentence1:
        print(i, end = "")
        time.sleep(1)
    """
    fig.savefig("Results_Simulation%d.png" %(flag+1), format = "png", dpi=1200)
    print('\nCompleted! Simulation figure %d has been saved into "Results_Simulation%d.png" file!' %(flag+1, flag+1))
    """
    if flag == STEPS - 1:
        time.sleep(1)
        input("Press Enter to Continue...")
    else:
        time.sleep(1)
        input("Press Enter to See the Next Simulation...")
    """
    # Five extra options after the simulation
    if flag == STEPS - 1: 
        print("\nOptions:")
        print("A) Show the Bar Chart for the Number of Monsters Survived in Different Colours")
        print("B) Show the Table for the Total Deaths and Total Reproductions of the Monsters")
        print('C) Save the Bar Chart into a ".png" file')
        print('D) Save the Data for each monsters into a ".csv" file')
        print("E) Exit the Simulation")
        selection = input("Please Select the Option:")
        choice = selection.upper()
        
        while choice[0] != "E":
            if choice[0] == "A":
                print("Here is the Bar Chart:")
                monsters = ("Blue", "Purple", "Yellow")
                monstersNo = [blueNo, purpleNo, yellowNo]
                plt.bar(monsters, monstersNo, align = "center", alpha = 0.5, width = 0.5, color = ("Aqua", "Purple", "Yellow")) # alpha is to change color brightness
                plt.xlabel("Monsters")
                plt.ylabel("Number of Monsters")
                plt.title("Number of Monsters in Different Colours")
                ax.set_facecolor("White")
                plt.show()
                input("Press Enter to Continue...")
                
            elif choice[0] == "B":
                print("Here is the Table:")
                b = Texttable()
                b.add_rows([["Total Deaths", "Total Reproductions"], [totalDeaths, totalReproductions]])
                print(b.draw())
                print('Fun Fact: Use the "initial number of monsters" - "total deaths" + "total reproductions",')
                print('          and you will get the "TOTAL" in the last table of the simulation!')
                input("Press Enter to Continue...")
                
            elif choice[0] == "C":
                sentence1 = "Processing"
                for i in sentence1:
                    time.sleep(0.1)
                    print(i, end = "")
                    
                sentence1 = "..."
                for i in sentence1:
                    time.sleep(1)
                    print(i, end = "")
                    
                time.sleep(2)
                monsters = ("Blue", "Purple", "Yellow")
                monstersNo = [blueNo, purpleNo, yellowNo]
                plt.bar(monsters, monstersNo, align = "center", alpha = 0.5, width = 0.5, color = ("Aqua", "Purple", "Yellow")) # alpha is to change color brightness
                plt.xlabel("Monsters")
                plt.ylabel("Number of Monsters")
                plt.title("Number of Monsters in Different Colours")
                ax.set_facecolor("White")
                plt.savefig("Results_BarChart.png", format = "png", dpi=1200) # dpi is size, have to put before plt.show
                plt.close() # prevent plots from showing up after program end 
                print('\nCompleted! Bar Chart has been saved into "Results_BarChart.png" file!')
                input("Press Enter to Continue...")
                
            elif choice[0] == "D":    
                sentence1 = "Processing"
                for i in sentence1:
                    time.sleep(0.1)
                    print(i, end = "")
                    
                sentence1 = "..."
                for i in sentence1:
                    time.sleep(1)
                    print(i, end = "")
                    
                time.sleep(2)
                fileobj = open("Results_Data.csv", "w")
                fileobj.write("No., X, Y, Colour\n")
                for i in range(len(xvals)):
                    if cols[i] == 0:
                        fileobj.write(str(i+1) + "," + str(xvals[i]) + "," + str(yvals[i]) + "," + "Blue" + "\n")
                    elif cols[i] == 1:  
                        fileobj.write(str(i+1) + "," + str(xvals[i]) + "," + str(yvals[i]) + "," + "Purple" + "\n")
                    else:
                        fileobj.write(str(i+1) + "," + str(xvals[i]) + "," + str(yvals[i]) + "," + "Yellow" + "\n")
                fileobj.close()
                print('\nCompleted! Data has been saved into "Results_Data.csv" file!')
                input("Press Enter to Continue...")
                
            else:
                print("Please Enter a Valid Choice!")
                
            print("\nOptions:")
            print("A) Show the Bar Chart for the Number of Monsters Survived in Different Colours")
            print("B) Show the Table for the Total Deaths and Total Reproductions of the Monsters")
            print('C) Save the Bar Chart into a ".png" file')
            print('D) Save the Data for each monsters into a ".csv" file')
            print("E) Exit the Simulation")
            selection = input("Please Select Another Option: ")
            choice = selection.upper()
    
    flag += 1
    
    # Exit the program 
    if flag == STEPS: 
        design3 = [" _____ _                 _                          _  \n",
                   "|_   _| |               | |                        | | \n",
                   "  | | | |__   __ _ _ __ | | __  _   _  ___  _   _  | | \n",
                   "  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | | \n",
                   "  | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |_| \n",
                   "  \_/ |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| (_) \n",
                   "                                 __/ |                 \n",
                   "                                |___/                  \n"]

        for i in design3:
            print(i, end = "")
            time.sleep(0.25)
            
        time.sleep(0.5)
        print("\nThank you for using the simulation! Have a nice day!")
        winsound.PlaySound(None, winsound.SND_ASYNC) # End of the program