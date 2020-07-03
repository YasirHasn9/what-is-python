                        #Strings -2
'''
String  is simply any text you want be treated as text in python
'''
print("Hello world")
'''
 This is a string. How does python know that ?
                   --because it wraps with (" " ) or (' ')
So basically you have 2 option either using single or double quotations

In some case we have to use an apostrophe (')  like the word don't etc ...

if we use the single quotations we will get an error  
'''
# ---> print('don't') # this is invald in python

'''
to fix this we can do this "don't"  we can wrap the text with double quotations and 
use the a single quotation.Also , this works if you want to quote someone but with
 single quotation
              'She said "Khalessi is not coming this winter"' 
'''
print("don't")  # --> this is working
print('She said "Khalessi is not coming this winter"')

'''
But what if inside the quote using another apostrophe 
        'Khalessi said "Don't go to the waterfall"' 

'''
# print('Khalessi said "Don't go to the waterfall"' )# --> this is not working
'''
How can we skip this invalid text?
  Python allows us to use ( / ) before the apostrophe to make the interpreter ignore this  
'''
print('He is said "python isn\'t complier lanague" ')
print("Google what is the difference between complier and interpreter language  ")
