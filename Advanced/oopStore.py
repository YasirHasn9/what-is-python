'''
How to build a store ?
  what the store needs to be store ?
     who deal with store ?
        what the store contains ?



store's needs :
  a.users
    1.customers
    2.vendors
    3.admins
  b.product
  c.parchases




A.Users
 -attributes
  1.name 
  2. is the user admin?
    customer:
       -attributes
        1.name
        2.purchases
    vendors:
    -attributes
        1.name
        2.products
    admin:
    -attributes
        1.name
        2.the user is an admin
'''


class User:
    # each user needs name and is he is a an admin or not ?
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


# there is 3 types of users
# 1.customer
class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []

# 2.venders


class Vender(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []


# 3.Admin
class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)


'''
B.Products
   -- attribute
     1.name
     2.price
     3.vender 


C.Purchases
 -- attribute
     1.Products
     2.customer
     3.price
     4.date and time info about when the purchase was completed
'''
