
from department import Department
from products import Product


class Store:
    # init is working as constructor and initialize the object
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(
            f"Welcome {self.name} , what department do you like to visit ?")

        for d in self.departments:
            print(d.name)


store = Store("The Dugout", [
    Department(1, "Baseball", [
        Product("Kid's bat", 20),
        Product("Bat", 21),
        Product("Cather 's Mitt", 22),
    ]),
    Department(2, "Basketball", [
        Product("Basketball", 40),
        Product("Shorts", 41),
        Product("Jersay", 42),

    ]),
    Department(3, "Football", [
        Product("Helmet", 40),
        Product("Cleats", 42),
    ]),
    Department(4, "Golf", [
        Product("Driver", 440),
        Product("Putter", 441),
        Product("Golf Ball", 442),
    ]),
]
)
# print(store.departments[1].name)

while True:
    store.print_welcome()

    # get the department number the user wants to visit:
    selection = input("Which department would you like to visit? ")

    if selection == "quit":
        break

    chosen_department = store.departments[int(selection) - 1]
    print(f"You picked the {chosen_department.name} department.")
    print('''
    here is the products
    ''')
    chosen_department.print_products()

    print('''

    choose different ones
    
    ''')
