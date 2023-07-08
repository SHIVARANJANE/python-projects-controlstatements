print('welcome to amazon!')
num1=num2=num3=num4=num5=num6=num7=num8=num9=num10=num11=num12=num13=num14=num15=num16=num17=num18=num19=num20=num21=num22=num23=num24=0
order=input("would you like to order something(yes/no):")
if order=='yes' or order=='no':
        if order=='yes':
            pass

else:
    order=input('please enter yes or no:')
while order=='yes':
    print('menu:','categories:','1.women','2.men','3.electronics',sep='\n')
    menu=int(input('enter the number of your preffered category: '))

    if menu==1:
        while order=='yes':
                print("IN WOMEN'S SECTION:")
                print('1.tees','2.pantaloons','3.beauty essentials',sep='\n')
                women=int(input('enter the number of the product you would like to see: '))
                if women==1:
                    print("1.women's solid black tee :RS.399","2.women's solid white tee :RS.399",
                          "3.women's printed green tee :RS.499",sep='\n')
                    tee=int(input('enter the number of your choice from the above options: '))
                    if tee==1 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected women's solid black tee")
                         print('--------------------------------------------------------------------------------')
                         num1=int(input("enter the no.of items you need: "))
                         a="women's solid black tee :RS.399"
                    if tee==2 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected women's solid white tee")
                         print('--------------------------------------------------------------------------------')
                         num2=int(input("enter the no.of items you need: "))
                         b="women's solid white tee :RS.399"
                    if tee==3 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected women's printed green tee")
                         print('--------------------------------------------------------------------------------')
                         num3=int(input("enter the no.of items you need: "))
                         c="women's printed green tee :RS.499"
                
                if women==2:
                    print('1.flared jeans :RS.499','2.track pants :RS.399',sep='\n')
                    pantaloons=int(input('enter the number of your choice from the above options: '))
                    if pantaloons==1:
                            print('--------------------------------------------------------------------------------')
                            print("you have selected flared jeans")
                            print('--------------------------------------------------------------------------------')
                            print('available colors:','1.black','2.grey','3.blue',sep='\n')
                            color=int(input('enter the number of the color you want to choose :'))
                            num4=int(input("enter the no.of items you need: "))
                            d='flared jeans :RS.499'
                    if pantaloons==2:
                            print("you have selected track pants")
                            print('available colors:','1.black','2.grey','3.blue',sep='\n')
                            color=int(input('enter the number of the color you want to choose :'))
                            num5=int(input("enter the no.of items you need: "))
                            e='track pants :RS.399'
                if women==3:
                    print('1.moisturizer-RS.199','2.sunscreen-RS.399','3.lip balm-RS.199',sep='\n')
                    bs=int(input('enter the number of your choice from the above options: '))
                    if bs==1:
                        print('--------------------------------------------------------------------------------')
                        print('you have selected moisturizer!')
                        print('--------------------------------------------------------------------------------')
                        print('brands available:','1.DOT AND KEY','2.LAKME',sep='\n')
                        brand=int(input('enter the number of your choice from the above options:'))
                        num6=int(input("enter the no.of items you need: "))
                        f='moisturizer-RS.199'
                    if bs==2:
                        print('--------------------------------------------------------------------------------')
                        print('you have selected sunscreen!')
                        print('--------------------------------------------------------------------------------')
                        print('brands available:','1.DOT AND KEY','2.LAKME',sep='\n')
                        brand=int(input('enter the number of your choice from the above options:'))
                        num7=int(input("enter the no.of items you need: "))
                        g='sunscreen-RS.399'
                    if bs==3:
                        print('--------------------------------------------------------------------------------')
                        print('you have selected lip balm!')
                        print('--------------------------------------------------------------------------------')
                        print('brands available:','1.DOT AND KEY','2.LAKME',sep='\n')
                        brand=int(input('enter the number of your choice from the above options:'))
                        num8=int(input("enter the no.of items you need: "))
                        h='lip balm-RS.199'
                order=input("would you like to order some more in women's section(yes/no):")
                if order=='yes' or order=='no':
                        pass
                else:
                    order=input('please enter yes or no:')
    if menu==2:
            while order=='yes':
                print("IN MEN'S SECTION:")
                print('1.tees','2.pantaloons','3.shirt',sep='\n')
                men=int(input('enter the number of the product you would like to see: '))
                if men==1:
                    print("1.men's solid black tee :RS.399","2.men's solid white tee :RS.399",
                          "3.men's solid green tee :RS.499",sep='\n')
                    tee=int(input('enter the number of your choice from the above options: '))
                    if tee==1 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected men's solid black tee")
                         print('--------------------------------------------------------------------------------')
                         num9=int(input("enter the no.of items you need: "))
                         i="men's solid black tee :RS.399"
                    if tee==2 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected men's solid white tee")
                         print('--------------------------------------------------------------------------------')
                         num10=int(input("enter the no.of items you need: "))
                         j="men's solid white tee :RS.399"
                    if tee==3 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected men's solid green tee")
                         print('--------------------------------------------------------------------------------')
                         num11=int(input("enter the no.of items you need: "))
                         k="men's solid green tee :RS.499"
                if men==2:
                    print('1.full pants :RS.499','2.trousers :RS.399',sep='\n')
                    pantaloons=int(input('enter the number of your choice from the above options: '))
                    if pantaloons==1:
                            print('--------------------------------------------------------------------------------')
                            print("you have selected full pants")
                            print('--------------------------------------------------------------------------------')
                            print('available colors:','1.black','2.grey','3.blue',sep='\n')
                            color=int(input('enter the number of the color you want to choose :'))
                            num12=int(input("enter the no.of items you need: "))
                            l='full pants :RS.499'
                    if pantaloons==2:
                            print("you have selected trousers")
                            print('available colors:','1.black','2.grey','3.blue',sep='\n')
                            color=int(input('enter the number of the color you want to choose :'))
                            num13=int(input("enter the no.of items you need: "))
                            m='trousers :RS.399'
                if men==3:
                        print('1.checked shirts-RS.299','2.plain shirts-RS.199',sep='\n')
                        shirt=int(input('enter the number of your choice from the above options: '))
                        if shirt==1:
                            print('--------------------------------------------------------------------------------')
                            print('you have selected checked shirts')
                            print('--------------------------------------------------------------------------------')
                            print('brands available:','1.lacoste','2.peter england',sep='\n')
                            brand=int(input('enter the number of your choice from the above options:'))
                            num14=int(input("enter the no.of items you need: "))
                            n='checked shirts-RS.299'
                        if shirt==2:
                            print('--------------------------------------------------------------------------------')
                            print('you have selected plain shirts')
                            print('--------------------------------------------------------------------------------')
                            print('brands available:','1.lacoste','2.peter england',sep='\n')
                            brand=int(input('enter the number of your choice from the above options:'))
                            num15=int(input("enter the no.of items you need: "))
                            o='plain shirts-RS.199'
                order=input("would you like to order some more in men's section(yes/no):")
                if order=='yes' or order=='no':
                        pass
                else:
                    order=input('please enter yes or no:')
    if menu==3:
            while order=='yes':
                print('IN ELECTRONICS SECTION:')
                print('1.mobiles','2.laptop','3.tablets',sep='\n')
                electronics=int(input('enter the number of the product you would like to see: '))
                if electronics==1:
                    print("1.samsung A23(5G) :RS.23,999","2.vivo Y35(4G) :RS.16,499",
                          "3.APPLE Iphone(5G) :RS.1,29,999",sep='\n')
                    mobiles=int(input('enter the number of your choice from the above options: '))
                    if mobiles==1 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected samsung A23(5G)")
                         print('--------------------------------------------------------------------------------')
                         num16=int(input("enter the no.of items you need: "))
                         p="samsung A23(5G) :RS.23,999"
                    if mobiles==2 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected vivo Y35(4G)")
                         print('--------------------------------------------------------------------------------')
                         num17=int(input("enter the no.of items you need: "))
                         q="vivo Y35(4G) :RS.16,499"
                    if mobiles==3 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected APPLE Iphone(5G)")
                         print('--------------------------------------------------------------------------------')
                         num18=int(input("enter the no.of items you need: "))
                         r="APPLE Iphone(5G) :RS.1,29,999"
                if electronics==2:
                    print("1.lenovo:RS.89,999","2.HP :RS.79,999",
                          "3.DELL :RS.69,999",sep='\n')
                    laptop=int(input('enter the number of your choice from the above options: '))
                    if laptop==1 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected lenovo")
                         print('--------------------------------------------------------------------------------')
                         num19=int(input("enter the no.of items you need: "))
                         s="lenovo:RS.89,999"
                    if laptop==2 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected HP")
                         print('--------------------------------------------------------------------------------')
                         num20=int(input("enter the no.of items you need: "))
                         t="HP :RS.79,999"
                    if laptop==3 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected DELL")
                         print('--------------------------------------------------------------------------------')
                         num21=int(input("enter the no.of items you need: "))
                         u="DELL :RS.69,999"
                if electronics==3:
                    print("1.SAMSUNG galaxy TAB10:RS.59,999","2.IPAD :RS.2,79,999",
                          "3.GOOGLE pixel TAB :RS.1,69,999",sep='\n')
                    tablets=int(input('enter the number of your choice from the above options: '))
                    if tablets==1 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected SAMSUNG galaxy TAB10")
                         print('--------------------------------------------------------------------------------')
                         num22=int(input("enter the no.of items you need: "))
                         v="SAMSUNG galaxy TAB10:RS.59,999"
                    if tablets==2 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected IPAD")
                         print('--------------------------------------------------------------------------------')
                         num23=int(input("enter the no.of items you need: "))
                         w="2.IPAD :RS.2,79,999"
                    if tablets==3 :
                         print('--------------------------------------------------------------------------------')
                         print("you have selected GOOGLE pixel TAB")
                         print('--------------------------------------------------------------------------------')
                         num24=int(input("enter the no.of items you need: "))
                         x="GOOGLE pixel TAB :RS.1,69,999"
                order=input("would you like to order some more in electronics section(yes/no):")
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
print('product name:','no.of items',sep='\t\t\t\t\t\t\t  ')
if num1>0:
        print(a,'\t\t\t\t\t',num1)
