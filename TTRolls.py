import random

class Rolls():
	allRolls = []
	def __init__(self):
		self.rolls = []
	def __str__(self):
		out = []
		for i in range(len(self.rolls)):
			out.append(str(self.rolls[i].log))
		return "\n".join(out)
	def append(self, roll):
		self.allRolls.append(roll)
		self.rolls.append(roll)

class normRoll():
	def __init__(self, num = 3, sides = 20, mod = 0, increase = 0):
		self.kind = "normal"
		self.num = num
		self.sides = sides
		self.mod = mod
		self.increase = increase
		self.inputStr = str(self.num)+"n"+str(self.sides)+"+"+str(self.mod)
		if self.increase > 0:
			self.inputStr += "I"
		if self.increase < 0:
			self.inputStr += "D"
		if self.increase == 0:
			self.inputStr += "N"

		self.rollList = [random.randint(0, self.sides) 
						 for x in range(0, self.num)]

		self.result = sorted(self.rollList)[self.increase+1] + self.mod

		if self.result in range(1, 5):
			self.success = 1
			self.successStr = "very bad"
		elif self.result in range(5, 9):
			self.success = 2
			self.successStr = "bad"
		elif self.result in range(9, 13):
			self.success = 3
			self.successStr = "mixed"
		elif self.result in range(13, 17):
			self.success = 4
			self.successStr = "good"
		else:
			self.success = 5
			self.successStr = "very good"
		
		rollLog.append(self)
	@property
	def log(self):
		return str(self.inputStr.ljust(10)+
		           str(self.result).ljust(4)+
		           self.successStr)
	def __str__(self):
		return str(self.result)+", "+str(self.successStr)

class sumRoll():
	def __init__(self, num = 1, sides = 8, mod = 0):
		self.kind = "sum"
		self.num = num
		self.sides = sides
		self.mod = mod
		self.inputStr = str(self.num)+"s"+str(self.sides)+"+"+str(self.mod)
		self.rolls = [random.randint(1, self.sides) 
					  for x in range(0, self.num)]
		self.result = sum(self.rolls)+mod
		
		rollLog.append(self)	
			
	def __str__(self):
		return str(self.result)
	@property
	def log(self):
		return str(self.inputStr.ljust(10)+str(self.result))

def combatRoll(increase = 0, hitmod = 0,  
			   damnum = 1, damsides = 8, dammod = 0):
	hit = normRoll(increase = increase, mod = hitmod)
	if hit.success >= 5:
		damnum += 1
	dam = sumRoll(damnum+increase, damsides, dammod)
	return str(hit.log)+"\n"+str(dam.log)

rollLog = Rolls()
