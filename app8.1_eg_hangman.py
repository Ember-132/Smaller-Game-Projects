import random
from hangman_images import hangman_pics, hangman_logo
from hangman_words import word_list


#-----------------------------------------------------------------------------------


print(hangman_logo)

random_word = random.choice(word_list)
random_word_length = len(random_word)

placeholder = ""

for position in range(random_word_length):
    placeholder += "-"
    
print(f"Word to guess: {placeholder}")

#MAIN BODY OF CODE.

lives = 8

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/8 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}")

    display = ""

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"

    print("Word to guess: " + display)


    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE. The correct word was {random_word} **********************")

    if "-" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_pics[lives])