"""
Class: A blueprint/template used to build objects

Object: A combination of data and functionality; An instance of a class

State: Data associated with an object, assigned through attributes

Behavior: An object's functionality, defined through methods 
"""



class Student:
    clzname="kathmandu University"

    def __init__(self,name,registr_no,school_name,exam_roll,course_code):
        self.name=name
        self.registr_no=registr_no
        self.school_name=school_name
        self.exam_roll=exam_roll
        self.course_code=course_code


    def printall(self):
        print( self.name,
        self.registr_no,
        self.school_name,
        self.exam_roll,
        self.course_code,sep="\n")
        

m1=Student("Arjun Parajuli","0222233356780900098744-71","KUSOS","8066","MATH452")
m1.printall()