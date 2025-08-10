alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z',]

display=""
def encryption(message,shift_number,display):
    for char in message:
        if char==' ':
            display+=' '
            continue
        idx=alphabet.index(char)
        new_idx=(idx+shift_number)%26
        display+=alphabet[new_idx]
    print(display)

def decryption(message,shift_number,display):
    for char in message:
        if char==' ':
            display+=' '
            continue
        idx=alphabet.index(char)
        new_idx=(idx-shift_number)%26
        display+=alphabet[new_idx]
    print(display)

wanna_over=False
while not wanna_over:
    choice = input("Type 'encrypt' for encryption, Type 'decrypt' for decryption")
    message = input("Type a message")
    shift_number = int(input("type the shift number"))
    if choice=='encrypt':
        encryption(message,shift_number,display)
    elif choice=='decrypt':
        decryption(message,shift_number,display)
    else:
        print("invalid input")

    game_over=input("enter yes to play again and no to quit")
    if game_over=='yes':
        wanna_over=False
    else:
        wanna_over=True
        print("game over")