if num2>0:
        print(b,'\t\t\t\t\t',num2)
if num3>0:
        print(c,'\t\t\t\t\t',num3)
if num4>0:
        print(d,'\t\t\t\t\t\t',num4)
if num5>0:
        print(e,'\t\t\t\t\t\t',num5)
if num6>0:
        print(f,'\t\t\t\t\t\t',num6)
if num7>0:
        print(g,'\t\t\t\t\t\t',num7)
if num8>0:
        print(h,'\t\t\t\t\t\t',num8)
if num9>0:
        print(i,'\t\t\t\t\t\t',num9)
if num10>0:
        print(j,'\t\t\t\t\t\t',num10)
if num11>0:
        print(k,'\t\t\t\t\t\t',num11)
if num12>0:
        print(l,'\t\t\t\t\t\t',num12)
if num13>0:
        print(m,'\t\t\t\t\t\t',num13)
if num14>0:
        print(n,'\t\t\t\t\t\t',num14)
if num15>0:
        print(o,'\t\t\t\t\t\t',num15)
if num16>0:
        print(p,'\t\t\t\t\t\t',num16)
if num17>0:
        print(q,'\t\t\t\t\t\t',num17)
if num18>0:
        print(r,'\t\t\t\t\t\t',num18)
if num19>0:
        print(s,'\t\t\t\t\t\t',num19)
if num20>0:
        print(t,'\t\t\t\t\t\t',num20)
if num21>0:
        print(u,'\t\t\t\t\t\t',num21)
if num22>0:
        print(v,'\t\t\t\t\t\t',num22)
if num23>0:
        print(w,'\t\t\t\t\t\t',num23)
if num24>0:
        print(x,'\t\t\t\t\t',num24)

print('--------------------------------------------------------------------------------')      
bill=((num1*399)+(num2*399)+(num3*499)+(num4*499)+(num5*399)
      +(num6*199)+(num7*399)+(num8*199)+(num9*399)+(num10*399)+(num11*499)+(num12*499)
      +(num13*399)+(num14*299)+(num15*199)+(num16*23999)+(num17*16499)+
      (num18*129999)+(num19*89999)+(num20*79999)+(num21*69999)+(num22*59999)
      +(num23*279999)+(num24*169999))
print('total bill payable   :\t\t\t\t\t\tRS.',bill)
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
else:
        print('thank you')



        
