# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:56:39 2021

@author: fgluck
"""
# This program defines a function which generates a menu then executes the
# menu choices.
# Ref: https://www.youtube.com/watch?v=63nw00JqHo0
# ------------------------------------------------------
# Import the Following Libraries
import random
# ------------------------------------------------------
# Function Definitions
# display_menu()
	# 
	# Description: Display the menu. Putting it in a function  makes
	# it easier to maintain
	# Arguments: none
	# Returns: none
def display_menu():
	print("\n**********************")
	print ("[1] Greeting")
	print ("[2] Simulate Coin Flipping")
	print ("[3] Something else")
	print ("\n")
	print ("[0] Exit The Program")
	print("\n**********************")
#End of Function Defs
# -----------------------------------------
# Program starts here
# Display the menu and ask for the choice
display_menu()
choice = int(input("Enter Your Choice: "))
# And process the menu as long as we are not asked to end 
while choice != 0:
	# *******************************
	# PROBLEM 1: Simple Greeting
	# *******************************
	if choice == 1:
		name = input("Hello, what is your name? ")
		print(f"Nice to meet you {name}!")
	# ***************************************
	# PROBLEM 1A: Coin Flip Simulation 
	# ***************************************
	elif choice == 2:
		heads=0
		tails=0
		print ("Simulating one million flips... be patient...")
		# generate random number between 1 and 1000
		for val in range(0,1000000):
			target = random.randint(1,1000)
			# if the number is even, then it represents heads
			if target%2 == 0:
				heads=heads + 1
			else: # if the number is odd, then it represents tails
				tails=tails+1
		#end of loop	
		print(f'Number of tails:{tails:,} \nNumber of heads:{heads:,}')
	elif choice ==3:
		print("Choice 3")
	else:
		print ("Bad choice. Try Again")
		
	choice = int(input("Enter Your Choice:"))
# END OF WHILE LOOP	
print ("Thanks for Using This Program")


	




