import random
import time
LINE_UP = '\033[1A'
day_int = 0 ; 
hawk = 50 ; 
dove = 50 ; 
meet = 0 ; 
s1_int = 0
s2_int = 0;
s3_int = 0
res = input("Welcome to my game theory simylation would you like to know how this works? y/n ")
run_str = input("How long do you want to simulate? (input a number) ") ; 
rep_str = input("How many confrontations per day? (input a number) ") ;
qrt_str = input("Chance of Dove reproducing when meeting another dove. EX: 1/(input) ")
wer_str = input("Chance of Hawk dying when meeting another Hawk. EX: 1/(input) ")
qwe_str = input("Chance of Dove dying when meeting a Hawk. EX: 1/(input) ")
run = int(run_str)
qwe = int(qwe_str)
wer = int(wer_str)
qrt = int(qrt_str)
rep = int(rep_str)
while run > 0 :
  for i in range (rep) : 
    meet = random.randint (1,3) 
    if meet == 1 :
      s1_int = s1_int + 1
      chee = random.randint (1,qrt)
      if chee == 1 :
        dove = dove + 1 
    if meet == 2 : 
      s2_int = s2_int + 1
      for i in range(2):
        surv = random.randint(1,wer)
        if surv == 1 :
          hawk = hawk - 1 
    if meet == 3 :
      s3_int = s3_int + 1
      brick = random.randint(1,qwe)
      hawk = hawk + 1 
      if brick == 1:
        dove = dove - 1
  day_int = day_int + 1
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
  s1 = str(s1_int)
  s2 = str(s2_int)
  s3 = str(s3_int)
  if s1_int == 0 :
    print("Dove met Dove 1 time")
  else : 
    print("Dove met Dove " +s1+ " times")
  if s2_int == 0 :
    print("Hawk met Hawk 1 time ")
  else :
    print("Hawk met Hawk " +s2+ " times")
  if s3_int == 0 :
    print("Hawk met Dove 1 time")
  else :
    print("Hawk met Dove " +s3+ " times")
  print("Day: " +day+ "  Days left: " + run_str + " ")
  print("Hawks:" +hawk_str+ "  Doves: " + dove_str + " ")
  print("Hawk percent:" + hawk_percent + "%  Dove percent: " + dove_percent + "% ")
  for x in range(19):
    print("Progress: {:.1%}".format(x / 18 ), end="\r") # GABRIEL ZANE RODRIGUEZ participated
    time.sleep(0.5)
  s1_int = 0
  s2_int = 0
  s3_int = 0
