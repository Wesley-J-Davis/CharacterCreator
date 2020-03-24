# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:33:32 2020

@author: Wesley Davis
"""
import numpy as np
'''All NumPy arrays of level progression for each class, up to Epic'''
Barbarian = np.array([[ 0, 0, 0, 0],
                      [ 1, 2, 0, 0],
                      [ 2, 3, 0, 0],
                      [ 3, 3, 1, 1],
                      [ 4, 4, 1, 1],
                      [ 5, 4, 1, 1],
                      [ 6, 5, 2, 2],
                      [ 7, 5, 2, 2],
                      [ 8, 6, 2, 2],
                      [ 9, 6, 3, 3],
                      [10, 7, 3, 3],
                      [11, 7, 3, 3],
                      [12, 8, 4, 4],
                      [13, 8, 4, 4],
                      [14, 9, 4, 4],
                      [15, 9, 5, 5],
                      [16,10, 5, 5],
                      [17,10, 5, 5],
                      [18,11, 6, 6],
                      [19,11, 6, 6],
                      [20,12, 6, 6]])

Bard =      np.array([[ 0, 0, 0, 0],
                      [ 0, 0, 2, 2],
                      [ 1, 0, 3, 3],
                      [ 2, 1, 3, 3],
                      [ 3, 1, 4, 4],
                      [ 3, 1, 4, 4],
                      [ 4, 2, 5, 5],
                      [ 5, 2, 5, 5],
                      [ 6, 2, 6, 6],
                      [ 6, 3, 6, 6],
                      [ 7, 3, 7, 7],
                      [ 8, 3, 7, 7],
                      [ 9, 4, 8, 8],
                      [ 9, 4, 8, 8],
                      [10, 4, 9, 9],
                      [11, 5, 9, 9],
                      [12, 5,10,10],
                      [12, 5,10,10],
                      [13, 6,11,11],
                      [14, 6,11,11],
                      [15, 6,12,12]])

Cleric = Bard[:,[0,2,1,3]]
Druid = Cleric
Fighter = Barbarian
Monk = Bard[:,[0,2,2,2]]
Paladin = Barbarian
Ranger = Barbarian[:,[0,1,1,3]]
Rogue = Bard[:,[0,1,2,1]]
Sorcerer = np.array([[ 0, 0, 0, 0],
                     [ 0, 0, 0, 2],
                     [ 1, 0, 0, 3],
                     [ 1, 1, 1, 3],
                     [ 2, 1, 1, 4],
                     [ 2, 1, 1, 4],
                     [ 3, 2, 2, 5],
                     [ 3, 2, 2, 5],
                     [ 4, 2, 2, 6],
                     [ 4, 3, 3, 6],
                     [ 5, 3, 3, 7],
                     [ 5, 3, 3, 7],
                     [ 6, 4, 4, 8],
                     [ 6, 4, 4, 8],
                     [ 7, 4, 4, 9],
                     [ 7, 5, 5, 9],
                     [ 8, 5, 5,10],
                     [ 8, 5, 5,10],
                     [ 9, 6, 6,11],
                     [ 9, 6, 6,11],
                     [10, 6, 6,12]])
Wizard = Sorcerer

Classes = {"BARBARIAN": Barbarian, "BARD": Bard, "CLERIC":Cleric, "DRUID": Druid, 
           "FIGHTER": Fighter, "MONK": Monk, "PALADIN": Paladin, "RANGER": Ranger, 
           "ROGUE": Rogue, "SORCERER": Sorcerer, "WIZARD": Wizard}

CLASSES = ("BARB", "BARD", "CLERIC", "DRUID","FIGHTER", "MONK", "PALADIN", 
           "RANGER", "ROGUE", "SORCERER", "WIZARD")

#CLASSES_PRESTIGE = {"SHADOWDANCER": ShadowDancer, "HARPER_SCOUT": Harper_Scout,
#                    "ARCANE_ARCHER": Arcane_Archer, "ASSASSIN": Assassin,
#                    "BLACKGUARD": Blackguard, "DIVINE_CHAMPION": Divine_Champion,
#                    "WEAPONMASTER": Weapon_Master, "PALE_MASTER": Pale_Master,
#                    "SHIFTER": Shifter, "EARTHKIN_DEFENDER": Earthkin_Defender,
#                    "RED_DRAGON_DISCIPLE": Red_Dragon_Disciple,
#                    "HARPER_MAGE": Harper_Mage, "HARPER_PRIEST": Harper_Priest,
#                    "HARPER_PARAGON": Harper_Paragon, "MASTER_HARPER": Master_Harper,
#                    "COMMONER": Commoner, "SPECIALIST": Specialist}
epic_level  = 0
EPIC_LEVELS =       np.array([[ 0, 0, 0, 0],
                              [ 1, 0, 0, 0],
                              [ 1, 1, 1, 1],
                              [ 2, 1, 1, 1],
                              [ 2, 2, 2, 2],
                              [ 3, 2, 2, 2],
                              [ 3, 3, 3, 3],
                              [ 4, 3, 3, 3],
                              [ 4, 4, 4, 4],
                              [ 5, 4, 4, 4],
                              [ 5, 5, 5, 5]])

Alignment = ["LG", "NG", "CG",
             "LN", "TN", "CN",
             "LE", "NE", "CE"]


#Earthkin_Defender = np.array([[ 0, 0, 0, 0],
#                              [ 1, 2, 0, 2],
#                              [ 2, 3, 0, 3],
#                              [ 3, 3, 1, 3],
#                              [ 4, 4, 1, 4],
#                              [ 5, 4, 1, 4],
#                              [ 6, 5, 2, 5],
#                              [ 7, 5, 2, 5],
#                              [ 8, 6, 2, 6],
#                              [ 9, 6, 3, 6],
#                              [10, 7, 3, 7]])
#Shadowdancer = np.array([[ 0, 0, 0, 0],
#                         [ 0, 0, 2, 0],
#                         [ 1, 0, 3, 0],
#                         [ 2, 1, 3, 1],
#                         [ 3, 1, 4, 1],
#                         [ 3, 1, 4, 1],
#                         [ 4, 2, 5, 2],
#                         [ 5, 2, 5, 2],
#                         [ 6, 2, 6, 2],
#                         [ 6, 3, 6, 3],
#                         [ 7, 3, 7, 3]])
#Arcane_Archer = np.array([[ 0, 0, 0, 0],
#                          [ 1, 2, 2, 0],
#                          [ 2, 3, 3, 0],
#                          [ 3, 3, 3, 1],
#                          []])

# Thinking Tuples for now, cause they won't have to change, but will
#
#Assassin = 
#Weapon_Master = 
#Blackguard = 
#Red_Dragon_Disciple = 
#Purple_Dragon_Knight = 
#Knight = 
#Divine_Champion = 
#Commoner = 
#Specialist = 

#Classes_Prestige = (Earthkin_Defender,
#           Shadowdancer, Arcane_Archer, Assassin,
#           Blackguard, Weapon_Master, Red_Dragon_Disciple,
#           Purple_Dragon_Knight, Knight, Divine_Champion,
#           Commoner, Specialist)


#Epic_Barb
#Epic_Bard
#Epic_Cleric
#Epic_Druid
#Epic_Fighter
#Epic_Monk
#Epic_Paladin
#Epic_Rogue
#Epic_Ranger
#Epic_Sorcerer
#Epic_Wizard
#Epic_Defender
#Epic_SD
#Epic_AA
#Epic_Assassin
#Epic_BG
#Epic_WM
#Epic_RDD
#Epic_Knight
#Epic_Divine_Champion
#Epic_Commoner
#Epic_Specialist
#
#Classes_Epic = (Epic_Barb, Epic_Bard, Epic_Cleric, Epic_Druid,
#                Epic_Fighter, Epic_Monk, Epic_Paladin, Epic_Paladin,
#                Epic_Rogue, Epic_Ranger, Epic_Sorcerer, Epic_Wizard,
#                Epic_Defender, Epic_SD, Epic_AA, Epic_Assassin,
#                Epic_BG, Epic_WM, Epic_RDD, Epic_Knight,
#                Epic_Divine_Champion, Epic_Commoner, Epic_Specialist)