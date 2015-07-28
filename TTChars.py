import types
from TTTraits import *
from TTRolls import *

charList = []

class Character():

	def __init__(self, name, toughness, statList, mainStat, traits, desc,
				 gear = [],
				 notes = [],
				 stAdvantage = {"Exploration" : 1, "combat" : 1}):
		self.name        = name
		self.toughness   = toughness
		self.hpmax		 = 4*toughness
		self.hp			 = self.hpmax
		self.brawn    	 = statList[0]
		self.finesse 	 = statList[1]
		self.mind	     = statList[2]
		self.spirit		 = statList[3]
		self.mainStat	 = mainStat
		self.traits      = traits
		self.desc        = desc
		self.gear        = gear
		self.notes 	     = notes
		self.rolls       = Roller()
		self._dDice      = 1
		self.stAdvantage = stAdvantage
		self.advantage   = self.stAdvantage

		charList.append(self)

	@property
	def statList(self):
		self.statList    = {"brawn":   self.brawn[0],
							"finesse": self.finesse[1],
							"mind":    self.mind[2],
							"spirit":  self.spirit[3]}

	@property
	def traitsVerbose(self):
		output = ""
		for i in range(len(self.traits)):
			output += str(self.traits[i]) + "\n \n"
		return output

	@property
	def stats(self):
		def p(s):
			return s.rjust(8) + str(self.statList[s]).rjust(3) + "\n"
		output  = p("brawn")
		output += p("finesse")
		output += p("mind")
		output += p("spirit")
		return output

	def getall(self, verbose = False):
		output  = self.name + "\n"
		output += self.stats + "\n"
		if verbose == False:
			output += str(self.traits)
		if verbose == True:
			output += self.traitsverbose()
			output += "----- \n"
		output += "\n" + self.desc + "\n" + str(self.notes) + "\n"
		return output

	def roll(self, num = 3, sides = 20, mod = 0, increase = 0):
		return normRoll(num, sides, mod, increase, roller = self.rolls)

	def melee(self, target = None, dice = 1, increase = 0, mod = None):
		if mod == None:
			mod = self.mainStat
		return combatRoll(increase = increase, damsides = dice,
						  roller = self.rolls)
		
	def ranged(self, target = None, dice = 1, increase = 0, mod = None):
		if mod == None:
			mod = self.mainStat
		return combatRoll(increase = increase, damnum = dice, damsides = 6, 
						  roller = self.rolls)

	def __str__(self):
		return self.getall()

pseu = Character ("Pseu", 10, (1, 3, 2, -1), 3, [],
"Pseu is a blue testdragon.")

pseu.traits.append(dragonsBreath)
