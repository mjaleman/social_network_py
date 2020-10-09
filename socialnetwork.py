import csv

import person

usernamelist = []
passwordlist = []

def sortSelection(values):
	for i in range (len(values)):
		minPos = minimumPosition(values, i)
		temp = values[minPos]
		values[minPos] = values[i]
		values[i] = temp

def minimumPosition(values, start):
	minPos = start
	for i in range(start + 1, len(values)):
		if values[i] < values[minPos]:
			minPos = i	
	return minPos

def getusernamelist(usernamelist):
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv.DictReader(csv_file)
		for line in newtwork_reader:
			if line['Username'] not in usernamelist:
				word = line['Username']
				newword = '' + str(word) + ''
				usernamelist.append(newword)
	return usernamelist

def getpasswordlist(passwordlist):
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv.DictReader(csv_file)
		for line in newtwork_reader:
			passwordlist.append(line['Password'])
			if line['Password'] == '':
				passwordlist.remove('')
	return passwordlist

def get_statuses(username):
	templist = []
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv. DictReader(csv_file)
		for line in newtwork_reader:
			if line['Username'] == username:
				templist.append(line['Status Updates'])
				sortSelection(templist)
		if '' in templist:
			templist.remove('')
	return templist

def friends_status(username):
	friendslist = showfriends(username)
	templist = []
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv.DictReader(csv_file)
		for line in newtwork_reader:
			if line['Username'] in friendslist:
				templist.append(line['Status Updates'])
	return templist

def add_status(username):
	userinput = input("New Status: ")
	with open('./network.csv', 'a') as csv_file:
		newtwork_writer = csv.writer(csv_file)
		newtwork_writer.writerow([username, '', userinput, ''])
	print("Status Updated!")

def showfriends(username):
	templist = []
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv.DictReader(csv_file)
		for line in newtwork_reader:
			if line['Username'] == username:
				templist.append(line['Friends'])
		sortSelection(templist)
		if '' in templist:
			templist.remove('')
	return templist

def login(usernamelist, passwordlist):
	print("Welcome to Social X!")
	userinput = input("Would you like to: \n1. Login \nor \n2. Sign Up? \nEnter 1 or 2: ")
	if userinput == "1":
		username = str(input("Enter your username: "))
		if username in usernamelist:
			index = usernamelist.index(username)
			password = input("Please enter your password: ")
			if passwordlist[index] == password:
				print("Logging in")
				mainmenu(username)
			else:
				password = input("Incorrect password! Try again: ")
		elif username not in usernamelist:
			signup_input = input("This username is not in our network. Would you like to sign up?"
				+ " Enter Y for Yes or N for No: ")
			if signup_input.upper() == "Y":
				signup(usernamelist)
			else:
				print("Sorry this username is not in our network try logging in again!")
				login(usernamelist, passwordlist)
	if userinput == "2":
		signup(usernamelist, passwordlist)

def signup(usernamelist, passwordlist):
	username = '@' + input("Enter your desired username: ")
	if username not in usernamelist:
		password = input("Enter your password: ")
		confirm_pass = input("Confirm your password: ")
		if password == confirm_pass:
			with open('./network.csv', 'a') as csv_file:
				newtwork_writer = csv.writer(csv_file)
				newtwork_writer.writerow([username, password, '', ''])
			print("Congrats, you've made an account!")
			mainmenu(username, usernamelist, passwordlist)
		else:
			print("Your password didn't match, Please try again")
			confirm_pass = input("Confirm your password: ")
			if password == confirm_pass:
				with open('./network.csv', 'a') as csv_file:
					newtwork_writer = csv.writer(csv_file)
					newtwork_writer.writerow([username, password, '', ''])
				print("Congrats, you've made an account!")
				mainmenu(username, usernamelist, passwordlist)
			else:
				print("Unable to register")
				login(usernamelist, passwordlist)
	else:
		print("This username is already in user, try another one!")
		signup()

def Add_friend(username):
	friednslist = []
	allusers = []
	with open('./network.csv', 'r') as csv_file:
		newtwork_reader = csv.DictReader(csv_file)
		for line in newtwork_reader:
			if line['Username'] == username:
				friednslist.append(line['Friends'])
		for line in newtwork_reader:
			if line['Username'] not in allusers:
				allusers.append(line['Username'])
		userinput = input("Type in the handle of your friend: ")
		if userinput not in allusers:
			print("Sorry that user is not in our network.")
			mainmenu(username)
		elif userinput in allusers and userinput not in friednslist:
			newtwork_reader.writerow([username, '', '', userinput])
			print("You've added a new friend!")
			mainmenu(username)
		elif userinput in allusers and userinput in friednslist:
			print("User is already your friend!")
			mainmenu(username)

def logout(username):
	print("See you again soon!")
	login(usernamelist, passwordlist)

def mainmenu(username, usernamelist, passwordlist):
	print("Welcome back", username, "the Social X !")
	print("1. Show Previous statuses")
	print("2. Show friend's statuses")
	print("3. Show Friends List")
	print("4. Update your status")
	print("5. Logout")
	userinput = input("Choose an option: ")
	if userinput == "1":
		print(get_statuses(username))
		mainmenu(username, usernamelist, passwordlist)
	if userinput == '2':
		print(friends_status(username))
		mainmenu(username, usernamelist, passwordlist)
	if userinput == '3':
		print(username.get_friends())
	if userinput == '4':
		print(add_status(username))
		mainmenu(username, usernamelist, passwordlist)
	if userinput == '5':
		logout()

def main(usernamelist, passwordlist):
	usernamelist = getusernamelist(usernamelist)
	passwordlist = getpasswordlist(passwordlist)
	print(passwordlist)
	for i in range(len(usernamelist)):
		statuslist = get_statuses(usernamelist[i])
		friendslist = showfriends(usernamelist[i])
		usernamelist[i] = person.Person(usernamelist[i], passwordlist[i], statuslist, friendslist)

	login(usernamelist, passwordlist)


main(usernamelist, passwordlist)
