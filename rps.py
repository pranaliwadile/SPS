# -*- coding: utf-8 -*-
"""RPS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZOw_xQhgdIK2SXG4IvOAq1t8fiqXh97
"""

import random

choices = ["Stone", "Paper", "Scissors"]
computer = random.choice(choices)

player = False
cpu_score = 0
player_score = 0

while True:
    player = input("Stone, Paper or  Scissors?").capitalize()
    ## Conditions of Stone,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Stone":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Stone":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break









