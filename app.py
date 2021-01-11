#This is an employee account app 
#10/01/2021

#will be employyee account object
class Account(object):
	
	def __init__(self, username, password):
		''' Object constructor '''
		self.username = username
		self.password = password
		#Put this in methods if false denie access
		self.__loggedIn = True
	
	def login(self):
		''' user login '''
		usern = input('Enter a username: ')
		passw = input('Enter a passwrod: ')
		
		if self.username == usern and self.password == passw:
			print(self.username,'You have been logged in')
			self.__loggedIn = True
		else:
			print('ACCESS DENIED')

	def logout(self):
		if self.__loggedIn:
			self.__loggedIn = False
		else:
			print('NOT LOGGED IN')