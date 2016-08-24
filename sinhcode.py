class Person:

    # TODO: abc
    
    def haha():
        print('ngungu')

	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
        self.scores = scores
        
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        avg = float(sum(self.scores)/len(sum),1)
        if (avg>=90 and avg <=100):
            print ('O')
        elif (avg>=80 and avg<=90):
            print ('E')
        elif (avg>=70 and avg<=80):
            print ('A')
        elif (avg>=55 and avg<=70):
            print ('P')
        elif (avg>=40 and avg<=55):
            print ('D')
        elif (avg<=40):
            print ('T')

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
