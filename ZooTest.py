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
RightChoice = GroupOfZoo[1]
HungryAnimal = GroupOfZoo[0]

print(HungryAnimal.Test)


HungryAnimal.eats(RightChoice.type)

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
