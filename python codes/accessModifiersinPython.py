#Public, Protected and Private Data Members of a class in python.
class vinay:
	name=None #public member
	_age=None #protected member 
	__rollno=None #private member
	#Constructor
	def __init__(self,name,age,rollno):
		self.name=name
		self._age=age
		self.__rollno=rollno
	#Private member function
	def __showAllMembers(self):
		print("NAME: ",self.name," AGE: ",self._age," ROLL NUMBER: ",self.__rollno)
	def show(self):
		self.__showAllMembers()

class vinaySon(vinay):
	def __init__(self,name,age,rollno):
		vinay.__init__(self,name,age,rollno)

obj= vinaySon("VINAY",21,1613051056)
obj.show()
