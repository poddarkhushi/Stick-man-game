import os
def clr_terminal():
    os.system('cls')
# how do i clear the terminal after taking the input?
# os.system() is a Python function used to run operating-system commands (like commands you type in a terminal or command prompt)
clr_terminal()
def zero(n):
    if n == 0:
       print(' 0')
       print('/|\\')
       print("/ \\")
    elif n == 1:
       print(' 0')
       print('/|\\')
       print("  \\")
    elif n == 2:
       print(' 0')
       print('/|\\')
       print('')
    elif n == 3:
       print(' 0')
       print(' |\\')
       print('')
    elif n == 4:
       print(' 0')
       print(' |')
       print('')
    elif n == 5:
       print(' 0')
       print('')
    elif n == 6:
       print('The poor man died !!')

# P1 = input("Player 1: ")
# P2 = input("Player 2: ")
clr_terminal()
movie = input("Enter a movie name: ").lower()  # better option
# a = movie.lower()
clr_terminal()
Vowels = "aeiou"
Display = ""
for v in movie:
    if v in Vowels:
        Display += v
    elif v == " ":
        Display += " "
    else:  # last mein elif nahi aaiyega
        Display += "_"
n = 0
print(f"Guess the movie name: {Display}")
print("Save the man and win or let him die and loose.")
zero(0)

while "_" in Display and n < 6:  
    guess = input("Make a guess: ").lower()
    clr_terminal()
    new_display = ""  # new string
    for i in range(len(movie)):
       if movie[i] == guess:          # If the guess matches the movie at this position
       # movie[i] refers to the i-th character of the movie string
          new_display += guess       # Put the guessed letter
       else:
          new_display += Display[i]
    if guess not in movie:
        n += 1            
    Display = new_display

    print(f"Guess the movie name: {Display}")
    print("Save the man and win or let him die and loose.")
    zero(n)
    if n >= 1 and n != 6 :
       print('Number of chances left = ', 6-n)

if "_" not in Display :
    print("Congratulations! You saved the man and guessed the movie!")
else:
    print(f"You lost! The movie was: {movie}")


