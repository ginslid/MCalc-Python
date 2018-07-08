import subjects

# This class contain all the menu functions
class Menu:

    # class variable for user input (userInput method will take care of it)
    userInp = None
    # identifier serves to identify if the subject contains 4 or 6 assignment grades
    identifier = None
    # empty list that will be filled with all the grades
    grades = []

    def __init__(self):
        pass
    
    # function that contains the first menu that the user will see
    @classmethod
    def userInput(cls):
        print("Welcome! Select the subject you want")
        print("1 - Calculus")
        print("2 - Analytic Geometry")
        print("3 - Chemistry")
        print("4 - Physics")
        # here we get the input from the user (userInp class variable)
        cls.userInp = int(input("Your input: "))
        # here we assign the identifier based on the user choice (Physics is the only subject with the identifier 6)
        if cls.userInp > 0 and cls.userInp < 4:
            cls.identifier = 4
        if cls.userInp == 4:
            cls.identifier = 6
        if cls.userInp < 1 or cls.userInp > 4:
            print("something went wrong")
        
        # skipping a line to make it more readable to the user
        print()

        # return the user input variable with the value given by the user
        return cls.userInp
   
   # function to get the grades from the user
    @classmethod
    def getter(cls):
        
        # based on the identifier the function asks for the grades (4 -> 4 assignment grades)
        if cls.identifier == 4:
            print("Type your grades for")
            # begins with test grades (subjects.py defines it)
            T1 = float(input("Test 1: "))
            T2 = float(input("Test 2: "))
            T3 = float(input("Test 3: "))
            T4 = float(input("Test 4: "))
            A1 = float(input("Assignment 1: "))
            A2 = float(input("Assignment 2: "))
            A3 = float(input("Assignment 3: "))
            A4 = float(input("Assignment 4: "))

            # adds the input to the grades list defined in the beginning of the class
            cls.grades.extend((T1, T2, T3, T4, A1, A2, A3, A4))
        
        # 6 -> 6 assignment grades
        if cls.identifier == 6:
            print("Type your grades for")
            # begins with test grades (subjects.py defines it)
            T1 = float(input("Test 1: "))
            T2 = float(input("Test 2: "))
            T3 = float(input("Test 3: "))
            T4 = float(input("Test 4: "))
            A1 = float(input("Assignment 1: "))
            A2 = float(input("Assignment 2: "))
            A3 = float(input("Assignment 3: "))
            A4 = float(input("Assignment 4: "))
            A5 = float(input("Assignment 5: "))
            A6 = float(input("Assignment 6: "))

            # adds the input to the grades list defined in the beginning of the class
            cls.grades.extend((T1, T2, T3, T4, A1, A2, A3, A4, A5, A6))

        # skipping a line to make it more readable to the user
        print()

        # return the grades list with the values given by the user
        return cls.grades


    # this function calls the functions from the subjects class
    def caller(self, Inp, grades):
        # (*grades) -> argument unpacking operator
        # unpacks the list values so that the program accepts them as separate values and not as a list
        if Inp == 1:
            grade2 = subjects.Calculus(*grades)
            grade2.showResults()
        if Inp == 2:
            grade2 = subjects.AGeometry(*grades)
            grade2.showResults()
        if Inp == 3:
            grade2 = subjects.Chemistry(*grades)
            grade2.showResults()
        if Inp == 4:
            grade2 = subjects.Physics(*grades)
            grade2.showResults()

