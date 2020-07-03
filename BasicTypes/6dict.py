# Dictionaries
'''
Dictionary is another way of structuring data inside a program using 
curly brackets {} and and you can store data as key/value
{
    key: value 
}
If you wanna access an item inside the the dictionary and you have to do is 
to use the key 
       *** note  ***
       the key should be unique inside the dictionary
'''

person = {
    "first_name": "Jon",
    "last_name": "Doe",
    "age": 29,
    1: "hello"
}
'''
notice that we use quatation marks around the key otherwise can't be done 
because this is not a js lol, however we can use number as key
'''
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person[1])
'''
 we use a [key's name inside the dict to get the value of the key]
'''