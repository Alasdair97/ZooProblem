# Zoo Problem
from ZooAnimal import Bear,Bug,Grass

Bear = Bear()
Bug = Bug()
Grass = Grass()

# for i in range(obj.diet())
#print(obj.diet)
#obj.eats('bug')
#print(obj.diet)

#small test group
GroupOfZoo = [Bug, Bear, Grass]
i = 0

Stop = 1

while Stop == 1:
    
    Length = len(GroupOfZoo)
    
    HungryAnimal = GroupOfZoo[i]
    print(i)
    
    if i != 0: #Branch: Eat Left if not on far left
        LeftChoice = GroupOfZoo[i-1]

        print(repr(HungryAnimal), 'Is Hungry')
        #print(HungryAnimal.Test)
        print('A')

        print(repr(LeftChoice), 'is next to', repr(HungryAnimal))
        HungryAnimal.eats(repr(LeftChoice))

        if HungryAnimal.Test == True: #Eat and del victim from array
                    print(repr(HungryAnimal), 'eats', repr(LeftChoice))
                    LeftChoice.die
                    del GroupOfZoo[i-1]
                    HungryAnimal.Test = False
                    print('B')
        elif HungryAnimal.Test == False: #Cant eat left
            print(repr(HungryAnimal), 'does not eat', repr(LeftChoice))
            i = i + 1
            print('F')
            if i == Length: #Branch: Try to eat left but can't and at end of list
             Stop = 2
            
    elif i == 0 and not Length == 1:
        RightChoice = GroupOfZoo[i+1]

        print(repr(HungryAnimal), 'Is Hungry')
        #print(HungryAnimal.Test)
        print('C')

        print(repr(RightChoice), 'is next to', repr(HungryAnimal))
        HungryAnimal.eats(repr(RightChoice))

        if HungryAnimal.Test == True:
                    print(repr(HungryAnimal), 'eats', repr(RightChoice))
                    RightChoice.die
                    del GroupOfZoo[i+1]
                    print('D')
                    HungryAnimal.Test = False
        elif HungryAnimal.Test == False:
            print(repr(HungryAnimal), 'does not eat', repr(RightChoice))
            i = i + 1
            print('E')

print('Animals left')    
print(GroupOfZoo)       
            

            


'''
GroupOfZoo = [Bear, Bug, Grass]

for i in GroupOfZoo:
    GroupOfZoo[i] = HungryAnimal

    if i = 0:
        GroupOfZoo[i+1] = RightChoice
        HungryAnimal.eats(RightChoice.type)
        if HungryAnimal.Test == True
            RightChoice.die()
        else
         pass           
 '''   
