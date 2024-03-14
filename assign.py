class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Accept input for attributes
name = input("Enter the person's name: ")
age = int(input("Enter the person's age: "))
gender = input("Enter the person's gender: ")

# Create an instance of the Person class with the input values
person1 = Person(name, age, gender)

# Call the introduce method to display the person's information
person1.introduce()
