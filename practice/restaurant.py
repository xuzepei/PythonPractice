class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def description(self):
        print(self.name + ': ' + self.cuisine)

    def open(self):
        print("Now our restaurant is opened.")


temp = Restaurant("Food", "Chinese")
temp.description()
temp.open()