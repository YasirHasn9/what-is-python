class Store:

    # init is working as constructor and initialize the object
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(
            f"Welcome to {self.name} , what department do yoi like to visit ?")

        for d in self.departments:
            print(d.name)


class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"


store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", []),
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
