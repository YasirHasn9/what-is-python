# conditions statements
'''
In programming , its important to know whats true and false because getting to know that helps 
a lot in your logic and how to deal with the truthy values/statements and falsy/statements

Also , this would help a lot on how to write a well shaped algorithm 
      in case of true statement, do something
                 false statement , do something else


so how to write a conditional statements ?
   python provide something called if/else and this not only python most of the languages provide this



how do i use the if/else?

if condition:
    do something
else:
    do something else in case the condition fails
'''
number = 5
if number > 4:
    print("Number is greater than 4")
else:
    print("Number is les than 4")

'''
but what if we have more then one condition to deal with ?
   easy, python provides a way to right more than one condition

if condition_one:
    do something

elif condition_two:
    do something else

elif condition_three:
    do something different 

else:
    if none of the above is true then run the code here
    do something 
'''
# we use multiple elif statement but one else statement and been used at the end
if number > 4:
    print("Number is greater than 4")
if number == 5:
    print("Number is 5")
else:
    print("Number is les than 4")
