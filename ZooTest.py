# Zoo Problem
from ZooAnimal import Antelope, Big_Fish, Bear, Bug, Chicken, Cow, Fox, Giraffe, Leaves, Lion, Grass, Sheep

Bear = Bear()
Bug = Bug()
Grass = Grass()
Antelope = Antelope()
Big_Fish = Big_Fish()
Chicken = Chicken()
Cow = Cow()
Fox = Fox()
Giraffe = Giraffe() 
Leaves = Leaves()
Lion = Lion()
Sheep = Sheep()

#test group
#GroupOfZoo = [Lion,Antelope,Bug, Bear, Grass,Fox]
#Question Group
GroupOfZoo = [Fox, Bug, Chicken, Sheep]



print('Starting Animals:')
print(GroupOfZoo)

i = 0
Stop = []

while Stop == []:
    
    Length = len(GroupOfZoo)
    
    HungryAnimal = GroupOfZoo[i]

    if i == 0 and not Length == 1: #First loop
        
        RightChoice = GroupOfZoo[i+1]
        HungryAnimal.eats(repr(RightChoice))

        if HungryAnimal.Test == True:
            
            print(repr(HungryAnimal), 'eats', repr(RightChoice))
            RightChoice.die
            del GroupOfZoo[i+1]
            HungryAnimal.Test = False
            
        elif HungryAnimal.Test == False:
        
            i = i + 1

    elif i ==0 and Length == 1: #Last animal standing

        Stop = 2
        
    elif i != 0 and i == Length-1: #Last loop
        
        LeftChoice = GroupOfZoo[i-1]
        HungryAnimal.eats(repr(LeftChoice))

        if HungryAnimal.Test == True: #Eat and del victim from array try eat left again
            
            print(repr(HungryAnimal), 'eats', repr(LeftChoice))
            LeftChoice.die
            del GroupOfZoo[i-1]
            HungryAnimal.Test = False
            
        if HungryAnimal.Test == False: #Can not eat left so end

            Stop = 2

    elif i != 0 and i != Length-1: #mid loops
        
        LeftChoice = GroupOfZoo[i-1]
        HungryAnimal.eats(repr(LeftChoice))

        if HungryAnimal.Test == True: # Eat left and del victim from array
                
                print(repr(HungryAnimal), 'eats', repr(LeftChoice))
                LeftChoice.die
                del GroupOfZoo[i-1]
                HungryAnimal.Test = False
                i = 0
                    
        elif HungryAnimal.Test == False: # Can not eat left so try right
            
                RightChoice = GroupOfZoo[i+1]
                HungryAnimal.eats(repr(RightChoice))

                if HungryAnimal.Test == True: #Eat animal on right
                    
                    print(repr(HungryAnimal), 'eats', repr(RightChoice))
                    RightChoice.die
                    del GroupOfZoo[i+1]
                    HungryAnimal.Test = False
                    
                elif HungryAnimal.Test == False: # Move to next animal

                    i = i + 1

print('Animals left:')    
print(GroupOfZoo)       
        
