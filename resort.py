import random
print('\t\t\tWelcome to GREEN COCONUT REOSORT')
print('\t\t\t********************************')
room = []
price=[]
rn=[]
r=rs=0
pers=0
p=0
tot=0
order=input("would you like to proceed further(yes/no):")
if order=='yes' or order=='no':
        if order=='yes':
            pass

else:
    order=input('please enter yes or no:')
while order=='yes':
    print('\t\t\t1.BOOKING')
    print('\t\t\t2.ROOM SERVICE')
    
    ch=int(input('->'))
    if ch==1:
        n=str(input('NAME:'))
        p=int(input('MOBILE NO.:'))
        cind=input('DATE OF CHECK-IN:')
        coutd=input('DATE OF CHECK-OUT:')
        night=int(input('number of nights u want to stay:'))
        pers=int(input('enter the number of persons:'))
        print("----ROOM TYPE----")
        print("  Standard Non-AC")
        print("  Standard AC")
        print("  3-Bed Non-AC")
        print("  3-Bed AC")
        print(("Press 0 for Room Prices"))
             
        ch=int(input("->"))
        if ch==0:
                print(" 1. Standard Non-AC - Rs. 3500")
                print(" 2. Standard AC - Rs. 4000")
                print(" 3. 3-Bed Non-AC - Rs. 4500")
                print(" 4. 3-Bed AC - Rs. 5000")
                ch=int(input("->"))
                if ch==1:
                    room.append('Standard Non-AC')
                    print("Room Type- Standard Non-AC")
                    print("---------------------------------------------------------------")
                    print("Room amenities include: 1 Double Bed, Television, Telephone,")
                    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
                    print("an attached washroom with hot/cold water.\n")
                    print("---------------------------------------------------------------")
                    price.append(3500)
                    print("Price- 3500")
                    p=3500
                elif ch==2:
                    room.append('Standard AC')
                    print("Room Type- Standard AC")
                    print("---------------------------------------------------------------")
                    print("Room amenities include: 1 Double Bed, Television, Telephone,")
                    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
                    print("an attached washroom with hot/cold water + Window/Split AC.\n")
                    print("---------------------------------------------------------------")
                    price.append(4000)
                    print("Price- 4000")
                    p=4000
                elif ch==3:
                    room.append('3-Bed Non-AC')
                    print("Room Type- 3-Bed Non-AC")
                    print("---------------------------------------------------------------")
                    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
                    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
                    print("Side table, Balcony with an Accent table with 2 Chair and an")
                    print("attached washroom with hot/cold water.\n")
                    print("---------------------------------------------------------------")
                    price.append(4500)
                    print("Price- 4500")
                    p=4500
                elif ch==4:
                    room.append('3-Bed AC')
                    print("Room Type- 3-Bed AC")
                    print("---------------------------------------------------------------")
                    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
                    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
                    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
                    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
                    print("---------------------------------------------------------------")
                    price.append(5000)
                    print("Price- 5000")
                    p=5000
                else:
                    print(" Wrong choice..!!")
    if ch==2:
         print("-------------------------------------------------------------------------")
         print("                        GREEN COCONUT RESORT")
         print("-------------------------------------------------------------------------")
         print("                            Menu Card")
         print("-------------------------------------------------------------------------")
         print("\n BEVARAGES                              26 Dal Fry................ 140.00")
         print("----------------------------------      27 Dal Makhani............ 150.00")
         print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
         print(" 2  Masala Tea.............. 25.00")
         print(" 3  Coffee.................. 25.00      ROTI")
         print(" 4  Cold Drink.............. 25.00     ----------------------------------")
         print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
         print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
         print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
         print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
         print(" 9  Cheese Toast Sandwich... 70.00")
         print(" 10 Grilled Sandwich........ 70.00      RICE")
         print("                                       ----------------------------------")
         print(" SOUPS                                  33 Plain Rice.............. 90.00")
         print("----------------------------------      34 Jeera Rice.............. 90.00")
         print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
         print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
         print(" 13 Veg. Noodle Soup....... 110.00")
         print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
         print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
         print("                                        37 Plain Dosa............. 100.00")
         print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
         print("----------------------------------      39 Masala Dosa............ 130.00")
         print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
         print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
         print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
         print(" 19 Palak Paneer........... 120.00")
         print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
         print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
         print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
         print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
         print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
         print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
         print('PRESS 0 ONCE YOU ARE DONE WITH YOUR ORDERS')
         
         ch=1
         while(ch!=0):
                     
                    ch=int(input(" -> "))
                     
                    # if-elif-conditions to assign item
                    # prices listed in menu card
                    if ch==1 or ch==31 or ch==32:
                        rs=20
                        r=r+rs
                    elif ch<=4 and ch>=2:
                        rs=25
                        r=r+rs
                    elif ch<=6 and ch>=5:
                        rs=30
                        r=r+rs
                    elif ch<=8 and ch>=7:
                        rs=50
                        r=r+rs
                    elif ch<=10 and ch>=9:
                        rs=70
                        r=r+rs
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                        rs=110
                        r=r+rs
                    elif ch<=19 and ch>=18:
                        rs=120
                        r=r+rs
                    elif (ch<=26 and ch>=20) or ch==42:
                        rs=140
                        r=r+rs
                    elif ch<=28 and ch>=27:
                        rs=150
                        r=r+rs
                    elif ch<=30 and ch>=29:
                        rs=15
                        r=r+rs
                    elif ch==33 or ch==34:
                        rs=90
                        r=r+rs
                    elif ch==37:
                        rs=100
                        r=r+rs
                    elif ch<=41 and ch>=39:
                        rs=130
                        r=r+rs
                    elif ch<=46 and ch>=43:
                        rs=60
                        r=r+rs
                    elif ch==0:
                        pass
                    else:
                        print("Wrong Choice..!!")
         print("Total Bill: ",r)
    order=input('would you like to order anything from our room service(yes/no):')
    if order=='yes' or order=='no':
            pass
    else:
            order=input('please enter yes or no:')
print("your bill for your room is:RS.",p*pers*night)
print("your bill for your food is:RS.",r)
tot=(p*pers*night)+r
print('total amount to be paid   :RS.',tot)
print('to pay through your card please select.....')
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
print('amount to be paid: ',tot)
print('transaction successful!')
rn = random.randrange(40)+300
print('your room no:',rn)
print('your date CHECK-IN:',cind)
print('your date CHECK-OUT:',coutd)
    
print('THANK YOU FOR BOOKING ROOMS WITH US, PLEASE COME AGAIN :)')
print('1.GOOD','2.MODERATE','3.EXCELLENT',sep='/')
rating=int(input('rate your experience with us(enter 1/2/3):'))
other=input('would you like to give any feedback(yes/no):')
if other=='yes':
                    feed=input('your comment here:')
                    print('thank you for your response!')
else:
            print('thank you')

   
            
                
        

