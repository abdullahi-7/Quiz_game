print("welcome to my computer quiz !")

playing = input("do you want to play? ")


if playing.lower() != "yes":
    quit()
    
print("Okay!let's play: )") 
scre = 0
answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print('correct') 
    score =+ 1
else:
    print("incorrect!")
answer = input("what does Gpu stand for?")

if answer.lower() == "graphics processing unit":
    print('correct')
    score =+ 2     
else:
    print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct') 
    score =+ 3    
else:
    print("incorrect!")

answer = input("what does psu stand for?")
if answer.lower() == "power supply":
    print('correct')
    score =+ 4     
else:
    print("incorrect!")

print("You got " + str(score) + "question correct!")
print("You got " + str((score / 4)* 100) + "%")