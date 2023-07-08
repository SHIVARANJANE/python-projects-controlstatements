print('BUDGET PLANNER')
oh=mo=groc=food=ie=hm=cloth=te=med=pet=ent=0
salary=int(input('enter your monthly income:'))
print('enter the details of your monthly expenses for the below cases:')
det=input('do you live in ur own house or a mortgaded house:')
if det=='own house':
    oh=int(input('home loan:'))
if det=='mortgaged':
    mo=int(input('house rent:'))
groc=int(input('groceries:'))
food=int(input('food(outside):'))
ie=int(input('irregular expenses and emergency fund:'))
hm=int(input('household maintanance:'))
cloth=int(input('clothing:'))
te=int(input('travel expenses:'))
med=int(input(' regular medical expenses:'))
p=input('do you have a pet(yes/no):')
if p=='yes':
    pet=int(input('pet maintanance:'))
ent=int(input('entertainment:'))
totmon=oh+mo+groc+food+ie+hm+cloth+te+med+pet+ent
print('your total monthly expenses:',totmon)
sav=salary-totmon
print('total amount you could save each month:',sav)
savy=sav*12
print('total amount you could save in a year:',savy)



                 
