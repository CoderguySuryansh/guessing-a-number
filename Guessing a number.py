#module to import a random =random.randint(lowerlimit,upperlimit)
import random2
num= random2.randint(1,6)
ctr=0
while ctr<5:
    x=int(input('Guess a number etween 1 to 6:'))
    if x==num:
         print('YOU WON')
         
         break
    else:
        ctr+=1

if not ctr<5:
    print('YOU LOST')
    
    
        
    

