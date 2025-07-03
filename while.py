"""
Looping  statements are also called iterative statements

these statements are used to run a particualr conditions no of times...
they are broadly dived into two types 
1.while
2.for
"""

# while : it executes when the condition is true 
"""
syntax: while condition :
            statements
            exit condition/incrementation
"""
# eg 
# i=1
# while i<=10:
    # print(i)--->in this particular line the "i" value runs "n" times because na incrementation/exit cound specified
    # print("the value",i)
    # i+=1
# eg2
# while True:
#     print("the while condition")
# note: as default condition is true the while loop runs "infinite times"

# eg3
# while False:
#     print("the while condition")
# as while is also called entry control loop it just checks the cindition in the entrance as default False is given as condition it wont execute

"""
jumping or transfer statements:
these statements are used to control the normal execution of a program they are of "2" types
1.Break :this statements is used to terminate/break the loop 
2.continue: this statements are used to skip current iteration and run the next iteration 
"""
i=1
while i<=10:
    i+=1
    if i==6:
        break   # ternimates/stops the program
    print(i)

i=1
while i<=10:
    i+=1
    if i==6:
       continue  # skips the current iteration an runs the program
    print(i)