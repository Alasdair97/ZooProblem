from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes

    IsAlive = True
    Test = False
    diet = None
        
    #Constructors
    def __init__(self):
        self.value = "Animal"

    #Methods
    @abstractmethod
    def reproduce(self):
        pass

  #  def diet(self):
  #      pass

    def sleep(self):
        return ("I am sleeping")

    def type(self):
        pass

    def die(self):
        self.IsAlive = False
        return

    def eats(self,Food):
        pass

##################### Mammal #################

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def diet(self):
        pass
    
    def reproduce(self):
        return "Live Birth"

    def type(self):
        pass

    def eats(self,Food):
        pass

################### Bird ####################

class Bird(Animal):
    #Attributes
    wingspan = None

    #Constructors
    def __init__(self):
        self.value = "Bird"


    #Methods
    @abstractmethod
    def diet(self):
        pass
    
    def reproduce(self):
        return "Lay Egg"


    def type(self):
        pass

    def eats(self,Food):
        pass

########################### Mammals ##########################
    
################## antelope
        
class Antelope(Mammal):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "Antelope"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return "grass"

################## Fox
        
class Fox(Mammal):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "Fox"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return "chicken sheep"

################## giraffe
        
class giraffe(Mammal):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "giraffe"

    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return "leaves"

################## bear
        
class Bear(Mammal):
     #Attributes
    diet = list['big_fish','bug','chicken','cow','leaves','sheep']


    #Constructors
    def __init__(self):
        self.value = "Bear"

    def __repr__(self):
        rep = 'Bear'
        return rep


    #Methods
    def type(self):
        return(self.value)

    #def diet(self):
       # return ['big_fish', 'bug' ,'chicken', 'cow', 'leaves' ,'sheep']

    def eats(self,Food):
            if Food in self.diet:
                self.Test = True
                return
            else:
                Test = False

################## Cow
        
class Cow(Mammal):
     #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Cow"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return 'grass'
    
################## Lion
        
class Lion(Mammal):
     #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Lion"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return 'antelope''cow'

################## Panda
        
class Panda(Mammal):
     #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Panda"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return 'leaves'


################## Sheep
        
class Sheep(Mammal):
     #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Sheep"


    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return 'Grass'
    
########################### Birds ##########################
    
################## chicken

class chicken(Bird):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "chicken"

    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return ["bug"]


########################### Others ##########################
    
################## Bug

class Bug(Animal):
     #Attributes
    diet = ['leaves']

    #Constructors
    def __init__(self):
        self.value = "Bug"

    def __repr__(self):
        rep = 'Bug'
        return rep

    #Methods
    def reproduce(self):
        return "Lay Egg"

    def type(self):
        return(self.value)

    def eats(self,Food):
            if Food in self.diet:
                self.Test = True
                return
            else:
                Test = False

## big-fish
class big_fish(Animal):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "big_fish"

    #Methods
    def type(self):
        return(self.value)

    def diet(self):
        return "little_fish"
    
## grass
class Grass(Animal):
     #Attributes
    diet = ['leaves']
    
    #Constructors
    def __init__(self):
        self.value = "grass"

    def __repr__(self):
        rep = 'grass'
        return rep

    #Methods
    def reproduce(self):
        return "Pollonate"
    
    def type(self):
        return(self.value)

    def eats(self,Food):
            if Food in self.diet:
                self.Test = True
                return
            else:
                Test = False
