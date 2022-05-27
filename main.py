#from curses.ascii import BEL


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age 
        self.tracks = tracks
        self.score = score

    def myfunction(self):
        print("Hey, this is " + self.name + ".I am " + str(int(self.age)) + " years old. My tracks are " + str(self.tracks) + ", and my score is " + str(float(self.score)))
        print("Please enter new values to be displayed: Name,Age,Track and Score.")
        print("Hey this is " + str(input()) + ".I am " + str(int(input())) + " years old. My tracks are " + str(input()) + ", and my score is " + str(float(input())) )
    
var=Student("Bob" , 26 , ["FE","BE"] , 20.09)
var.myfunction()


 
#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
# Bob.get_score()
