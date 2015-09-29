from TTRolls import *

class Trait():
    name = None
    theme = None
    category = None
    desc = None
    action = None
    activation = None
    action = None
    def __init__(self, owner):
        self.owner = owner

    def __repr__(self):
        return self.name
    def __str__(self):
        if self.action == None:
            output = (self.name + '\n' + self.theme + ', ' + self.category +
            '\n')
        else: 
            output = (self.name + '\n' + self.theme + ', ' + self.category + 
            ', ' + self.action + '\n')
        if self.activation == None:
            output = (output + self.desc)
        else:
            output = (output + self.activation + " -> " + self.desc)
        return output
    def __gt__(self, other):
        selfOrder = traitOrder.index(type(self))
        otherOrder = traitOrder.index(type(other))
        if selfOrder > otherOrder:
            return True
        elif otherOrder > selfOrder:
            return False

class DragonsBreath(Trait):
    name = "Dragon's Breath"
    theme = 'Dragon'
    category = "Combat"
    action = 'standalone'
    activation = "Describe how you breathe with draconic fury"
    desc = "deal melee damage in a cone"
    def __call__(self, *args, **kwargs):
        kwargs['roller'] = self.owner.roller
        r = self.combatRoll(args, kwargs)
        out = str(r.log) + "\n in a cone"

class Carnage(Trait):
    name = "Carnage"
    theme = "Dragon"
    category = "Combat"
    action = 'modifies attack'
    desc = """when you spend advantage on an attack, and deal damage, maim the target."""
    def __call__(self,r, out, argsin = None, kwargsin = None, *args, **kwargs):
        argParse(argsin, kwargsin, args, kwargs)

        if kwargs.get('increase', 0) > 0:
            if r.hit.success > 2:
                if r.dam > 0:
                    out += '\nand maim the target'
        return out


traitOrder = [DragonsBreath, Carnage]
#dragonsRoar = Trait("Dragon's Roar", "Dragon", "Combat",
#"Terrify enemies with a midrange distance who hear you, resisting.",
#activation = "Describe how you give a terrifying draconic roar")
#
#stokeTheFurnace = Trait("Stoke The Furnace", "Dragon", "Combat",
#"""Bolster. Your next attack this combat \
#covers about twice as much space as normal.""",
#activation = "Describe how you gather power")
#
#youDare = Trait("You Dare!?", "Dragon", "Combat",
#"""Whenever a creature legitimately offends you \
#(merely damaging you doesn't count), \
#write that creature's name on your list. 
#Increase all rolls you make to achieve horrible revenge \
#against creatures on your list. 
#You can have up to 3 names on your list at a time; \
#you can only remove names of people when they are dead.""")
#
#forTheHoard = Trait("For The Hoard", "Dragon", "Exploration",
#"""choose one:
#COLLECTOR: The GM tells you where to find the most valuable nearby item \
#you don't own, and a relevant fact about it.
#MINE!: The GM tells you exactly where to find a valuable item \
#you touched before.""",
#activation = "Describe how you covet.")
#
#kingOfYourDomain = Trait("King of Your Domain", "Dragon", "Exploration", 
#"increase all rolls you make while in territory you control")
#
#lair = Trait("Lair", "Dragon", "Exploration",
#"""A piece of territory that you control becomes your lair. \
#Gain creative license to slowly change the terrain and features of the lair \
#(create web-strewn paths, clinging ice, pools of magma, etc). \
#At any point, you can ask if someone is trespassing in your lair, \
#and the GM must answer honestly.""",
#activation = "describe how you claim your lair",
#action = "slow action")
#
#territorial = Trait("Territorial", "Dragon", "Exploration",
#"""When you are in another creature's territory, \
#you can ask 3 questions about the territory and its owner, \
#the GM must answer honestly. \
#At any point, you can have the GM tell you \
#what creatures and organizations own which territories in the region, \
#and a relevant fact about each.""")
#
#demandTribute = Trait("Demand Tribute", "Dragon", "Interaction",
#"""If you have a reputation, they freely offer you something useful \
#(valuables, shelter, useful information, etc).""",
#activation = "Describe how you demand tribute from a creature or organization",
#action = "action")
#
#gloryAndSplendor = Trait("Glory and Splendor", "Dragon", "Interaction",
#"""When you gain this trait, work with your GM \
#to determine your social leverage \
#(your family name is widely recognized and respected, \
#you are a celebrity, you're gorgeous, etc). 
#Whenever you decide to use this leverage, \
#non-hostile creatures are significantly more likely \
#to try to appease you.""")
#
#pawnsAndPlaythings = Trait("Pawns and Playthings", "Dragon", "Interaction", 
#"""The GM tells you the ways that the creature could be useful to you.
#Pick one; you gain significant insight \
#of how to gain that creature's goods OR services.""",
#activation = "Describe how you evaluate someone",
#action = "action")
#
#toTheVictor = Trait("To The Victor", "Dragon", "Interaction", 
#"""When you defeat a creature (physically or socially) \
#select something that your foe possesses \
#(followers, territory, respect, etc.)
#it is now lawfully yours.""")
