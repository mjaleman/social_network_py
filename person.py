class Person:
	def __init__(self, username, password, statuses, friends):
		self._username = username
		self._password = password
		self._stauses = statuses
		self._friends = friends

	def get_username(self):
		return self._username

	def get_password(self):
		return self._password

	def get_friends(self):
		return self._friends

	def __repr__(self):
		return str(self._username)

	def __str__(self):
		output = self._username + "'s Friends:" + self._friends
		return output 
