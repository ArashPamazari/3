import random

araye=[]

n = int(input('tedad adad ro vared konid: '))

for i in range(n):
    adad = random.randint(1,30)
    if adad not in araye:
        araye.append(adad)

print(araye)    
