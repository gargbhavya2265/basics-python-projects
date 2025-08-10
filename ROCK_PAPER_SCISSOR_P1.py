import random
print("Let's Play Rock Paper and Scissor!!!")
u_choice=int(input("Enter 0 for rock, 1 for paper, 2 for scissor?"))
c_choice =random.randint(0,2)
print(f"computer input is {c_choice}")
if u_choice==c_choice:
    print(" ITS A DRAW")
elif u_choice==c_choice+1:
    print("YOU WIN")
elif u_choice==c_choice-1:
    print("YOU LOOSE")
elif u_choice==c_choice-2:
    print("YOU WIN")
elif u_choice==c_choice+2:
    print("YOU LOOSE")
else:
    print("invalid input")