import random

class Roller():
    def __init__(self):
        self.rolls = []
    def __str__(self):
        out = []
        for i in range(len(self.rolls)):
            out.append(str(self.rolls[i].log))
        return "\n".join(out)
    def append(self, roll):
        allRolls.append(roll)
        self.rolls.append(roll)

class AllRolls(Roller):
    def append(self, roll):
        self.rolls.append(roll)

allRolls = AllRolls()

worldRolls = Roller()

class normRoll():
    def __init__(self, argsin = None, kwargsin = None, *args, **kwargs):
        self.kind = "normal"
        self.num = 3
        self.sides = 20
        self.mod = 0
        self.increase = 0
        self.roller = worldRolls

        for key in kwargs:
            setattr(self, key, kwargs[key])

        if 'increase' in args:
            self.increase += 1
        if 'decrease' in args:
            self.increase -= 1
        else: self.increase = 0

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
        
        self.roller.append(self)
    @property
    def log(self):
        return str(self.inputStr.ljust(10)+
                   str(self.result).ljust(4)+
                   self.successStr)
    def __str__(self):
        return str(self.result)+", "+str(self.successStr)

class sumRoll():
    def __init__(self, argsin = None, kwargsin = None, *args, **kwargs):
        argParse(argsin, kwargsin, args, kwargs)

        self.kind = "sum"
        self.num = kwargs.get('num', 1)
        self.sides = kwargs.get('sides', 8)
        self.mod = kwargs.get('mod', 0)
        self.roller = kwargs.get('roller', worldRolls)

        self.inputStr = str(self.num)+"s"+str(self.sides)+"+"+str(self.mod)
        self.rolls = [random.randint(1, self.sides) 
                                  for x in range(0, self.num)]
        self.result = sum(self.rolls)+self.mod
        
        self.roller.append(self)     
                    
    def __str__(self):
        return str(self.result)
    def __gt__(self, other):
        if self.result>int(other):
            return True
        elif self.result < int(other): 
            return False
    @property
    def log(self):
        return str(self.inputStr.ljust(10)+str(self.result))


class combatRoll():
    increase = 0
    hitmod = 0
    damnum = 1
    damsides = 8
    dammod = 0
    roller = worldRolls

    def __init__(self, argsin = None, kwargsin = None, *args, **kwargs):
        argParse(argsin, kwargsin, args, kwargs)

        self.damnum = kwargs.get('damnum', 1)

        self.hit = normRoll(args, kwargs)
        if self.hit.success >= 5:
            self.damnum += 1
        self.dam = sumRoll(argsin = args, kwargsin = kwargs)
        kwargs.get('roller', worldRolls).append(self)
    def __str__(self):
        return 'hit: {} \ndam: {}'.format(str(self.hit), str(self.dam))

def argParse(argsin, kwargsin, args, kwargs):
    if argsin:
        args +=argsin
    if kwargsin:
        for key in kwargsin.keys():
            if key not in kwargs.keys():
                kwargs[key] = kwargsin[key]
    return (args, kwargs)
