link="www google.com"
print(link[:3])
print(link[4:-4])
print(link[-4:])
print(link[:3],link[4:],sep='')
str = 'HshHhshjHSJDjsbdjBSHDBhb'
for bukva in str:
    if bukva.islower() == True:
        print(bukva.upper(),end='')
    else:
        print(bukva.lower(),end='')
