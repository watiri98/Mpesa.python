class MpesaAccount:
	def __init__(self,name,phone_number):
		self.balance = 0
		self.deposits = []
		self.withdrawals = []
		self.name = name
		self.phone_number = phone_number
		self.loan = 0
		
	def deposit(self,g):
		deposit = g
		self.balance = self.balance + g
		self.deposits.append(deposit)

		sms1 = "Dear {},confirmed you have deposited {} kshs in your account.Your Mpesa balance is {}kshs".format(self.name,g,self.balance)
		print(sms1)
	def withdraw(self,h):
		if h<self.balance:
		   self.balance = self.balance - h
		   self.withdrawals.append(withdraw)
		   sms2 = "Dear {},confirmed you have withdrawn {} kshs from your account.Your Mpesa balance is {}kshs".format(self.name,h,self.balance)
		   print(sms2)
		else:
			print("You have insufficient balance")


	def check(self):
		balance = self.balance
		sms3 = "Dear {},your current Mpesa balance is{}".format(self.name,self.balance)
		print(sms3)
	def my_deposits(self):
		for y in self.deposits:
			print(y)
	def my_withdrawals(self):
		for x in self.withdrawals:
			print(x)

	def give_loan(self,g):
		
		loan=g
		if len (self.deposits)>=5 and g<1/3 * sum(self.deposits) and self.loan==0:
			self.loan = self.loan + g
			print("You are eligible for loan")
		else:
			print("You don't qualify for loan")
	def loan_repayment(self):
		



		

