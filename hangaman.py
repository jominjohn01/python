#step1
import random
import hangman_word
end_of_game=False
#step2
chosen_word=random.choice(hangman_word.word_list)
word_len = len(chosen_word)
lives=6
from hangman_art import logo
print(logo)
display=[]
for _ in range (word_len):
    display+="_"


while not end_of_game:
 guess=input("Guess a letter").lower()
 if guess in display:
     print(f"You have already guess the letter {guess}")
 #Check the position of the letter 
 for poistion in range(word_len):
    letter=chosen_word[poistion]
    if letter==guess:
        display[poistion]=letter
        
 if guess not in chosen_word:
    print(f"You have gussed a wrong letter.You lose a life")
    lives-=1
    if lives==0:
        end_of_game=True
        print("You lose")
    
 print(f"{' '.join(display)}")
 if "_" not in display:
    end_of_game=True
    print("You won")
 from hangman_art import stages
 print(stages[lives])