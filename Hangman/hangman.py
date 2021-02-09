# Hangman

# importing these things just to make life easier
import os
import sys
from tkinter import *
import hangman_words
from hangman_words import *
import random
from random import choice

guessed_wrong = 0
def game():
	# Just setting up tkinter
	root = Tk()
	root.title("Hangman")
	root.geometry("487x515")

	# Creates the first frame (Top left)
	frame1 = LabelFrame(root, width = 368, height = 358, bg = "white")
	frame1.place(x = 0, y = 0)

	# Creates the second frame (Most right)
	frame2 = LabelFrame(root, padx = 4, pady = 4)
	frame2.place(x = 371, y = 0)

	# Creates the third frame (Under the first one)
	frame3 = LabelFrame(root, width = 368, height = 101)
	frame3.place(x = 0, y = 361)

	# Creates the fourth frame (The bottom one)
	frame4 = LabelFrame(root, width = 256, height = 51)
	frame4.place(x = 0, y = 465)

	# Filters the word from the imported word list words_list
	def filter(words_list):
		rand_word = random.choice(words_list)
		while ("-" in rand_word or " " in rand_word) and len(rand_word) > 12:
			rand_word = random.choice(words_list)
		return rand_word

	# To validate the input of the user
	def isValid(letter_input, word):
		if letter_input in word and (2 > len(letter_input) > 0):
			return True

	# Getting the word
	word = filter(words_list).upper()
	print(word)
	text_word = Label(root, text = word)

	# To keep track of the used letters in a set
	used_letter = set()
	word_letter = set(word)

	# Puts the buttons to a random position
	def generatePos(word_letter):
		# Setting the initial value of the buttons to be ""
		button_letter = ["" for i in range(18)]
		# Picking random characters less than the amount of characters needed for the word
		letters_in = 0
		for letter in range(len(button_letter)-len(word_letter)):
			alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			ran_in = random.randint(0, (len(button_letter)-1))
			while button_letter[ran_in] != "":
				ran_in = random.randint(0, (len(button_letter)-1))
			button_letter[ran_in] = random.choice(alphabet)
		# Picking the characters needed for the word
		word_letter_in = 0
		for letter in button_letter:
			if letter == "":
				letter_in = button_letter.index(letter)
				button_letter[letter_in] = list(word_letter)[word_letter_in]
				word_letter_in += 1
		return button_letter

	# Displays the state of the hangman
	def display(guessed_wrong):
		display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
		# Base
		if guessed_wrong == 1:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)
			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

		# Base + Pole
		elif guessed_wrong == 2:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)
			display_draw.create_line(86, 270, 86, 20, width = 4)
			display_draw.create_line(88, 120, 148, 40, width = 4)
			display_draw.create_line(66, 40, 290, 40, width = 4)			

			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

		# Base + Pole + Head + Body
		elif guessed_wrong == 3:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)
			
			display_draw.create_line(86, 270, 86, 20, width = 4)
			display_draw.create_line(88, 120, 148, 40, width = 4)
			display_draw.create_line(66, 40, 290, 40, width = 4)
			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

			display_draw.create_oval(265, 80, 313, 127, width = 4)
			display_draw.create_line(290, 127, 290, 210, width = 4)

		# Base + Pole + Head + Body + Arm
		elif guessed_wrong == 4:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)

			display_draw.create_line(86, 270, 86, 20, width = 4)
			display_draw.create_line(88, 120, 148, 40, width = 4)
			display_draw.create_line(66, 40, 290, 40, width = 4)
			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

			display_draw.create_oval(265, 80, 313, 127, width = 4)
			display_draw.create_line(290, 127, 290, 210, width = 4)
			display_draw.create_line(290, 160, 320, 120, width = 4)
			display_draw.create_line(290, 160, 260, 120, width = 4)

		# Base + Pole + Head + Body + Arm + Legs
		elif guessed_wrong == 5:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)

			display_draw.create_line(86, 270, 86, 20, width = 4)
			display_draw.create_line(88, 120, 148, 40, width = 4)
			display_draw.create_line(66, 40, 290, 40, width = 4)
			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

			display_draw.create_oval(265, 80, 313, 127, width = 4)
			display_draw.create_line(290, 127, 290, 210, width = 4)
			display_draw.create_line(290, 160, 320, 120, width = 4)
			display_draw.create_line(290, 160, 260, 120, width = 4)
			display_draw.create_line(290, 210, 310, 250, width = 4)
			display_draw.create_line(290, 210, 270, 250, width = 4)

		# Hangman
		elif guessed_wrong == 6:
			display_draw = Canvas(frame1, width = 360, height = 350, bg = "white")
			display_draw.place(x = 0, y = 0)

			display_draw.create_line(86, 270, 86, 20, width = 4) #
			display_draw.create_line(88, 120, 148, 40, width = 4)
			display_draw.create_line(66, 40, 290, 40, width = 4)
			display_draw.create_line(25, 320, 40, 270, width = 4)
			display_draw.create_line(40, 270, 131, 270, width = 4)
			display_draw.create_line(131, 270, 146, 320, width = 4)
			display_draw.create_line(25, 320, 146, 320, width = 4)

			display_draw.create_oval(265, 80, 313, 127, width = 4)
			display_draw.create_line(290, 127, 290, 210, width = 4)
			display_draw.create_line(290, 160, 320, 120, width = 4)
			display_draw.create_line(290, 160, 260, 120, width = 4)
			display_draw.create_line(290, 210, 310, 250, width = 4)
			display_draw.create_line(290, 210, 270, 250, width = 4)

			display_draw.create_line(290, 40, 290, 80, width = 4)


	# Calls the "generatePos()" funciton
	buttons_letters = generatePos(word_letter)

	# Will replace the unguessed characters with "_" in the word
	word_guessed = [letter if letter in used_letter else "_" for letter in word]
	word_guessed_state = "  ".join(word_guessed)
	text_word = Label(frame3, text = "WORD:")
	text_word.config(font = ("default", 13))
	text_word.place(x = 20, y = 15)
	text_word_guessed_state = Label(frame3, text = word_guessed_state)
	text_word_guessed_state.config(font = ("default", 20))
	text_word_guessed_state.place(x = 30, y = 40)

	# If the user presses the button with the characters, it'll be processed here
	def insertLetter(letter, wrong_guesses):
		if letter in word:

			# If the character's in the word and has not been used then show the player that it's the right char
			if letter not in used_letter:
				used_letter.add(letter)
				print(used_letter)
				word_guessed = [letter if letter in used_letter else "_" for letter in word]
				word_guessed_state = "  ".join(word_guessed)
				text_word = Label(frame3, text = "WORD:")
				text_word.config(font = ("default", 13))
				text_word.place(x = 20, y = 15)

				text_word_guessed_state = Label(frame3, text = word_guessed_state)
				text_word_guessed_state.config(font = ("default", 20))
				text_word_guessed_state.place(x = 30, y = 40)

				# this checks if the player has won or not
				if len(used_letter) == len(word_letter):
					print("You won")
					frame1 = LabelFrame(root, width = 368, height = 358, bg = "white")
					frame1.place(x = 0, y = 0)
					you_won_text = Label(frame1, text = "YOU WON!")
					you_won_text.config(font = ("default", 30))
					you_won_text.pack()
					disableButton("disable")
				return used_letter

			# If the character is in the word and has been used, it'll do nothing
			elif letter in used_letter:
				return

		# If the character is not in the word, or the wrong character then it'll be processed here
		elif letter not in word:

			# If the character is wrong and has been used then do nothing
			if letter in used_letter:
				return

			# Otherwise increment the amount of mistakes and change the hangman state
			else:
				print("wrong")
				global guessed_wrong
				guessed_wrong = guessed_wrong + 1
				if guessed_wrong == 6:
					print("The word is: " + word)
					frame1 = LabelFrame(root, width = 368, height = 358, bg = "white")
					frame1.place(x = 0, y = 0)
					you_lost_text = Label(frame1, text = "YOU LOST :(")
					you_lost_text.config(font = ("default", 30))
					you_lost_text.pack()
					the_word_text = Label(frame1, text = "WORD: " + (word).upper())
					the_word_text.config(font = ("default", 30))
					the_word_text.pack()
					display(guessed_wrong)
					disableButton("disable")
				print(guessed_wrong)
				display(guessed_wrong)

	# This function disables the button
	def disableButton(letter, num = "0"):
		if (letter == ("disable")) and (num == "0"):
			button1 = Button(frame2, text = buttons_letters[0], state = DISABLED, padx = 15, pady = 15).grid(row = 0, column = 1, padx = 1, pady = 1)
			button2 = Button(frame2, text = buttons_letters[1], state = DISABLED, padx = 15, pady = 15).grid(row = 1, column = 1, padx = 1, pady = 1)
			button3 = Button(frame2, text = buttons_letters[2], state = DISABLED, padx = 15, pady = 15).grid(row = 2, column = 1, padx = 1, pady = 1)
			button4 = Button(frame2, text = buttons_letters[3], state = DISABLED, padx = 15, pady = 15).grid(row = 3, column = 1, padx = 1, pady = 1)
			button5 = Button(frame2, text = buttons_letters[4], state = DISABLED, padx = 15, pady = 15).grid(row = 4, column = 1, padx = 1, pady = 1)
			button6 = Button(frame2, text = buttons_letters[5], state = DISABLED, padx = 15, pady = 15).grid(row = 5, column = 1, padx = 1, pady = 1)
			button7 = Button(frame2, text = buttons_letters[6], state = DISABLED, padx = 15, pady = 15).grid(row = 6, column = 1, padx = 1, pady = 1)
			button8 = Button(frame2, text = buttons_letters[7], state = DISABLED, padx = 15, pady = 15).grid(row = 7, column = 1, padx = 1, pady = 1)
			button9 = Button(frame2, text = buttons_letters[8], state = DISABLED, padx = 15, pady = 15).grid(row = 8, column = 1, padx = 1, pady = 1)
			button10 = Button(frame2, text = buttons_letters[9], state = DISABLED, padx = 15, pady = 15).grid(row = 0, column = 2, padx = 1, pady = 1)
			button11 = Button(frame2, text = buttons_letters[10], state = DISABLED, padx = 15, pady = 15).grid(row = 1, column = 2, padx = 1, pady = 1)
			button12 = Button(frame2, text = buttons_letters[11], state = DISABLED, padx = 15, pady = 15).grid(row = 2, column = 2, padx = 1, pady = 1)
			button13 = Button(frame2, text = buttons_letters[12], state = DISABLED, padx = 15, pady = 15).grid(row = 3, column = 2, padx = 1, pady = 1)
			button14 = Button(frame2, text = buttons_letters[13], state = DISABLED, padx = 15, pady = 15).grid(row = 5, column = 2, padx = 1, pady = 1)
			button15 = Button(frame2, text = buttons_letters[14], state = DISABLED, padx = 15, pady = 15).grid(row = 4, column = 2, padx = 1, pady = 1)
			button16 = Button(frame2, text = buttons_letters[15], state = DISABLED, padx = 15, pady = 15).grid(row = 6, column = 2, padx = 1, pady = 1)
			button17 = Button(frame2, text = buttons_letters[16], state = DISABLED, padx = 15, pady = 15).grid(row = 7, column = 2, padx = 1, pady = 1)
			button18 = Button(frame2, text = buttons_letters[17], state = DISABLED, padx = 15, pady = 15).grid(row = 8, column = 2, padx = 1, pady = 1)
		elif num == "1":
			button1 = Button(frame2, text = buttons_letters[0], state = DISABLED, padx = 15, pady = 15).grid(row = 0, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[0], guessed_wrong)
		elif num == "2":
			button2 = Button(frame2, text = buttons_letters[1], state = DISABLED, padx = 15, pady = 15).grid(row = 1, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[1], guessed_wrong)
		elif num == "3":
			button3 = Button(frame2, text = buttons_letters[2], state = DISABLED, padx = 15, pady = 15).grid(row = 2, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[2], guessed_wrong)
		elif num == "4":
			button4 = Button(frame2, text = buttons_letters[3], state = DISABLED, padx = 15, pady = 15).grid(row = 3, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[3], guessed_wrong)
		elif num == "5":
			button5 = Button(frame2, text = buttons_letters[4], state = DISABLED, padx = 15, pady = 15).grid(row = 4, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[4], guessed_wrong)
		elif num == "6":
			button6 = Button(frame2, text = buttons_letters[5], state = DISABLED, padx = 15, pady = 15).grid(row = 5, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[5], guessed_wrong)
		elif num == "7":
			button7 = Button(frame2, text = buttons_letters[6], state = DISABLED, padx = 15, pady = 15).grid(row = 6, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[6], guessed_wrong)
		elif num == "8":
			button8 = Button(frame2, text = buttons_letters[7], state = DISABLED, padx = 15, pady = 15).grid(row = 7, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[7], guessed_wrong)
		elif num == "9":
			button9 = Button(frame2, text = buttons_letters[8], state = DISABLED, padx = 15, pady = 15).grid(row = 8, column = 1, padx = 1, pady = 1)
			insertLetter(buttons_letters[8], guessed_wrong)
		elif num == "10":
			button10 = Button(frame2, text = buttons_letters[9], state = DISABLED, padx = 15, pady = 15).grid(row = 0, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[9], guessed_wrong)
		elif num == "11":
			button11 = Button(frame2, text = buttons_letters[10], state = DISABLED, padx = 15, pady = 15).grid(row = 1, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[10], guessed_wrong)
		elif num == "12":
			button12 = Button(frame2, text = buttons_letters[11], state = DISABLED, padx = 15, pady = 15).grid(row = 2, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[11], guessed_wrong)
		elif num == "13":
			button13 = Button(frame2, text = buttons_letters[12], state = DISABLED, padx = 15, pady = 15).grid(row = 3, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[12], guessed_wrong)
		elif num == "14":
			button14 = Button(frame2, text = buttons_letters[13], state = DISABLED, padx = 15, pady = 15).grid(row = 5, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[13], guessed_wrong)
		elif num == "15":
			button15 = Button(frame2, text = buttons_letters[14], state = DISABLED, padx = 15, pady = 15).grid(row = 4, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[14], guessed_wrong)
		elif num == "16":
			button16 = Button(frame2, text = buttons_letters[15], state = DISABLED, padx = 15, pady = 15).grid(row = 6, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[15], guessed_wrong)
		elif num == "17":
			button17 = Button(frame2, text = buttons_letters[16], state = DISABLED, padx = 15, pady = 15).grid(row = 7, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[16], guessed_wrong)
		elif num == "18":
			button18 = Button(frame2, text = buttons_letters[17], state = DISABLED, padx = 15, pady = 15).grid(row = 8, column = 2, padx = 1, pady = 1)
			insertLetter(buttons_letters[17], guessed_wrong)
	# This makes and puts the buttons
	button1 = Button(frame2, text = buttons_letters[0], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[0], "1")).grid(row = 0, column = 1, padx = 1, pady = 1)
	button2 = Button(frame2, text = buttons_letters[1], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[1], "2")).grid(row = 1, column = 1, padx = 1, pady = 1)
	button3 = Button(frame2, text = buttons_letters[2], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[2], "3")).grid(row = 2, column = 1, padx = 1, pady = 1)
	button4 = Button(frame2, text = buttons_letters[3], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[3], "4")).grid(row = 3, column = 1, padx = 1, pady = 1)
	button5 = Button(frame2, text = buttons_letters[4], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[4], "5")).grid(row = 4, column = 1, padx = 1, pady = 1)
	button6 = Button(frame2, text = buttons_letters[5], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[5], "6")).grid(row = 5, column = 1, padx = 1, pady = 1)
	button7 = Button(frame2, text = buttons_letters[6], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[6], "7")).grid(row = 6, column = 1, padx = 1, pady = 1)
	button8 = Button(frame2, text = buttons_letters[7], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[7], "8")).grid(row = 7, column = 1, padx = 1, pady = 1)
	button9 = Button(frame2, text = buttons_letters[8], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[8], "9")).grid(row = 8, column = 1, padx = 1, pady = 1)
	button10 = Button(frame2, text = buttons_letters[9], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[9], "10")).grid(row = 0, column = 2, padx = 1, pady = 1)
	button11 = Button(frame2, text = buttons_letters[10], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[10], "11")).grid(row = 1, column = 2, padx = 1, pady = 1)
	button12 = Button(frame2, text = buttons_letters[11], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[11], "12")).grid(row = 2, column = 2, padx = 1, pady = 1)
	button13 = Button(frame2, text = buttons_letters[12], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[12], "13")).grid(row = 3, column = 2, padx = 1, pady = 1)
	button14 = Button(frame2, text = buttons_letters[13], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[13], "14")).grid(row = 5, column = 2, padx = 1, pady = 1)
	button15 = Button(frame2, text = buttons_letters[14], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[14], "15")).grid(row = 4, column = 2, padx = 1, pady = 1)
	button16 = Button(frame2, text = buttons_letters[15], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[15], "16")).grid(row = 6, column = 2, padx = 1, pady = 1)
	button17 = Button(frame2, text = buttons_letters[16], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[16], "17")).grid(row = 7, column = 2, padx = 1, pady = 1)
	button18 = Button(frame2, text = buttons_letters[17], padx = 15, pady = 15, command = lambda: disableButton(buttons_letters[17], "18")).grid(row = 8, column = 2, padx = 1, pady = 1)

	# This funciton is executed when the button "button_exit" is presesd. It'll stop the program
	def exit():
		root.destroy()
	button_exit = Button(frame4, text = "EXIT", width = 8, height = 2, command = exit)
	button_exit.config(font = ("default", 11))
	button_exit.place(x = 0, y = 0)

	# This function will restart the program if the button "button_restart" is pressed
	def restart():
		os.execv(sys.executable, ['python'] + sys.argv)
	button_restart = Button(frame4, text = "RESTART", width = 8, height = 2, command = restart)
	button_restart.config(font = ("default", 11))
	button_restart.place(x = 85, y = 0)

	# This function is pretty useless. It's just there waiting for people to click it and tell them that I made it
	def credits():
		credits_window = Toplevel(root)
		credits_window.geometry("200x170")
		credits_text = Label(credits_window, text = "Credits:").pack(pady = 5)
		team_text = Label(credits_window, text = "Team:").pack()
		code_text = Label(credits_window, text = "Programmer: Kaindra Djoemena").pack()
		design_text = Label(credits_window, text = "Designer: Kaindra Djoemena").pack()
		illustrator_text = Label(credits_window, text = "illustrator: Kaindra Djoemena").pack()
		advisor_text = Label(credits_window, text = "Advisor: Kaindra Djoemena").pack()
		date_text = Label(credits_window, text = "02-2021", relief = SUNKEN).pack(pady = 6)
	button_credits = Button(frame4, text = "CREDITS", width = 8, height = 2, command = credits)
	button_credits.config(font = ("default", 11))
	button_credits.place(x = 170, y = 0)

	root.mainloop()

# This will execute the game
game()
