print('welcome to SVP!')
num1=num2=num3=num4=num5=num6=num7=num8=num9=num10=num11=0
order=input("would you like to order something(yes/no):")
if order=='yes' or order=='no':
        if order=='yes':
            pass
else:
    order=input('please enter yes or no:')
while order=='yes':
    print('menu:','categories:','1.BREAKFAST','2.LUNCH','3.DINNER',sep='\n')
    menu=int(input('enter the number of your preffered category: '))

    if menu==1:
        while order=='yes':
                print("IN BREAKFAST :")
                print('1.idli-RS.10','2.dosa','3.pongal-RS.40',sep='\n')
                bf=int(input('enter the number of the product you would like to see: '))
                if bf==1:
                    print('you have selected idli')
                    num1=int(input('enter the number of idlis'))
                    a='idli-RS.10'
                if bf==2:
                    print('1.plain dosa :RS.20','2.masala dosa:RS.30',
                          '3.onion rava dosa:RS.45',sep='\n')
                    dosa=int(input('enter the number of your choice from the above options: '))
                    if dosa==1:
                            print("you have selected plain dosa")
                            num2=int(input("enter the no.of plain dosa you need: "))
                            b='plain dosa :RS.20'
                    if dosa==2:
                            print("you have selected masala dosa")
                            num3=int(input("enter the no.of masala dosa you need: "))
                            c='masala dosa:RS.30'
                    if dosa==3:
                            
                            num4=int(input("enter the no.of onion rava dosa  you need: "))
                            d='onion rava dosa:RS.45' 
                if bf==3:
                    num5=int(input('enter the number of pongal:'))
                    e='pongal-RS.40'
                order=input("would you like to order some more in breakfast(yes/no):")
                if order=='yes' or order=='no':
                        pass
                else:
                    order=input('please enter yes or no:')
    if menu==2:
            while order=='yes':
                print("IN LUNCH:")
                print('1.mini meals-RS.192','2.full meals-RS.235','3.veg fried rice-RS.207',sep='\n')
                lunch=int(input('enter the number of the product you would like to see: '))
                if lunch==1:
                    num6=int(input('enter the number of mini meals you need: '))
                    f='mini meals-RS.192'
                    
                if lunch==2:
                   num7=int(input('enter the number of full meals you need: '))
                   g='full meals-RS.235'
                if lunch==3:
                   num8=int(input('enter the number of veg fried rice you need: '))
                   h='veg fried rice-RS.207'
                order=input("would you like to order some more in lunch (yes/no):")
                if order=='yes' or order=='no':
                        pass
                else:
                    order=input('please enter yes or no:')
    if menu==3:
            while order=='yes':
                print('IN DINNER:')
                print('1.chapathi-RS.15','2.pizza-RS.392','3.noodles-RS.290',sep='\n')
                dinner=int(input('enter the number of the product you would like to see: '))
                if dinner==1:
                    num9=int(input('enter the number of chapathi you need: '))
                    i='chapathi-RS.15'
                if dinner==2:
                    num10=int(input('enter the number of pizza you need: '))
                    j='pizza-RS.392'
                if dinner==3:
                   num11=int(input('enter the number of noodles you need: '))
                   k='noodles-RS.290'
                order=input("would you like to order some more in dinner(yes/no):")
                if order=='yes' or order=='no':
                        pass
                else:
                    order=input('please enter yes or no:')
    order=input('would you like to order something from other sections(yes/no):')
    if order=='yes' or order=='no':
            pass
    else:
            order=input('please enter yes or no:')
print('--------------------------------------------------------------------------------')
print('dear customer you have ordered:')
print('food item:','no.of items',sep='\t\t\t\t\t\t')
if num1>0:
        print(a,'\t\t\t\t\t\t',num1)
if num2>0:
        print(b,'\t\t\t\t\t\t',num2)
if num3>0:
        print(c,'\t\t\t\t\t',num3)
if num4>0:
        print(d,'\t\t\t\t\t',num4)
if num5>0:
        print(e,'\t\t\t\t\t\t',num5)
if num6>0:
        print(f,'\t\t\t\t\t',num6)
if num7>0:
        print(g,'\t\t\t\t\t',num7)
if num8>0:
        print(h,'\t\t\t\t\t',num8)
if num9>0:
        print(i,'\t\t\t\t\t\t',num9)
if num10>0:
        print(j,'\t\t\t\t\t\t',num10)
if num11>0:
        print(k,'\t\t\t\t\t\t',num11)
bill=(num1*10)+(num2*20)+(num3*30)+(num4*45)+(num5*40)+(num6*192)+(num7*235)+(num8*207)+(num9*15)+(num10*392)+(num11*290)
print('--------------------------------------------------------------------------------')
print('total bill payable:\t\t\t\t     RS.',bill)
print('--------------------------------------------------------------------------------')
payment=input('would you like to pay through card/cash:')
if payment=='card':
        card=int(input('1.debit card/2.credit card /3.UPI-(enter the number):'))
        if card==1 or card==2:
                print('1.ICIC','2.SBI','3.CANARA BANK',sep='\n')
                bank=int(input('select your preferred bank(enter the number): '))
                if bank==1 or bank==2 or bank==3:

                        if bank==1:
                                print('you have selected ICIC bank:')
                                un=input('enter your user name:')
                                pwd=input('enter your password:')
                                pin=input('enter your pin.no:')
                        if bank==2:
                                print('you have selected SBI bank:')
                                un=input('enter your user name:')
                                pwd=input('enter your password:')
                                pin=input('enter your pin.no:')
                        if bank==3:
                                print('you have selected CANARA bank:')
                                un=input('enter your user name:')
                                pwd=input('enter your password:')
                                pin=input('enter your pin.no:')
        if card==3:
               print('1.ICIC','2.SBI','3.CANARA BANK',sep='\n')
               bank=int(input('select your preferred bank(enter the number): '))
               if bank==1 or bank==2 or bank==3:

                        if bank==1:
                                print('you have selected ICIC bank:')
                                 
                        if bank==2:
                                print('you have selected SBI bank:')
                                
                        if bank==3:
                                print('you have selected CANARA bank:')
                              
               upi=input('enter your UPI number:')
        print('amount to be paid: ',bill)
        print('transaction successful!')
        print('dear customer your order has been placed successfully!')
if payment=='cash':
          print('you have selected cash on delivery:')             
          print('amount to be paid: ',bill)
          print('dear customer your order has been placed')
print('THANK YOU FOR SHOPPING WITH US, PLEASE COME AGAIN :)')
print('1.GOOD','2.MODERATE','3.EXCELLENT',sep='/')
rating=int(input('rate your experience with us(enter 1/2/3):'))
other=input('would you like to give any feedback(yes/no):')
if other=='yes':
        feed=input('your comment here:')
print('thank you for your response!')
