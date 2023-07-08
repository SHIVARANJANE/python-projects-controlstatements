print('welcome to ICIC bank')
balance=500000
amt=0
name=input('enter your username:')
if name=="shiva":
    print('username is available')
    pss=int(input('enter your password'))
    if pss==2006:
        print('logged in successfully')
        a=input("would you like to proceed further(yes/no):")
        if a=='yes' or a=='no':
            if a=='yes':
                pass
        else:
            a=input('please enter yes or no:')
        while a=='yes':
            print('1.transfer money','2.balance inquiry','3.change PIN ',sep='\n')
            act=int(input('choose your preffered action(1/2/3):'))
            if act==1 or act==2 or act==3:
                if act==1:
                    bn=int(input('enter the account number for which you would like to transfer money:'))
                    amt=int(input('enter the amount you need to transfer:RS.'))
                    if amt<=100000:
                        print('the money is being transferred...please wait',
                                'transaction successful',sep='\n')
                    else:
                        print("dear customer the transaction limit for a day is 1 lakh:")
                        amt=int(input('enter the amount you need to transfer:RS.'))
                        print('the money is being transferred...please wait',
                                'transaction successful',sep='\n')
                    print('account balance:',balance-amt)
            
                if act==2:
                    print('your account balance:',balance-amt)
                if act==3:
                    pssc=int(input('enter your current PIN number:'))
                    if pssc==pss:
                        pss1=int(input('enter your new PIN:'))
                        pss2=int(input('confirm your new pin:'))
                        if pss1==pss2:
                                    print('PIN no. is changed successfully')
                                    pss=pss1
                        if pss1!=pss2:
                            print('PIN numbers did not match')
                            pss2=int(input('confirm your new pin:'))
                            if pss2==pss1:
                                    print('PIN no. is changed successfully')
                                    pss=pss2
                    else:
                        print('incorrect pin')
            a=input('would you like to do any other action(yes/no):')
            if a=='yes' or a=='no':
                        pass
            else:
                a=input('please enter yes or no:')

    else:
        print('password is incorrect')
else:
    print('username is not available')
print('thank you')

        
