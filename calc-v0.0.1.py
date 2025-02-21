def calc():
 print ("please enter first number : ")
 number1 = int(input())
 print ("please enter second number : ")
 number2 = int(input())
 print ("""please enter 1 for sum : 
  please enter 2 for sub :
  please enter 3 for div :
  please enter 4 for mult :
        """)
 mark = input()
 sum = int(number1+number2)
 sub = int (number1-number2)
 div = float (number1/number2)
 mult = float (number1*number2) 
 if mark == "1" :
  print (sum)
 elif mark == "2" :
   print (sub)
 elif mark == "3" :
   print (div)
 elif mark == "4" :
   print (mult)
 else :
  print ("wrong choice try again")
  calc()
calc()