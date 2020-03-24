# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:00:29 2020

@author: Wesley Davis
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:24:50 2020

@author: Wesley Davis
"""

import numpy as np
from Classess import Classes
from Classess import CLASSES
from Classess import epic_level
from Classess import EPIC_LEVELS
from tkinter import *

root=Tk()
root.title("Builder Version 1.0")
#root.wm_geometry("600x800")
ThisLevel=0
classcount=0
CharacterLevel={}
Class_List = []
CharacterLevel_1=0
Class_Level_1=0
CharacterLevel_2=0
Class_Level_2=0
CharacterLevel_3=0
Class_Level_3=0
CLASSES = ["BARBARIAN", "BARD", 
           "CLERIC", "DRUID",
           "FIGHTER", "MONK", 
           "PALADIN", "RANGER", 
           "ROGUE", "SORCERER", 
           "WIZARD"]
ClassStats_1 = []
ClassStats_2 = []
ClassStats_3 = []

BAB_1 = 0
FORT_1 = 0
REFLEX_1 = 0
WILL_1 = 0

BAB_2 = 0
FORT_2 = 0
REFLEX_2 = 0
WILL_2 = 0

BAB_3 = 0
FORT_3 = 0
REFLEX_3 = 0
WILL_3 = 0

BAB_E = 0
FORT_E = 0
REFLEX_E = 0
WILL_E = 0


strength = 8
str_mod = -1
dexterity = 8
dex_mod = -1
constitution = 8
con_mod = -1
intelligence = 8
int_mod = -1
wisdom = 8
wis_mod = -1
charisma = 8
cha_mod = -1

ability_points = 30

score    = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
addsub   = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
modtable = [-5,-5,-4,-4,-3,-3,-2,-2,-1,-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

INITIALCLASSSKILLPOINTS = [ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
CLASSSKILLPOINTS        = [ 2, 6, 2, 2, 2, 2, 2, 4, 8, 2, 2]
skill_points = 0
ClassChoice = []
pointtick = 0
bonus_points=0
TEST = 0
#%%
def Level_Up_1 ():
#    access class defined by option button 1
#    advance one spot on the leveling chart
#    save this array and iteration 
#    display this array and iteration
    return

def Level_Up_2 ():
    #def Level_Up(Class_Selection):
#    global Classes
#    global ThisLevel
#    global BaseLevel
#    ThisLevel+=1
#    if ThisLevel <=20:
#        ClassStats = (Classes[Class_Selection])
#        BaseLevel += ClassStats[ThisLevel,:] 
#        print (BaseLevel)
#    else:
#        print("Epic Level")
#    return
    return

def Level_Up_3 ():
    return

#%%
frame1 = LabelFrame(root, text="Classes and Alignment")
frame1.grid(row=0, column=1, sticky=W+E+N+S)

#frame2 = LabelFrame(root, text="Skill Points")
#frame2.grid(row=1, column=1, sticky=W+E+N+S)

frame3 = LabelFrame(root, text="Base_Stats")
frame3.grid(row=0, column=3, sticky=W+E+N+S)

frame4 = LabelFrame(root, text="Finish")
frame4.grid(row=0, column=5, sticky=W+E+N+S)

frame5 = LabelFrame(root, text="Feats")
frame5.grid(row=0, column=4, sticky=W+E+N+S)

frame6 = LabelFrame(root, text="Attributes")
frame6.grid(row=0, column=0, sticky=W+E+N+S)

frame7 = LabelFrame(root, text="Skills")
frame7.grid(row=0, column=2, sticky=W+E+N+S)
#%% FRAME2
#SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
#SKILL_POINT_LABEL = Label(frame2, text="Remaining")
#SKILL_POINT_LABEL.grid(row=1, column=1, sticky=W+E)

#%% FRAME 3

def pullclass1(Class_Pointer):
    global myLabel1
    global myLabel2
    global myLabel3
    global Class_Level_1
    global Class_Level_2
    global Class_Level_3
    global Class_List
    global ThisLevel
    global Check1
    global Check2
    global Check3
    global Check_List
    global CLASSES
    global ClassStats_1
    global ClassStats_2
    global ClassStats_3
    global BAB_1
    global BAB_2
    global BAB_3
    global BAB_E
            
    global FORT_1
    global FORT_2
    global FORT_3
    global FORT_E
                        
    global REFLEX_1
    global REFLEX_2
    global REFLEX_3
    global REFLEX_E
                                    
    global WILL_1
    global WILL_2
    global WILL_3
    global WILL_E
    
    global int_mod
    global skill_points
    global INITIALCLASSSKILLPOINTS
    global CLASSSKILLPOINTS
    global SKILL_POINT_VALUE
    global SPENDING_POINT_VALUE
    global ClassChoice
    global pointtick
    global bonus_points
    global BONUS_POINTS_VALUE
    global EPIC_LEVELS
    global epic_level
    global TEST
    
    if ThisLevel>=20:
        print ("checkpoint 1")
        
        epic_level+=1    
        print (epic_level)
        #ACCOUNT FOR CLASS LEVELS
        if len(Class_List)==1:#If only one class has been chosen
            if Check1 == CLASSES[Class_Pointer]:#if the class you chose is the only class that has been chosen
                ThisLevel+=1   #increase the total character level
                
                #gain one attribute point every 4 levels
                pointtick+=1   
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    #display attribute point update
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    ABILITY_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                
                # gain appropriate skill points every level
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
                #display skill point update
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                
                #gain a level in the class
                Class_Level_1+=1
                #display the name of the chosen class in the first row, 2nd column of frame 1
                myLabel1.grid_forget()
                myLabel1 = Label(frame1, text=Check1)
                myLabel1.grid(row=0, column=1, sticky=W+E)
                
                #set up height and width to update the base stats display in frame 3
                height = ThisLevel
                width = 7
                #calculate the base stat progression in epic levels
                BAB_E = EPIC_LEVELS[epic_level,0]#current epic level points to a row in list EPIC LEVELS and a specific column, the progression for that stat
                print ("checkpoint 2")#this is printed
                print (BAB_E)#value just calculated is printed
                TEST = BAB_E+BAB_1#final sum is calculated
                print (TEST)#final sum is printed
                FORT_E = EPIC_LEVELS[epic_level,1]#process is repeated for other stats
                FORT_E+=FORT_1                
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                REFLEX_E+=REFLEX_1
                WILL_E = EPIC_LEVELS[epic_level,3] 
                WILL_E+=WILL_1
                for j in range(width): #set Columns = number of stats to display
                    b = Label(frame3, text=ThisLevel)#show current level - works
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check1)#show current class - works
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)#show current class level - works
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    b = Label(frame3, text=BAB_1+BAB_E)#show standard text string - does not work. shows [] instead.
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)    #still [] 
                    print ("checkpoint 3 - the loop")                    
                print (BAB_E)
                print (BAB_1)
                print (ThisLevel)
                
            else:
                Class_List.append(CLASSES[Class_Pointer])
                Check2 = (CLASSES[Class_Pointer])
                myLabel2.grid_forget()
                myLabel2 = Label(frame1, text=Check2)
                myLabel2.grid(row=1, column=1, sticky=W+E)
                
                
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)  
                
                Class_Level_2+=1
                
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E) 
                
        elif len(Class_List)==2:
            if Check1 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                Class_Level_2+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)      
            elif Check2 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                Class_Level_2+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3]
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)      
            else: 
                Class_List.append(CLASSES[Class_Pointer])
                Check3 = (CLASSES[Class_Pointer])
                myLabel2.grid_forget()
                myLabel2 = Label(frame1, text=Check3)
                myLabel2.grid(row=1, column=1, sticky=W+E)
                ThisLevel+=1
                Class_Level_3+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3]
                                
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_3)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)                
                
                
                
                
        elif len (Class_List)==3:
            if Check1 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                Class_Level_1+=1
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check1)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)
            elif Check2 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                Class_Level_2+=1
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)
            elif Check3 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                Class_Level_3+=1
                height = ThisLevel
                width = 7
                BAB_E = EPIC_LEVELS[epic_level,0]
                FORT_E = EPIC_LEVELS[epic_level,1] 
                REFLEX_E = EPIC_LEVELS[epic_level,2] 
                WILL_E = EPIC_LEVELS[epic_level,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check3)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_3)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3+BAB_E)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3+FORT_E)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3+REFLEX_E)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3+WILL_E)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)
            else: 
                pass

        



        
                                            
    elif ThisLevel <20:   
        ClassChoice = Class_Pointer
     
        
        if len(Class_List) <1:
            Class_List.append(CLASSES[Class_Pointer])
            Check1 = Class_List[0]
            ThisLevel+=1
            pointtick+=1
            if pointtick == 4:
                bonus_points+=1                   
                pointtick = 0
                BONUS_POINTS_VALUE.grid_forget()
                BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                BONUS_POINTS_VALUE.grid(row=5, column = 7)
            else: 
                pass   
            skill_points+=INITIALCLASSSKILLPOINTS[Class_Pointer]
            if int_mod >= 1:
                skill_points+=int_mod
            else:
                pass
#            SKILL_POINT_VALUE.grid_forget()
#            SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#            SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)


            Class_Level_1+=1
            myLabel1.grid_forget()
            myLabel1 = Label(frame1, text=Check1)
            myLabel1.grid(row=0, column=1, sticky=W+E)
    
            height = ThisLevel
            width = 7
            ClassStats_1 = (Classes[CLASSES[Class_Pointer]])
            BAB_1 = ClassStats_1[Class_Level_1,0]
            FORT_1 = ClassStats_1[Class_Level_1,1] 
            REFLEX_1 = ClassStats_1[Class_Level_1,2] 
            WILL_1 = ClassStats_1[Class_Level_1,3] 
            for j in range(width): #Columns
                b = Label(frame3, text=ThisLevel)
                b.grid(row=ThisLevel, column=0, sticky=W+E)
                b = Label(frame3, text=Check1)
                b.grid(row=ThisLevel, column=1, sticky=W+E)
                b = Label(frame3, text=Class_Level_1)
                b.grid(row=ThisLevel, column=2, sticky=W+E)
                
                b = Label(frame3, text=BAB_1)
                b.grid(row=ThisLevel, column=3, sticky=W+E)
                b = Label(frame3, text=FORT_1)
                b.grid(row=ThisLevel, column=4, sticky=W+E)
                b = Label(frame3, text=REFLEX_1)
                b.grid(row=ThisLevel, column=5, sticky=W+E)
                b = Label(frame3, text=WILL_1)
                b.grid(row=ThisLevel, column=6, sticky=W+E)
    
    
            print (ThisLevel)
            print (Class_Level_1)
        elif len(Class_List)==1:
            if Check1 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_1+=1
                myLabel1.grid_forget()
                myLabel1 = Label(frame1, text=Check1)
                myLabel1.grid(row=0, column=1, sticky=W+E)
                height = ThisLevel
                width = 7
                ClassStats_1 = (Classes[CLASSES[Class_Pointer]])
                BAB_1 = ClassStats_1[Class_Level_1,0]
                FORT_1 = ClassStats_1[Class_Level_1,1] 
                REFLEX_1 = ClassStats_1[Class_Level_1,2] 
                WILL_1 = ClassStats_1[Class_Level_1,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check1)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)            
                
                    b = Label(frame3, text=BAB_1)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)            
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_1)
            else:
                Class_List.append(CLASSES[Class_Pointer])
                Check2 = (CLASSES[Class_Pointer])
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)                
                Class_Level_2+=1
                myLabel2.grid_forget()
                myLabel2 = Label(frame1, text=Check2)
                myLabel2.grid(row=1, column=1, sticky=W+E)
                height = ThisLevel
                width = 7
                ClassStats_2 = (Classes[CLASSES[Class_Pointer]])
                BAB_2 = ClassStats_2[Class_Level_2,0]
                FORT_2 = ClassStats_2[Class_Level_2,1] 
                REFLEX_2 = ClassStats_2[Class_Level_2,2] 
                WILL_2 = ClassStats_2[Class_Level_2,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)            
    
                    b = Label(frame3, text=BAB_1+BAB_2)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)   
    
                
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_2)
                pass
        elif len(Class_List)==2:
            if Check1 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_1+=1
                myLabel1.grid_forget()
                myLabel1 = Label(frame1, text=Check1)
                myLabel1.grid(row=0, column=1, sticky=W+E)
                height = ThisLevel
                width = 7
                ClassStats_1 = (Classes[CLASSES[Class_Pointer]])
                BAB_1 = ClassStats_1[Class_Level_1,0]
                FORT_1 = ClassStats_1[Class_Level_1,1] 
                REFLEX_1 = ClassStats_1[Class_Level_1,2] 
                WILL_1 = ClassStats_1[Class_Level_1,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check1)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)     
                    
                    b = Label(frame3, text=BAB_1+BAB_2)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2)
                    b.grid(row=ThisLevel, column=6, sticky=W+E) 
                    
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_1)
            elif Check2 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_2+=1
                myLabel2.grid_forget()
                myLabel2 = Label(frame1, text=Check2)
                myLabel2.grid(row=1, column=1, sticky=W+E)
                
                height = ThisLevel
                width = 7
                
                ClassStats_2 = (Classes[CLASSES[Class_Pointer]])
                BAB_2 = ClassStats_2[Class_Level_2,0]
                FORT_2 = ClassStats_2[Class_Level_2,1] 
                REFLEX_2 = ClassStats_2[Class_Level_2,2] 
                WILL_2 = ClassStats_2[Class_Level_2,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)  
                    
                    b = Label(frame3, text=BAB_1+BAB_2)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)      
                print(BAB_1)
                print(BAB_2)
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_2)
            else: 
                Class_List.append(CLASSES[Class_Pointer])
                Check3 = (CLASSES[Class_Pointer])
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_3+=1
                myLabel3.grid_forget()
                myLabel3 = Label(frame1, text=Check3)
                myLabel3.grid(row=2, column=1, sticky=W+E)
    
                ClassStats_3 = (Classes[CLASSES[Class_Pointer]])
                BAB_3 = ClassStats_3[Class_Level_3,0]
                FORT_3 = ClassStats_3[Class_Level_3,1] 
                REFLEX_3 = ClassStats_3[Class_Level_3,2] 
                WILL_3 = ClassStats_3[Class_Level_3,3] 
               
                height = ThisLevel
                width = 7
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check3)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_3)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)  
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)                   
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_3)
        elif len(Class_List)==3:
            if Check1 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_1+=1
                myLabel1.grid_forget()
                myLabel1 = Label(frame1, text=Check1)
                myLabel1.grid(row=0, column=1, sticky=W+E)
                height = ThisLevel
                width = 7            
                 
                ClassStats_1 = (Classes[CLASSES[Class_Pointer]])
                BAB_1 = ClassStats_1[Class_Level_1,0]
                FORT_1 = ClassStats_1[Class_Level_1,1] 
                REFLEX_1 = ClassStats_1[Class_Level_1,2] 
                WILL_1 = ClassStats_1[Class_Level_1,3] 
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check1)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_1)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)     
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)              
    
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_1)
            elif Check2 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_2+=1
                myLabel2.grid_forget()
                myLabel2 = Label(frame1, text=Check2)
                myLabel2.grid(row=1, column=1, sticky=W+E)
    
                height = ThisLevel
                width = 7
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check2)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_2)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)  
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3)
                    b.grid(row=ThisLevel, column=6, sticky=W+E)                              
    
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_2)          
            elif Check3 == CLASSES[Class_Pointer]:
                ThisLevel+=1
                pointtick+=1
                if pointtick == 4:
                    bonus_points+=1                   
                    pointtick = 0
                    BONUS_POINTS_VALUE.grid_forget()
                    BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
                    BONUS_POINTS_VALUE.grid(row=5, column = 7)
                else: 
                    pass   
                skill_points+=CLASSSKILLPOINTS[Class_Pointer]
                if int_mod >= 1:
                    skill_points+=int_mod
                else:
                    pass
#                SKILL_POINT_VALUE.grid_forget()
#                SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#                SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
                Class_Level_3+=1
                myLabel3.grid_forget()
                myLabel3 = Label(frame1, text=Check3)
                myLabel3.grid(row=2, column=1, sticky=W+E)
                ClassStats_3 = (Classes[CLASSES[Class_Pointer]])
                BAB_3 = ClassStats_3[Class_Level_3,0]
                FORT_3 = ClassStats_3[Class_Level_3,1] 
                REFLEX_3 = ClassStats_3[Class_Level_3,2] 
                WILL_3 = ClassStats_3[Class_Level_3,3] 
               
                height = ThisLevel
                width = 7
                for j in range(width): #Columns
                    b = Label(frame3, text=ThisLevel)
                    b.grid(row=ThisLevel, column=0, sticky=W+E)
                    b = Label(frame3, text=Check3)
                    b.grid(row=ThisLevel, column=1, sticky=W+E)
                    b = Label(frame3, text=Class_Level_3)
                    b.grid(row=ThisLevel, column=2, sticky=W+E)  
                    
                    b = Label(frame3, text=BAB_1+BAB_2+BAB_3)
                    b.grid(row=ThisLevel, column=3, sticky=W+E)
                    b = Label(frame3, text=FORT_1+FORT_2+FORT_3)
                    b.grid(row=ThisLevel, column=4, sticky=W+E)
                    b = Label(frame3, text=REFLEX_1+REFLEX_2+REFLEX_3)
                    b.grid(row=ThisLevel, column=5, sticky=W+E)
                    b = Label(frame3, text=WILL_1+WILL_2+WILL_3)
                    b.grid(row=ThisLevel, column=6, sticky=W+E) 
                print (Class_List)
                print (ThisLevel)
                print (Class_Level_2)
            else:
                print ("Only 3 Classes Allowed")
    else:
        print("Epic Level")    
        top = Toplevel()
        top.title("Epic Level")
        
        msg = Message(top, text="Epic Level")
        msg.pack()
        
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
    SPENDING_POINT_VALUE.grid_forget()
    SPENDING_POINT_VALUE = Label(frame7, text=skill_points)
    SPENDING_POINT_VALUE.grid(row=0, column=1, sticky=W+E) 

        
        
def popup():
    top = Toplevel()
    top.title("Alignment Selection")   
    LG = Button(top, text="Lawful Good", pady=3, command=lambda: ALIGNMENT(0))
    LG.grid(row=0, column=0, sticky=W+E+N+S)
    #
    NG = Button(top, text="Neutral Good", pady=3, command=lambda: ALIGNMENT(1)) 
    NG.grid(row=0, column=1, sticky=W+E+N+S)
    
    CG = Button(top, text="Chaotic Good", pady=3, command=lambda: ALIGNMENT(2)) 
    CG.grid(row=0, column=2, sticky=W+E+N+S)
    
    LN = Button(top, text="Lawful Neutral", pady=3, command=lambda: ALIGNMENT(3))
    LN.grid(row=1, column=0, sticky=W+E+N+S)
    #
    TN = Button(top, text="True Neutral", pady=3, command=lambda: ALIGNMENT(4)) 
    TN.grid(row=1, column=1, sticky=W+E+N+S)
    
    CN = Button(top, text="Chaotic Neutral", pady=3, command=lambda: ALIGNMENT(5)) 
    CN.grid(row=1, column=2, sticky=W+E+N+S)
    
    LE = Button(top, text="Lawful Evil", pady=3, command=lambda: ALIGNMENT(6))
    LE.grid(row=2, column=0, sticky=W+E+N+S)
    #
    NE = Button(top, text="Neutral Evil", pady=3, command=lambda: ALIGNMENT(7)) 
    NE.grid(row=2, column=1, sticky=W+E+N+S)
    
    CE = Button(top, text="Chaotic Evil", pady=3, command=lambda: ALIGNMENT(8)) 
    CE.grid(row=2, column=2, sticky=W+E+N+S)
    
    button = Button(top, text="Dismiss", command=top.destroy)
    button.grid(row=3, column=0, columnspan=3)
    
def ALIGNMENT(selection):
    global ALIGNMENT_RESTRICTIONS
    global alignmentlabel
    global Alignment
    global Alignment_Choice
    global count
    ALIGNMENT_RESTRICTIONS.append(Alignment[selection])
    Alignment_Choice = ALIGNMENT_RESTRICTIONS[count]
    count+=1
    alignmentlabel.grid_forget()
    alignmentlabel = Label(frame6, text=Alignment_Choice)
    alignmentlabel.grid(row=2, column=6, sticky=W+E+N+S)
    
Alignment = ["Lawful Good", "Neutral Good", "Chaotic Good",
             "Lawful Neutral", "True Neutral", "Chaotic Neutral",
             "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
count=0
Alignment_Choice = []
ALIGNMENT_RESTRICTIONS=[]
Check1 = []
Check2 = []
Check3 = []
Check_List=[Check1, Check2, Check3]

#%% FRAME 1
myLabel1 = Label(frame1, text="Awaiting Class")
myLabel1.grid(row=0, column=1, sticky=W+E)
myLabel2 = Label(frame1, text="Awaiting Class")
myLabel2.grid(row=1, column=1, sticky=W+E)
myLabel3 = Label(frame1, text="Awaiting Class")
myLabel3.grid(row=2, column=1, sticky=W+E)
alignmentlabel = Label(frame6, text="Choose Alignment")
alignmentlabel.grid(row=2, column=6)
alignmentbutton = Button(frame6, text="Choose Alignment",command = popup)
alignmentbutton.grid(row=1, column=6)




Class_List = []




Level_BARB = Button(frame1, text="Barbarian", pady=3, command=lambda: pullclass1(0))
Level_BARB.grid(row=0, column=0, sticky=W+E+N+S)
#
Level_BARD = Button(frame1, text="Bard", pady=3, command=lambda: pullclass1(1)) 
Level_BARD.grid(row=1, column=0, sticky=W+E+N+S)

Level_CLERIC = Button(frame1, text="Cleric", pady=3, command=lambda: pullclass1(2)) 
Level_CLERIC.grid(row=2, column=0, sticky=W+E+N+S)

Level_DRUID = Button(frame1, text="Druid", pady=3, command=lambda: pullclass1(3))
Level_DRUID.grid(row=3, column=0, sticky=W+E+N+S)
#
Level_FIGHTER = Button(frame1, text="Fighter", pady=3, command=lambda: pullclass1(4)) 
Level_FIGHTER.grid(row=4, column=0, sticky=W+E+N+S)

Level_MONK = Button(frame1, text="Monk", pady=3, command=lambda: pullclass1(5)) 
Level_MONK.grid(row=5, column=0, sticky=W+E+N+S)

Level_PALADIN = Button(frame1, text="Paladin", pady=3, command=lambda: pullclass1(6))
Level_PALADIN.grid(row=6, column=0, sticky=W+E+N+S)
#
Level_RANGER = Button(frame1, text="Ranger", pady=3, command=lambda: pullclass1(7)) 
Level_RANGER.grid(row=7, column=0, sticky=W+E+N+S)

Level_ROGUE = Button(frame1, text="Rogue", pady=3, command=lambda: pullclass1(8)) 
Level_ROGUE.grid(row=8, column=0, sticky=W+E+N+S)

Level_SORCERER = Button(frame1, text="Sorcerer", pady=3, command=lambda: pullclass1(9)) 
Level_SORCERER.grid(row=9, column=0, sticky=W+E+N+S)

Level_WIZARD = Button(frame1, text="Wizard", pady=3, command=lambda: pullclass1(10)) 
Level_WIZARD.grid(row=10, column=0, sticky=W+E+N+S)

#%% FRAME 3 BASE STATS
Level = Label(frame3, text="| Level |")
Level.grid(row=0, column=0, sticky=W+E+N+S)

Class_Type = Label(frame3, text="| Class |")
Class_Type.grid(row=0, column=1, sticky=W+E+N+S)

Class_Level = Label(frame3, text="| Class Level |")
Class_Level.grid(row=0, column=2, sticky=W+E+N+S)

AB = Label(frame3, text="| Base Attack Bonus |")
AB.grid(row=0, column=3, sticky=W+E+N+S)

FORT = Label(frame3, text="| Fortitude Save |")
FORT.grid(row=0, column=4, sticky=W+E+N+S)

REF = Label(frame3, text="| Reflex Save |")
REF.grid(row=0, column=5, sticky=W+E+N+S)

WILL = Label(frame3, text="| Will Save |")
WILL.grid(row=0, column=6, sticky=W+E+N+S)
#%% FRAME 4
Quit = Button(frame4, text="Save and Continue", command=root.destroy) 
Quit.grid(row=1, column=0, columnspan=2, sticky=W+E+N+S)
#%% FRAME 5

My_Feats = Label(frame5, text="My Feats")
My_Feats.pack()
#%% FRAME 6
ABILITY_POINTS = Label(frame6, text="Ability Points Remaining")
ABILITY_POINTS.grid(row=0, column = 6)
ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
ABILITY_POINTS_VALUE.grid(row=0, column = 7)

BONUS_POINTS = Label(frame6, text="Bonus Points Remaining")
BONUS_POINTS.grid(row=5, column = 6)
BONUS_POINTS_VALUE = Label(frame6, text=bonus_points)
BONUS_POINTS_VALUE.grid(row=5, column = 7)
def STRENGTH(ButtonInput):
    global strength
    global STR_VALUE
    global str_mod
    global STR_MODIFIER
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable

    if ButtonInput == 1:
        if ability_points >= addsub[strength]:
            ability_points-= addsub[strength]
            strength += ButtonInput
            str_mod = modtable[strength]
        elif ability_points < addsub[strength]:
            pass
    elif ButtonInput == -1:
            ability_points+= addsub[strength-1]
            strength += ButtonInput
            str_mod = modtable[strength]

    STR_VALUE.grid_forget()
    STR_VALUE = Label(frame6, text=strength)
    STR_VALUE.grid(row=0, column=3, sticky=W+E)
    STR_MODIFIER.grid_forget()
    STR_MODIFIER = Label(frame6, text=str_mod)
    STR_MODIFIER.grid(row=0, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7)
STR = Label(frame6, text="Strength")
STR.grid(row=0, column=1, sticky=W+E)
STR_DOWN = Button(frame6, text="Down", command=lambda: STRENGTH(-1))
STR_DOWN.grid(row=0, column=2, sticky=W+E)
STR_VALUE= Label(frame6, text=strength)
STR_VALUE.grid(row=0, column=3, sticky=W+E)
STR_UP = Button(frame6, text="Up", command=lambda: STRENGTH(1)) 
STR_UP.grid(row=0, column=4, sticky=W+E)
STR_MODIFIER = Label(frame6, text=str_mod)
STR_MODIFIER.grid(row=0, column=5, sticky=W+E)

def DEXTERITY(ButtonInput):
    global dexterity
    global DEX_VALUE
    global dex_mod
    global DEX_MODIFIER  
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable


    if ButtonInput == 1:
        if ability_points >= addsub[dexterity]:
            ability_points -= addsub[dexterity]
            dexterity += ButtonInput
            dex_mod = modtable[dexterity]
        elif ability_points < addsub[dexterity]:
            pass
    elif ButtonInput == -1:
            ability_points += addsub[dexterity-1]
            dexterity += ButtonInput
            dex_mod = modtable[dexterity]
    DEX_VALUE.grid_forget()
    DEX_VALUE = Label(frame6, text=dexterity)
    DEX_VALUE.grid(row=1, column=3, sticky=W+E)  
    DEX_MODIFIER.grid_forget()
    DEX_MODIFIER = Label(frame6, text=dex_mod)
    DEX_MODIFIER.grid(row=1, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7)
DEX = Label(frame6, text="Dexterity")
DEX.grid(row=1, column=1, sticky=W+E)
DEX_DOWN = Button(frame6, text="Down", command=lambda: DEXTERITY(-1))
DEX_DOWN.grid(row=1, column=2, sticky=W+E)
DEX_VALUE= Label(frame6, text=dexterity)
DEX_VALUE.grid(row=1, column=3, sticky=W+E)
DEX_UP = Button(frame6, text="Up", command=lambda: DEXTERITY(1)) 
DEX_UP.grid(row=1, column=4, sticky=W+E)
DEX_MODIFIER = Label(frame6, text=dex_mod)
DEX_MODIFIER.grid(row=1, column=5, sticky=W+E)

def CONSTITUTION(ButtonInput):
    global constitution
    global CON_VALUE
    global con_mod
    global CON_MODIFIER
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable
    if ButtonInput == 1:
        if ability_points >= addsub[constitution]:
            ability_points -= addsub[constitution]
            constitution += ButtonInput
            con_mod = modtable[constitution]
        elif ability_points < addsub[constitution]:
            pass
    elif ButtonInput == -1:
            ability_points += addsub[constitution-1]
            constitution += ButtonInput
            con_mod = modtable[constitution]
    CON_VALUE.grid_forget()
    CON_VALUE = Label(frame6, text=constitution)
    CON_VALUE.grid(row=2, column=3, sticky=W+E)   
    CON_MODIFIER.grid_forget()
    CON_MODIFIER = Label(frame6, text=con_mod)
    CON_MODIFIER.grid(row=2, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7)

CON = Label(frame6, text="Constitution")
CON.grid(row=2, column=1, sticky=W+E)
CON_DOWN = Button(frame6, text="Down", command=lambda: CONSTITUTION(-1))
CON_DOWN.grid(row=2, column=2, sticky=W+E)
CON_VALUE= Label(frame6, text=constitution)
CON_VALUE.grid(row=2, column=3, sticky=W+E)
CON_UP = Button(frame6, text="Up", command=lambda: CONSTITUTION(1)) 
CON_UP.grid(row=2, column=4, sticky=W+E)
CON_MODIFIER = Label(frame6, text=con_mod)
CON_MODIFIER.grid(row=2, column=5, sticky=W+E)

def INTELLIGENCE(ButtonInput):
    global intelligence
    global INT_VALUE
    global int_mod
    global INT_MODIFIER
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable
    if ButtonInput == 1:
        if ability_points >= addsub[intelligence]:
            ability_points -= addsub[intelligence]
            intelligence += ButtonInput
            int_mod = modtable[intelligence]
        elif ability_points < addsub[intelligence]:
            pass
    elif ButtonInput == -1:
            ability_points += addsub[intelligence-1]
            intelligence += ButtonInput
            int_mod = modtable[intelligence]
    INT_VALUE.grid_forget()
    INT_VALUE = Label(frame6, text=intelligence)
    INT_VALUE.grid(row=3, column=3, sticky=W+E) 
    INT_MODIFIER.grid_forget()
    INT_MODIFIER = Label(frame6, text=int_mod)
    INT_MODIFIER.grid(row=3, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7)

INT = Label(frame6, text="Intelligence")
INT.grid(row=3, column=1, sticky=W+E)
INT_DOWN = Button(frame6, text="Down", command=lambda: INTELLIGENCE(-1))
INT_DOWN.grid(row=3, column=2, sticky=W+E)
INT_VALUE= Label(frame6, text=intelligence)
INT_VALUE.grid(row=3, column=3, sticky=W+E)
INT_UP = Button(frame6, text="Up", command=lambda: INTELLIGENCE(1)) 
INT_UP.grid(row=3, column=4, sticky=W+E)
INT_MODIFIER = Label(frame6, text=int_mod)
INT_MODIFIER.grid(row=3, column=5, sticky=W+E)

def WISDOM(ButtonInput):
    global wisdom
    global WIS_VALUE
    global wis_mod
    global WIS_MODIFIER
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable
    if ButtonInput == 1:
        if ability_points >= addsub[wisdom]:
            ability_points -= addsub[wisdom]
            wisdom += ButtonInput
            wis_mod = modtable[wisdom]
        elif ability_points < addsub[wisdom]:
            pass
    elif ButtonInput == -1:
            ability_points += addsub[wisdom-1]
            wisdom += ButtonInput
            wis_mod = modtable[wisdom]
    WIS_VALUE.grid_forget()
    WIS_VALUE = Label(frame6, text=wisdom)
    WIS_VALUE.grid(row=4, column=3, sticky=W+E) 
    WIS_MODIFIER.grid_forget()
    WIS_MODIFIER = Label(frame6, text=wis_mod)
    WIS_MODIFIER.grid(row=4, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7) 
WIS = Label(frame6, text="Wisdom")
WIS.grid(row=4, column=1, sticky=W+E)
WIS_DOWN = Button(frame6, text="Down", command=lambda: WISDOM(-1))
WIS_DOWN.grid(row=4, column=2, sticky=W+E)
WIS_VALUE= Label(frame6, text=wisdom)
WIS_VALUE.grid(row=4, column=3, sticky=W+E)
WIS_UP = Button(frame6, text="Up", command=lambda: WISDOM(1)) 
WIS_UP.grid(row=4, column=4, sticky=W+E)
WIS_MODIFIER = Label(frame6, text=wis_mod)
WIS_MODIFIER.grid(row=4, column=5, sticky=W+E)

def CHARISMA(ButtonInput):
    global charisma
    global CHA_VALUE
    global cha_mod
    global CHA_MODIFIER
    global ability_points
    global ABILITY_POINTS_VALUE
    global addsub
    global modtable
    if ButtonInput == 1:
        if ability_points >= addsub[charisma]:
            ability_points -= addsub[charisma]
            charisma += ButtonInput
            cha_mod = modtable[charisma]
        elif ability_points < addsub[charisma]:
            pass
    elif ButtonInput == -1:
            ability_points += addsub[charisma-1]
            charisma += ButtonInput
            cha_mod = modtable[charisma]
    CHA_VALUE.grid_forget()
    CHA_VALUE = Label(frame6, text=charisma)
    CHA_VALUE.grid(row=5, column=3, sticky=W+E) 
    CHA_MODIFIER.grid_forget()
    CHA_MODIFIER = Label(frame6, text=cha_mod)
    CHA_MODIFIER.grid(row=5, column=5, sticky=W+E)
    ABILITY_POINTS_VALUE.grid_forget()
    ABILITY_POINTS_VALUE = Label(frame6, text=ability_points)
    ABILITY_POINTS_VALUE.grid(row=0, column = 7)   
CHA = Label(frame6, text="Charisma")
CHA.grid(row=5, column=1, sticky=W+E)
CHA_DOWN = Button(frame6, text="Down", command=lambda: CHARISMA(-1))
CHA_DOWN.grid(row=5, column=2, sticky=W+E)
CHA_VALUE= Label(frame6, text=charisma)
CHA_VALUE.grid(row=5, column=3, sticky=W+E)
CHA_UP = Button(frame6, text="Up", command=lambda: CHARISMA(1)) 
CHA_UP.grid(row=5, column=4, sticky=W+E)
CHA_MODIFIER = Label(frame6, text=cha_mod)
CHA_MODIFIER.grid(row=5, column=5, sticky=W+E)
#%% FRAME 7
animal_empathy = 0
appraise = 0
bluff = 0
concentration = 0 
craft_mastery = 0
craft_trap = 0
disable_trap = 0
discipline = 0
heal = 0
hide = 0
intimidate = 0
listen = 0
lore = 0
move_silently = 0
open_lock = 0
parry = 0
perform = 0
persuade = 0
pick_pocket = 0
ride = 0
search = 0
set_trap = 0
spot = 0
spellcraft = 0
taunt = 0
tumble = 0
use_magic_device = 0
class_skill_modifier =1
SKILLS = [animal_empathy,
          appraise,
          bluff, 
          concentration, 
          craft_mastery, 
          craft_trap,
          disable_trap,
          discipline,
          heal,
          hide,
          intimidate,
          listen,
          lore,
          move_silently,
          open_lock,
          parry,
          perform,
          persuade,
          pick_pocket,
          ride,
          search,
          set_trap,
          spellcraft,
          spot,
          taunt,
          tumble,
          use_magic_device]
barb   = [ 0, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 2, 1, 2, 0]
bard   = [ 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1]
cleric = [ 0, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 2, 1, 2, 2, 2, 0]
druid  = [ 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 0]
fighter= [ 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0]
monk   = [ 0, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 0]
paladin= [ 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 2, 2, 1, 1, 2, 0]
ranger = [ 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 1, 2, 2, 0]
rogue  = [ 0, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1]
sorcerer=[ 0, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 0]
wizard = [ 0, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0]
#          ae ap bl co cm ct dt di he hi in li lo mo op pa pe pr pi ri se st sp st ta tu um

modifier_list = [
          barb,
          bard,
          cleric, 
          druid, 
          fighter, 
          monk,
          paladin,
          ranger,
          rogue,
          sorcerer,
          wizard]

def SKILLADJ(spendskillpoint):
    global skill_points
    global SKILLS
    global SPENDING_POINT_VALUE
    global SPENDING_POINT_LABEL
    global ANIMAL_EMPATHY_VALUE
    global APPRAISE_VALUE
    global BLUFF_VALUE
    global CONCENTRATION_VALUE
    global CRAFT_MASTERY_VALUE
    global CRAFT_TRAP_VALUE
    global DISABLE_TRAP_VALUE
    global DISCIPLINE_VALUE
    global HEAL_VALUE
    global HIDE_VALUE
    global INTIMIDATE_VALUE
    global LISTEN_VALUE
    global LORE_VALUE
    global MOVE_SILENTLY_VALUE
    global OPEN_LOCK_VALUE
    global PARRY_VALUE
    global PERFORM_VALUE
    global PERSUADE_VALUE
    global PICK_POCKET_VALUE
    global RIDE_VALUE
    global SEARCH_VALUE
    global SET_TRAP_VALUE
    global SPOT_VALUE
    global SPELLCRAFT_VALUE
    global TAUNT_VALUE
    global TUMBLE_VALUE
    global UMD_VALUE
    global ClassChoice
    global class_skill_modifier
    global modifier_list
    global SKILL_POINT_VALUE
    
    class_skill_modifier = modifier_list[ClassChoice]
    
    
    if skill_points > 0:
        skill=SKILLS[spendskillpoint]
        if class_skill_modifier[spendskillpoint] == 0:
            pass
        else:
            skill_points-=class_skill_modifier[spendskillpoint]
            skill+=1
            SKILLS[spendskillpoint]=skill
    else:
        pass
    SPENDING_POINT_VALUE.grid_forget()
    SPENDING_POINT_VALUE = Label(frame7, text=skill_points)
    SPENDING_POINT_VALUE.grid(row=0, column=1, sticky=W+E)  
#    SKILL_POINT_VALUE.grid_forget()
#    SKILL_POINT_VALUE = Label(frame2, text=skill_points)
#    SKILL_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
    ANIMAL_EMPATHY_VALUE.grid_forget()
    ANIMAL_EMPATHY_VALUE= Label(frame7, text=SKILLS[0])
    ANIMAL_EMPATHY_VALUE.grid(row=1, column=1, sticky=W+E)
    APPRAISE_VALUE.grid_forget()
    APPRAISE_VALUE= Label(frame7, text=SKILLS[1])
    APPRAISE_VALUE.grid(row=2, column=1, sticky=W+E)
    BLUFF_VALUE.grid_forget()
    BLUFF_VALUE= Label(frame7, text=SKILLS[2])
    BLUFF_VALUE.grid(row=3, column=1, sticky=W+E)
    CONCENTRATION_VALUE.grid_forget()
    CONCENTRATION_VALUE= Label(frame7, text=SKILLS[3])
    CONCENTRATION_VALUE.grid(row=4, column=1, sticky=W+E)
    CRAFT_MASTERY_VALUE.grid_forget()
    CRAFT_MASTERY_VALUE= Label(frame7, text=SKILLS[4])
    CRAFT_MASTERY_VALUE.grid(row=5, column=1, sticky=W+E)
    CRAFT_TRAP_VALUE.grid_forget()
    CRAFT_TRAP_VALUE= Label(frame7, text=SKILLS[5])
    CRAFT_TRAP_VALUE.grid(row=6, column=1, sticky=W+E)
    DISABLE_TRAP_VALUE.grid_forget()
    DISABLE_TRAP_VALUE= Label(frame7, text=SKILLS[6])
    DISABLE_TRAP_VALUE.grid(row=7, column=1, sticky=W+E)    
    DISCIPLINE_VALUE.grid_forget()
    DISCIPLINE_VALUE= Label(frame7, text=SKILLS[7])
    DISCIPLINE_VALUE.grid(row=8, column=1, sticky=W+E)    
    HEAL_VALUE.grid_forget()
    HEAL_VALUE= Label(frame7, text=SKILLS[8])
    HEAL_VALUE.grid(row=9, column=1, sticky=W+E)    
    HIDE_VALUE.grid_forget()
    HIDE_VALUE= Label(frame7, text=SKILLS[9])
    HIDE_VALUE.grid(row=10, column=1, sticky=W+E)    
    INTIMIDATE_VALUE.grid_forget()
    INTIMIDATE_VALUE= Label(frame7, text=SKILLS[10])
    INTIMIDATE_VALUE.grid(row=11, column=1, sticky=W+E)
    LISTEN_VALUE.grid_forget()
    LISTEN_VALUE= Label(frame7, text=SKILLS[11])
    LISTEN_VALUE.grid(row=12, column=1, sticky=W+E)
    LORE_VALUE.grid_forget()
    LORE_VALUE= Label(frame7, text=SKILLS[12])
    LORE_VALUE.grid(row=13, column=1, sticky=W+E)
    MOVE_SILENTLY_VALUE.grid_forget()
    MOVE_SILENTLY_VALUE= Label(frame7, text=SKILLS[13])
    MOVE_SILENTLY_VALUE.grid(row=14, column=1, sticky=W+E)
    OPEN_LOCK_VALUE.grid_forget()
    OPEN_LOCK_VALUE= Label(frame7, text=SKILLS[14])
    OPEN_LOCK_VALUE.grid(row=15, column=1, sticky=W+E)
    PARRY_VALUE.grid_forget()
    PARRY_VALUE= Label(frame7, text=SKILLS[15])
    PARRY_VALUE.grid(row=16, column=1, sticky=W+E)
    PERFORM_VALUE.grid_forget()
    PERFORM_VALUE= Label(frame7, text=SKILLS[16])
    PERFORM_VALUE.grid(row=17, column=1, sticky=W+E)    
    PERSUADE_VALUE.grid_forget()
    PERSUADE_VALUE= Label(frame7, text=SKILLS[17])
    PERSUADE_VALUE.grid(row=18, column=1, sticky=W+E)
    PICK_POCKET_VALUE.grid_forget()
    PICK_POCKET_VALUE= Label(frame7, text=SKILLS[18])
    PICK_POCKET_VALUE.grid(row=19, column=1, sticky=W+E)
    RIDE_VALUE.grid_forget()
    RIDE_VALUE= Label(frame7, text=SKILLS[19])
    RIDE_VALUE.grid(row=20, column=1, sticky=W+E)
    SEARCH_VALUE.grid_forget()
    SEARCH_VALUE= Label(frame7, text=SKILLS[20])
    SEARCH_VALUE.grid(row=21, column=1, sticky=W+E)
    SET_TRAP_VALUE.grid_forget()
    SET_TRAP_VALUE= Label(frame7, text=SKILLS[21])
    SET_TRAP_VALUE.grid(row=22, column=1, sticky=W+E)
    SPOT_VALUE.grid_forget()
    SPOT_VALUE= Label(frame7, text=SKILLS[22])
    SPOT_VALUE.grid(row=23, column=1, sticky=W+E)
    SPELLCRAFT_VALUE.grid_forget()
    SPELLCRAFT_VALUE= Label(frame7, text=SKILLS[23])
    SPELLCRAFT_VALUE.grid(row=24, column=1, sticky=W+E)    
    TAUNT_VALUE.grid_forget()
    TAUNT_VALUE= Label(frame7, text=SKILLS[24])
    TAUNT_VALUE.grid(row=25, column=1, sticky=W+E)
    TUMBLE_VALUE.grid_forget()
    TUMBLE_VALUE= Label(frame7, text=SKILLS[25])
    TUMBLE_VALUE.grid(row=26, column=1, sticky=W+E)
    UMD_VALUE.grid_forget()
    UMD_VALUE= Label(frame7, text=SKILLS[26])
    UMD_VALUE.grid(row=27, column=1, sticky=W+E)
    
SPENDING_POINT_VALUE = Label(frame7, text=skill_points)
SPENDING_POINT_VALUE.grid(row=0, column=1, sticky=W+E)
SPENDING_POINT_LABEL = Label(frame7, text="Points Remaining")
SPENDING_POINT_LABEL.grid(row=0, column=0, sticky=W+E)

ANIMAL_EMPATHY = Button(frame7, text="Animal Empathy", command=lambda: SKILLADJ(0))
ANIMAL_EMPATHY.grid(row=1, column=0, sticky=W+E)
ANIMAL_EMPATHY_VALUE= Label(frame7, text=SKILLS[0])
ANIMAL_EMPATHY_VALUE.grid(row=1, column=1, sticky=W+E)

APPRAISE = Button(frame7, text="Appraise", command=lambda: SKILLADJ(1))
APPRAISE.grid(row=2, column=0, sticky=W+E)
APPRAISE_VALUE= Label(frame7, text=SKILLS[1])
APPRAISE_VALUE.grid(row=2, column=1, sticky=W+E)

BLUFF = Button(frame7, text="Bluff", command=lambda: SKILLADJ(2))
BLUFF.grid(row=3, column=0, sticky=W+E)
BLUFF_VALUE= Label(frame7, text=SKILLS[2])
BLUFF_VALUE.grid(row=3, column=1, sticky=W+E)

CONCENTRATION = Button(frame7, text="Concentration", command=lambda: SKILLADJ(3))
CONCENTRATION.grid(row=4, column=0, sticky=W+E)
CONCENTRATION_VALUE= Label(frame7, text=SKILLS[3])
CONCENTRATION_VALUE.grid(row=4, column=1, sticky=W+E)

CRAFT_MASTERY = Button(frame7, text="Craft Mastery", command=lambda: SKILLADJ(4))
CRAFT_MASTERY.grid(row=5, column=0, sticky=W+E)
CRAFT_MASTERY_VALUE= Label(frame7, text=SKILLS[4])
CRAFT_MASTERY_VALUE.grid(row=5, column=1, sticky=W+E)

CRAFT_TRAP = Button(frame7, text="Craft Trap", command=lambda: SKILLADJ(5))
CRAFT_TRAP.grid(row=6, column=0, sticky=W+E)
CRAFT_TRAP_VALUE= Label(frame7, text=SKILLS[5])
CRAFT_TRAP_VALUE.grid(row=6, column=1, sticky=W+E)

DISABLE_TRAP = Button(frame7, text="Disable Trap", command=lambda: SKILLADJ(6))
DISABLE_TRAP.grid(row=7, column=0, sticky=W+E)
DISABLE_TRAP_VALUE= Label(frame7, text=SKILLS[5])
DISABLE_TRAP_VALUE.grid(row=7, column=1, sticky=W+E)

DISCIPLINE = Button(frame7, text="Discipline", command=lambda: SKILLADJ(7))
DISCIPLINE.grid(row=8, column=0, sticky=W+E)
DISCIPLINE_VALUE= Label(frame7, text=SKILLS[7])
DISCIPLINE_VALUE.grid(row=8, column=1, sticky=W+E)

HEAL = Button(frame7, text="Heal", command=lambda: SKILLADJ(8))
HEAL.grid(row=9, column=0, sticky=W+E)
HEAL_VALUE= Label(frame7, text=SKILLS[8])
HEAL_VALUE.grid(row=9, column=1, sticky=W+E)

HIDE = Button(frame7, text="Hide", command=lambda: SKILLADJ(9))
HIDE.grid(row=10, column=0, sticky=W+E)
HIDE_VALUE= Label(frame7, text=SKILLS[9])
HIDE_VALUE.grid(row=10, column=1, sticky=W+E)

INTIMIDATE = Button(frame7, text="Intimidate", command=lambda: SKILLADJ(10))
INTIMIDATE.grid(row=11, column=0, sticky=W+E)
INTIMIDATE_VALUE= Label(frame7, text=SKILLS[10])
INTIMIDATE_VALUE.grid(row=11, column=1, sticky=W+E)

LISTEN = Button(frame7, text="Listen", command=lambda: SKILLADJ(11))
LISTEN.grid(row=12, column=0, sticky=W+E)
LISTEN_VALUE= Label(frame7, text=SKILLS[11])
LISTEN_VALUE.grid(row=12, column=1, sticky=W+E)

LORE = Button(frame7, text="Lore", command=lambda: SKILLADJ(12))
LORE.grid(row=13, column=0, sticky=W+E)
LORE_VALUE= Label(frame7, text=SKILLS[12])
LORE_VALUE.grid(row=13, column=1, sticky=W+E)

MOVE_SILENTLY = Button(frame7, text="Move Silently", command=lambda: SKILLADJ(13))
MOVE_SILENTLY.grid(row=14, column=0, sticky=W+E)
MOVE_SILENTLY_VALUE= Label(frame7, text=SKILLS[13])
MOVE_SILENTLY_VALUE.grid(row=14, column=1, sticky=W+E)

OPEN_LOCK = Button(frame7, text="Open Lock", command=lambda: SKILLADJ(14))
OPEN_LOCK.grid(row=15, column=0, sticky=W+E)
OPEN_LOCK_VALUE= Label(frame7, text=SKILLS[14])
OPEN_LOCK_VALUE.grid(row=15, column=1, sticky=W+E)
                         
PARRY = Button(frame7, text="Parry", command=lambda: SKILLADJ(15))
PARRY.grid(row=16, column=0, sticky=W+E)
PARRY_VALUE= Label(frame7, text=SKILLS[15])
PARRY_VALUE.grid(row=16, column=1, sticky=W+E)

PERFORM = Button(frame7, text="Perform", command=lambda: SKILLADJ(16))
PERFORM.grid(row=17, column=0, sticky=W+E)
PERFORM_VALUE= Label(frame7, text=SKILLS[16])
PERFORM_VALUE.grid(row=17, column=1, sticky=W+E)

PERSUADE = Button(frame7, text="Persuade", command=lambda: SKILLADJ(17))
PERSUADE.grid(row=18, column=0, sticky=W+E)
PERSUADE_VALUE= Label(frame7, text=SKILLS[17])
PERSUADE_VALUE.grid(row=18, column=1, sticky=W+E)

PICK_POCKET = Button(frame7, text="Pick Pocket", command=lambda: SKILLADJ(18))
PICK_POCKET.grid(row=19, column=0, sticky=W+E)
PICK_POCKET_VALUE= Label(frame7, text=SKILLS[18])
PICK_POCKET_VALUE.grid(row=19, column=1, sticky=W+E)

RIDE = Button(frame7, text="Ride", command=lambda: SKILLADJ(19))
RIDE.grid(row=20, column=0, sticky=W+E)
RIDE_VALUE= Label(frame7, text=SKILLS[19])
RIDE_VALUE.grid(row=20, column=1, sticky=W+E)

SEARCH = Button(frame7, text="Search", command=lambda: SKILLADJ(20))
SEARCH.grid(row=21, column=0, sticky=W+E)
SEARCH_VALUE= Label(frame7, text=SKILLS[20])
SEARCH_VALUE.grid(row=21, column=1, sticky=W+E)

SET_TRAP = Button(frame7, text="Set Trap", command=lambda: SKILLADJ(21))
SET_TRAP.grid(row=22, column=0, sticky=W+E)
SET_TRAP_VALUE= Label(frame7, text=SKILLS[21])
SET_TRAP_VALUE.grid(row=22, column=1, sticky=W+E)

SPELLCRAFT = Button(frame7, text="Spellcraft", command=lambda: SKILLADJ(22))
SPELLCRAFT.grid(row=23, column=0, sticky=W+E)
SPELLCRAFT_VALUE= Label(frame7, text=SKILLS[22])
SPELLCRAFT_VALUE.grid(row=23, column=1, sticky=W+E)

SPOT = Button(frame7, text="Spot", command=lambda: SKILLADJ(23))
SPOT.grid(row=24, column=0, sticky=W+E)
SPOT_VALUE= Label(frame7, text=SKILLS[23])
SPOT_VALUE.grid(row=24, column=1, sticky=W+E)

TAUNT = Button(frame7, text="Taunt", command=lambda: SKILLADJ(24))
TAUNT.grid(row=25, column=0, sticky=W+E)
TAUNT_VALUE= Label(frame7, text=SKILLS[24])
TAUNT_VALUE.grid(row=25, column=1, sticky=W+E)

TUMBLE = Button(frame7, text="Tumble", command=lambda: SKILLADJ(25))
TUMBLE.grid(row=26, column=0, sticky=W+E)
TUMBLE_VALUE= Label(frame7, text=SKILLS[25])
TUMBLE_VALUE.grid(row=26, column=1, sticky=W+E)

UMD = Button(frame7, text="Use Magic Device", command=lambda: SKILLADJ(26))
UMD.grid(row=27, column=0, sticky=W+E)
UMD_VALUE= Label(frame7, text=SKILLS[26])
UMD_VALUE.grid(row=27, column=1, sticky=W+E)

#%%
root.mainloop()