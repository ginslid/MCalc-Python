
# Each class represents a different subject

class Calculus:

    # calculus receives 4 test grades and 4 assignment grades
    def __init__(self, T1, T2, T3, T4, A1, A2, A3, A4):
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.T4 = T4

        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
    
    # calculates the assignment average grade and returns it
    def meanA(self):
        MA = (self.A1 + self.A2 + self.A3 + self.A4)/4
        return MA
    
    # calculates the test average grade and returns it
    def meanT(self):
        MT = (self.T1 + self.T2 + self.T3 + self.T4)/4
        return MT
    
    # calculates the final grade and returns it rounded to be more readable
    def finalGrade(self):
        meanA = self.meanA() * 0.3
        meanT = self.meanT() * 0.7
        FG = round((meanA + meanT), 2)
        return FG
    
    # print the assignment and test partial grades, the final grade and determines if the student has been approved (final grade >= 6)
    def showResults(self):
        finalGrade = self.finalGrade()
        print("Assignments partial grade: ", self.meanA())
        print("Tests partial grade: ", self.meanT())
        print("Your final grade in calculus is: ", finalGrade)
        if finalGrade >= 6.0 and finalGrade <= 10.0:
            print("Congratulations! You have been approved in Calculus!")
        if finalGrade < 6.0 and finalGrade >= 0.0:
            print("You have not been approved in Calculus!")
        if finalGrade < 0.0 or finalGrade > 10.0:
            print("Something went wrong, please try again")

# this class calculates all the grades the exact same way it happens in the Calculus class, so we inherit all those functions from it
class AGeometry(Calculus):

    # print the assignment and test partial grades, the final grade and determines if the student has been approved (final grade >= 6)
    def showResults(self):
        finalGrade = self.finalGrade()
        print("Assignments partial grade: ", self.meanA())
        print("Tests partial grade: ", self.meanT())
        print("Your final grade in analytic geometry is: ", finalGrade)
        if finalGrade >= 6.0 and finalGrade <= 10.0:
            print("Congratulations! You have been approved in analytic geometry!")
        if finalGrade < 6.0 and finalGrade >= 0.0:
            print("You have not been approved in analytic geometry!")
        if finalGrade < 0.0 or finalGrade > 10.0:
            print("Something went wrong, please try again")

# we inherit the meanT and meanA functions from calculus
class Chemistry(Calculus):
    
    # calculates the final grade and returns it
    def finalGrade(self):
        meanA = self.meanA() 
        meanT = self.meanT() 
        FG = ((meanA + meanT * 2) / 3)
        return FG
    
    # print the assignment and test partial grades, the final grade and determines if the student has been approved (final grade >= 6)
    def showResults(self):
        finalGrade = self.finalGrade()
        print("Assignments partial grade: ", self.meanA())
        print("Tests partial grade: ", self.meanT())
        print("Your final grade in Chemistry is: ", finalGrade)
        if finalGrade >= 6.0 and finalGrade <= 10.0:
            print("Congratulations! You have been approved in Chemistry!")
        if finalGrade < 6.0 and finalGrade >= 0.0:
            print("You have not been approved in Chemistry!")
        if finalGrade < 0.0 or finalGrade > 10.0:
            print("Something went wrong, please try again")

# we inherit the meanT function from calculus
class Physics(Calculus):

     # physics receives 4 test grades and 6 assignment grades
    def __init__(self, T1, T2, T3, T4, A1, A2, A3, A4, A5, A6):
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.T4 = T4

        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.A5 = A5
        self.A6 = A6

    # calculates the assignment partial grade and return it
    def meanA(self):
        MA = ((self.A1 * 0.5) + (self.A2 * 0.5) + (self.A3 * 4) + (self.A4 * 0.5) + (self.A5 * 0.5) + (self.A6 * 4)) * 0.1
        return MA
    
    # calculates the final grade and returns it rounded to be more readable
    def finalGrade(self):
        meanA = self.meanA() * 0.4
        meanT = self.meanT() * 0.6
        FG = round((meanA + meanT), 2)
        return FG
    
    # print the assignment and test partial grades, the final grade and determines if the student has been approved (final grade >= 6)
    def showResults(self):
        finalGrade = self.finalGrade()
        print("Assignments partial grade: ", self.meanA())
        print("Tests partial grade: ", self.meanT())
        print("Your final grade in Physics is: ", finalGrade)
        if finalGrade >= 6.0 and finalGrade <= 10.0:
            print("Congratulations! You have been approved in Physics!")
        if finalGrade < 6.0 and finalGrade >= 0.0:
            print("You have not been approved in Physics!")
        if finalGrade < 0.0 or finalGrade > 10.0:
            print("Something went wrong, please try again")

