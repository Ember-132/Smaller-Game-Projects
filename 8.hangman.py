import random
from hangman_words import word_list

hangman_8 = '''
      _______
     |/      
     |      
     |      
     |       
     |        
     |
    _|___
'''
hangman_7 = '''
      _______
     |/      |
     |      
     |      
     |       
     |       
     |
    _|___
'''

hangman_6 = '''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
'''

hangman_5 = '''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |       
     |
    _|___
'''

hangman_4 = '''
      _______
     |/      |
     |      (_)
     |     __|
     |       
     |       
     |
    _|___
'''

hangman_3 = '''
      _______
     |/      |
     |      (_)
     |     __|__
     |       
     |       
     |
    _|___
'''

hangman_2 = '''
      _______
     |/      |
     |      (_)
     |     __|__
     |       |
     |       
     |
    _|___
'''

hangman_1 = '''
      _______
     |/      |
     |      (_)
     |     __|__
     |       |
     |      /  
     |
    _|___
'''

hangman_0 = '''
      _______
     |/      |
     |      (_)
     |     __|__
     |       |
     |      // 
     |
    _|___
'''

def game_complete():
    incorrect_char = 0
    correct_char = 0
    letter_match2 = 0
    for letter in list_word:
            if letter != "_":
                correct_char += 1
                letter_match2 +=1
                if letter_match2 == len(random_word):
                    if incorrect_char >= 1:
                        return False
                    else:
                        print("WINNER! You completed the game!")
                        print(f"\nThe word was: {random_word}")
                        return True
            elif letter == "_":
                letter_match2 += 1
                incorrect_char += 1
                if letter_match2 == len(random_word):
                    if incorrect_char >= 1:
                        return False
                    else:
                        print("WINNER! You completed the game!")
                        return True
        

#-----------------------------------------------------------------------------------

print("Welcome to Hangman!")
print(hangman_0)

random_word = random.choice(word_list)
random_word_length = len(random_word)

#SEPERATE RANDOM WORD INTO [A, B, C] FORMAT
list_word = [random_word[0]]
index_number1 =0
for char in range(0, random_word_length-1):
    index_number1 += 1
    list_word.append(random_word[index_number1])

#PRINT THE WORD WITH '_''S TO SHOW HOW MANY LETTERS ARE NEEDED. ALSO PRINT THE NUMBER OF LETTERS NEEDED
index_number2 = 0
for char in range(0, random_word_length):
    list_word[index_number2] = "_"
    index_number2 += 1
print(f"Your word to guess has {random_word_length} characters:")
print(list_word)

#MAIN BODY OF CODE. WHILE GAME ISN'T YET WON, REPEAT UNTIL 15 TURNS HAVE BEEN TAKEN.

lives = 8
turns = 0

while game_complete() == False:
    if lives > 0:
        
        if turns >= 1:
            print(f"\nNumber of lives left = {lives}")
            print(f"\n{list_word}")

                
        guess = input("\nTry and guess the word by typing a letter! :")
        turns += 1
        

        letter_match = 0
        incorrect_char = 0
        correct_char = 0
        
        for letter in random_word:
            if letter == guess:
                list_word[letter_match] = guess
                letter_match += 1
                correct_char += 1
                if letter_match == random_word_length and correct_char >= 1:
                    print("\nWell done! You got a letter right!")
            elif letter != guess:
                letter_match += 1
                incorrect_char += 1
                if incorrect_char == random_word_length:
                    lives -= 1
                    if lives > 0:    
                        print("\nBad guess. Try Again")
                elif letter_match == random_word_length and correct_char >= 1:
                    print("\nWell done! You got a letter right!")
        
        if lives == 8:
           print(hangman_8)
        elif lives == 7:
           print(hangman_7)
        elif lives == 6:
           print(hangman_6)
        elif lives == 5:
           print(hangman_5)
        elif lives == 4:
           print(hangman_4)
        elif lives == 3:
           print(hangman_3)
        elif lives == 2:
           print(hangman_2)
        elif lives == 1:
           print(hangman_1)
        

    else:
        print("\nYou ran out of lives. GAME OVER")
        print(f"\nThe word was: {random_word}")
        print(hangman_0)
        break
    
# How can I improve this?

#- add a message if you repeat a letter guessed already
#- add an error message if entered anything but a letter
