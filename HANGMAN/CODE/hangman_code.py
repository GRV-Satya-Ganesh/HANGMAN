import random
from hangman_art import stages,logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word) #test
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(" ".join(display))
print(f"You are given a {len(display)} letterd word")

lives = 6 # Number of Chances

while ("_" in display) and (lives >= 0):
    guess = input("Guess a letter: ").lower()

   
    for position in range(word_length):
        letter = chosen_word[position]
        #Check guessed letter
        if letter == guess:
            display[position] = letter
	
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

   #Condition for loosing a life
    if guess not in chosen_word:
        print(f"You guessed {guess} ,that's not in the word. You loose a life")
        print(stages[lives])
        #Check if lives are out of stock.
        if lives <= 0:
            print(f"You loose, and the given word is {chosen_word}.")
        lives -= 1

#Game wining conditions :

#Check if user has got all letters.
if "_" not in display:
    print("You win, I think you have great interst in bikes.")