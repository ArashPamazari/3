araye = []

while True:

    adade_karbar= int(input("adad khod ra vared konid: "))

    araye.append(adade_karbar)

    if adade_karbar == 00:
        break

print(araye)

for i in range(1,len(araye)):
    if i > i-1:
        print('true')
    else:
        print('false')

