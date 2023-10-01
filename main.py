import random
from stages import stages
from wordList import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display_word = []
lives = 6
game_over = False


for _ in range(word_length):
  display_word.append("_")

print(f"Welcome to the Hangman game! The word has {word_length} letters.\n")
  
while not game_over:
  guess = input("Guess a letter:\n").lower()
  if len(guess) > 1:
    print("One letter per guess!\nYou have lost a live!")
    lives -= 1
    print(stages[lives])
  elif len(guess) == 0:
    print("No letter was guessed!")
  elif guess in display_word:
    print(f"{guess} is already chosen")
  else:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        print(f"{guess} is correct!")
        display_word[position] = letter
    if guess not in display_word:
      print("Wrong choice...\nYou have lost a live!")
      lives -= 1
      print(stages[lives])
    if "_" not in display_word:
      game_over = True
      print("You won!")
    elif lives == 0:
      game_over = True
      print(f"You lost! The word was: {chosen_word}")
    printed_word = f"Your guess is: {' '.join(display_word)}\n"
    print(printed_word)
