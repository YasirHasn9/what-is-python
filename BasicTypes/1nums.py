                         #Numbers -1
'''
There are 2 types of numbers in python
               -Integer 
               -Float (any number has a decimal )
'''

print(5) # == 5
print(5 + 6) # == 11
print("5" + "6") # == 56 why? Basically when you wrap a number with (" ")
                 # python deal with it as a string: "1" + "100" = "1100"
'''
so just try to remember that you don't need to wrap numbers with (" ") when you are dealing 
with mathematician operations
'''

print(2.5) # == 2.5 is floating number
print(2.5 + 2.5) # == 5.0 ? because this is how python works. Once you use floating number
                        #   python will return a floating number 


                         #Converting 
'''
Now lets say that we have a a number that been wrapped in (" " )
      --- How can we convert it to a number ?
       Luckily python has a built-in function that can convert a string to a number 
       (If the string has no other character rather than numbers) 
'''
print(int("65") , int("5") + int("11")) # == 65 ,  16
print(int("B44")) # == error , Invalid , why ?