from abc import ABCMeta,abstractmethod

class Person:
    __metaclass__ = ABCMeta

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def show(self):raise NotImplementedError

class Teacher(Person):
    def __init__(self,name,age):
       Person.__init__(self,name,age)

    def show(self):
        print ("The teacher {} is {} years ago".format(self.name,self.age))

class Student(Person):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        self.id = id 
    def show(self):
        print ("The student at {} is {} and {} years ago".format(self.id,self.name,self.age))

if __name__ == "__main__":
    t = Teacher("p1",25)
    t2 = Student("p2",10,1)
    t2.show()
    t.show()