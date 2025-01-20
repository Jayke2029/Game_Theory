import random
day_int = 0 ; 
hawk = 50 ; 
dove = 50 ; 
meet = 0 ; 
run_str = input("How long do you want to simulate? (input a number) ") ; 
rep_str = input("How many confrontations per day? (input a number) ") ;
run = int(run_str)
rep = int(rep_str)
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
  day_int + 1
  run = run - 1
  total = hawk + dove
  hawk_percent = hawk / total * 100
  dove_percent = dove / total * 100
  hawk_percent = round(hawk_percent, 2)
  dove_percent = round(dove_percent, 2)
  hawk_percent = str(hawk_percent)
  dove_percent = str(dove_percent)
  day = str(day_int)
  run_str = str(run)
  hawk_str = str(hawk)
  dove_str = str(dove)
  print("Day: " +day+ "  Days left: " + run_str + " ")
  print("Hawks:" +hawk_str+ "  Doves: " + dove_str + " ")
  print("Hawk percent:" + hawk_percent + "%  Dove percent: " + dove_percent + "% ")
  