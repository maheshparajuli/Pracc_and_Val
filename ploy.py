''' The word polymorphism means many forms, and it means methods/functions/operators 
with the same name that can be executed on many objects or classes.

#function polymorphism:
len() function can be used in different objects i.e iterable objects
example:
lst=list(1,2,4,8)
print(len(lst))

#class polymorphism:
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.


#more than simple example

class Teacher():
    def greet(self):
        print("aey budo, namaste hai")
class Student():
    def greet(self):
        print("k xa bro?")
ob1=Teacher()
ob2=Student()

for i in (ob1,ob2):
    i.greet()

#Inheritance Class Polymorphism
nothing but just checking what happens when we define same named methods in parent and child classes, the result is that the child class 
methods can override parent class methods(same name wala)

lets demonstrate with example:

'''
#simple code for my verification.
class School:
    def name(self):
        print("Bright Angels' School, Thankot")
class Student(School):
    def name(self):
        print("Jalakman Gandharba")

obj=School()
obj.name()
c=Student()
c.name()