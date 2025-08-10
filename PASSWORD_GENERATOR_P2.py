import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
         'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',")"]
print("Welcome to password Generator!!!!")
letter_want_user=int(input("Enter how many letters you want in your password"))
num_want_user=int(input("Enter how many numbers you want in your password"))
symbols_want_user=int(input("Enter how many symbols you want in your password"))
password_list=[]
for i in range(1,letter_want_user+1):
   password_list+=random.choice(letters)

for i in range(1,num_want_user+1):
   password_list+=random.choice(numbers)

for i in range(1,symbols_want_user+1):
    password_list+=random.choice(symbols)

random.shuffle(password_list)

password='bhavya'
for CHAR in password_list:
    password+=CHAR

print(password)
