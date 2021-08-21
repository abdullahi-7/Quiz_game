import time
print("my name is Abdullahi.\nI use python to write it.\nwelcome to use it")

quiz = input("do you want to play?").lower()
quiz1 = "yes"

if quiz == quiz1:
    print("let start game")
else:
    print("you are done")    
    quit()


score = 0    
variable = input("how many planets in the soler sistem?")
variable1 = 8

if variable == str(variable1):
    print("correct")
    score =+ 1
else:
    print("wrong")    

question = int(input("how many legs are you have?"))
answer = 2

if question == answer:
    print("correct")
    score =+ 1
else:
    print("wrong")    
question1 = input("Three take away one?\nTwo or one ").lower()
answer1 = "no"

if question1 == answer1:
    print("correct")
    score =+ 1
else:
    print("wrong")    
       
legs = input("itis rainy today?").capitalize()
leg = False

if legs == str(leg):
    print("correct")
    score =+ 1
else:
    print("wrong")    
    
playing = input("itis sunny today?").capitalize()
play = True

if playing == str(play):
    print("correct")
    score =+ 1
else:
    print("wrong")
    
quiz5 =int(input("five take away two?"))
quiz3 = 3

if quize5 == quiz3:
    score =+ 1
    print("correct")
else:
    print("incorrect")

shop = input("you want milk?")
shoping = "yes"

if shop == shoping:
    score = score + 1
    print("you correct")
else:
    print("incorrect")

book = int(input("four take away two?"))
books = 2

if book == books:
    score =+ 1
    print("incorrect")
else:
    print("correct")

pen = input("itis cluody today?").capitalize()
pens = False

if pen =! pens:
    print("incorrect")
else:
    print("correct")
    score =+ 1

print("you got " + str(score) + " marks")    
print("you are done plese wait for 5...seconds")

time.sleep(5)