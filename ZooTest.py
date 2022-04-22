# Zoo Problem
from ZooAnimal import Bear,Bug,Grass

Bear = Bear()
Bug = Bug()
Grass = Grass()

# for i in range(obj.diet())
#print(obj.diet)
#obj.eats('bug')
#print(obj.diet)

GroupOfZoo = [Bear, Bug, Grass]

while GroupOfZoo:
    
    Length = len(GroupOfZoo)
    HungryAnimal = GroupOfZoo[i]

    if i == 0 and not Length == 1:
        RightChoice = GroupOfZoo[i+1]

        print(repr(HungryAnimal), 'Is Hungry')
        print(HungryAnimal.Test) 

        print(repr(RightChoice), 'is next to', repr(HungryAnimal))
        HungryAnimal.eats(repr(RightChoice))

        if HungryAnimal.Test == True:
                    print(repr(HungryAnimal), 'eats', repr(RightChoice))
        else:
            print(repr(HungryAnimal), 'does not eat', repr(RightChoice))


HungryAnimal.Test = False

RightChoice = GroupOfZoo[2]

print(repr(RightChoice))
HungryAnimal.eats(repr(RightChoice))
print(HungryAnimal.Test)

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
