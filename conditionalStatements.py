"if"
"""
if condition:
    statements

    num = int(input("enter a number.."))
if num>142:
    print("I love you.. ",num)

"""
# write a python program to find whether a number is positive or not 
num = int(input("enter a number: "))
if num>0:
  print("the number is positive",num)
else:
  print("the number is negative",num)

#write a program to find bigest of two numbers

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
if num1>num2:
    print("the biggest number is ",num1) 
else:
    print("the biggest number is ",num2)

# accept the percentage from the user and display the grade according to the following criteria
"""
Below 25 --D
25-45 --C
45-50 --B
50-60 --B+
60-80 --A
above 80 --A+
"""
percentage = int(input("enter percentage: "))
if percentage<25:
    print("your grade is 'D'")
elif percentage>=25 and percentage<45:
    print("your grade is 'C'")
elif percentage>=45 and percentage<50:
    print("your grade is 'B'")
elif percentage>=50 and percentage<60:
    print("your grade is 'B+'")
elif percentage>=60 and percentage<80:
    print("your grade is 'A'")
elif percentage>=80:
    print("your grade is 'A+'")
else:
    print("your failed")

# write a program to display the week names by taking input from the user
"""
1-- SUNDAY
2-- MONDAY
3-- TUESDAY
4-- WEDNESDAY
5-- THURSDAY
6-- FRIDAY
7-- SATURDAY
"""
number = int(input("enter a number: "))
if number ==1:
    print("its SUNDAY")
elif number ==2:
    print("its MONDAY")
elif number ==3:
    print("its TUESDAY")
elif number ==4:
    print("its WEDNESDAY")
elif number ==5:
    print("its THURSDAY")
elif number ==6:
    print("its FRIDAY")
elif number ==7:
    print("its SATURDAY")
else:
    print("wrong input")

# write a progeam to display the monuments according 
"""
delhi-- redfort
agra-- taghmahal
hyderabad-- charminar
chennai-- marina beach
mysore-- ismilla bath
bombay-- gate of india
"""
city = input("emter city: ")
if city == "delhi":
    print("Delhi's monument is RedFort")
elif city == "agra":
    print("Agra's monument is TaghMahal")
elif city == "hyderabad":
    print("Hyderabad's monument is Charminar")
elif city == "chennai":
    print("Chennai's monument is Marina Beach")
elif city == "mysore":
    print("Mysore's monument is Ismila Bath")
elif city == "bonbay":
    print("Bomay's monument is Gate Way Of INDIA")

# accept the number of days from the user and calculate the  charge for library according to the following
"""
till five days: Rs 2/day
six to ten days: Rs 3/day
11 to 15 days: Rs 4/days
after 15 days: Rs 5/days 
"""
num = int(input("enter ur days: "))
if num<5:
    print("the charge is: ",num*2)
elif num>=6 and num<=10:
    print("the charge is: ",num*3)
elif num>=11 and num<=15:
    print("the charge is: ",num*4) 
elif num>15:
    print("the charge is: ",num*5) 
else:
    print("wrong days selected...")

# write a program to accept two numbers from the user an then operator from the user and perform an operation accordingly
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
opr = input("enter a operator: ")
if opr == "+":
    print("your answer is: ",num1+num2)
elif opr == "-":
    print("your answer is: ",num1-num2)
elif opr == "*":
    print("your answer is: ",num1*num2)
elif opr == "/":
    print("your answer is: ",num1/num2)
else:
    print("undefined operator..")

# write a program to accept a number from 1 to 12 and display name of month and days in that month like 
# 1-- jan no of days 31...  
num = int(input("enter a number: "))
if num == 1:
    print("it's JANUARY and number of days are 31")
elif num == 2:
    print("it's FEBUARY and number of days are 28/29")
elif num == 3:
    print("it's MARCH and number od days are 31")
elif num == 4:
    print("it's APRIL and number of days are 30")
elif num == 5:
    print("it's MAY and number of days are 31")
elif num == 6:
    print("it's JUNEand number of days are 30")
elif num == 7:
    print("it's JULY and number of days are 31")
elif num == 8:
    print("it's AUGUST and number of days are 31")
elif num == 9:
    print("it's SEPTEMBER and number of days are 30")
elif num == 10:
    print("it's OCTOBER and number of days are 31")
elif num == 11:
    print("it's NOVEMBER and number of days are 30")
elif num == 12:
    print("it's DECEMBER and number of days are 31")
else:
    print("OOPS! wrong number entered")

# write a program to print "hello" i fa number is entered by user is a multiple of five otherwise print "bye"
num = int(input("entera number: "))
if num%5 == 0:
    print("hello :)")
else:
    print("bye :(")

 # express Delivery
weight = int(input("enter the weight.."))
if weight==4:
    print("the delivery can be expected within 24hrs...")
    if weight<=10:
        print("need to pay an extra amount for extra weight..")
    else:
        print("no need to pay any extra charge have a great delivery!!")
else:
    print("need to wait 3-5 bussiness days to expect the delivery")
    # check the code once 