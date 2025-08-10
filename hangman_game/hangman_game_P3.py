import random
from hangman_game import hangman_list
import hangman_stages
hearts=6
choosen_word=str(random.choice(hangman_list.list1))
display=[]
for i in range(len(choosen_word)):
    display+='_'
print(display)

game_over=False

while not game_over:
    guess_letter=input("Guess a letter:")
    for idx in range(len(choosen_word)):
           letter=choosen_word[idx]
           if letter== guess_letter:
               display[idx]=guess_letter
    print(display)


    if guess_letter not in choosen_word:
        hearts-=1
        print(f"{hangman_stages.stages[hearts]}")
        print(f"you have {hearts} hearts remaining.so try to guess the word")
        if hearts==0:
            print("you loose")
            game_over=True

    if '_' not in display:
        print("you won")
        game_over=True



