print("Welcome to my quiz")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0
count = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("you are correct")
  score+=1
  count+=1
else: 
  print("incorrect")
  count+=1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("you are correct")
  score+=1
  count+=1
else: 
  print("incorrect")
  count+=1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("you are correct")
  score+=1
  count+=1
else: 
  print("incorrect")
  count+=1

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
  print("you are correct")
  count+=1
  score+=1
else: 
  print("incorrect")
  count+=1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print("you are correct")
  count+=1
  score+=1
else: 
  print("incorrect")
  count+=1

print("")
print("You got " + str(score) + " questions correct")
print("Your score is " + str((score/5)*100) + "%" )
print("You score " + str(score) + " out of " + str(count) + " questions correct")