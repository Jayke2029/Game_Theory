import random
day = 0 ; 
hawk = 50 ; 
dove = 50 ; 
meet = 0 ; 
run = input("How long do you want to simulate? (input a number) ") ; 
rep = input("How many confrontations per day? (input a number) ") ;
while run > 0 :
  for i in range (rep) : 
    meet = random.randint (1,3) ;
    if meet == 1 :
      dove = dove + 1
    if meet == 2 : 
      for i in range(2):
        surv = random.randint(1,2)
        if surv == 2 :
          hawk = hawk - 1
    if meet == 3 :
      brick = random.randint(1,2)
      hawk = hawk + 1
      if brick == 1:
        dove = dove - 1
  day + 1
  run = run - 1
  total = hawk + dove
  hawk_percent = hawk / total * 100
  dove_percent = dove / total * 100
  print("Day: " +day+ "  Days left: " + run + " ")
  print("Hawks:" +hawk+ "  Doves: " + dove + " ")
  print("Hawk percent:" + hawk_percent + "  Dove percent: " + dove_percent + " ")
  

      



