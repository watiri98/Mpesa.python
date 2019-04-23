class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance
	def deposit(self,g):
		deposit = g
		self.balance = self.balance + g
		sms1 = "Dear {},confirmed you have deposited {} kshs in your account.Your Mpesa balance is {}kshs".format(self.name,g,self.balance)
		print(sms1)
	def withdraw(self,h):
		h<self.balance
		self.balance = self.balance - h
		sms2 = "Dear {},confirmed you have withdrawn {} kshs from your account.Your Mpesa balance is {}kshs".format(self.name,h,self.balance)
		print(sms2)
	def check(self):
		balance = self.balance
		sms3 = "Dear {},your current Mpesa balance is{}".format(self.name,self.balance)
		print(sms3)