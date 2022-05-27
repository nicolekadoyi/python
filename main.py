#from curses.ascii import BEL


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age 
        self.tracks = tracks
        self.score = score

    def myfunction(self):
        print("Hey, this is " + self.name)
        print("I am " + str(int(self.age)) + "years old." )
        print("My track is " + str(self.tracks))
        print("And my score is " + str(float(self.score)))
        
        print("Please enter new values to be displayed: Name,Age,Track an score.")
        
        print("Hey this is " + str(input()))
        print("I am " + str(int(input())) + " years old.")
        print("My track is " + str(input()))
        print("And my score is " + str(float(input())) )
    
bob=Student("Bob" , 26 , "FE,BE" , 20.09)
bob.myfunction()

#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
