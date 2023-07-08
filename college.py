print('welcome to ABC college of engineering')
print('departments:','1.Computer science','2.Electrical',
      '3.Civil','4.Mechanical',sep='\n')
num1=num2=num3=num4=num5=num6=num7=num8=num9=num10=num11=num12=num13=num14=0
a=int(input('enter the number of the department you would like to explore:'))
if a==1 or  a==2 or  a==3 or  a==4:
    if a==1:
        print('welcome to COMPUTER SCIENCE department')
        print('--------------------------------------')
        print('courses available:','1.CSE','2.CSE(AI and ML)','3.CSE(DataScience)',sep='\n')
        b=int(input('enter the number of the course you prefer:'))
        if b==1:
            print('CSE')
            print('course fee: 2,60,000')
            num1=260000
        if b==2:
            print('CSE(AI and ML)')
            print('course fee: 4,60,000')
            num2=460000
        if b==3:
            print('CSE(DataScience)')
            print('course fee: 3,60,000')
            num3=360000
    if a==2:
        print('welcome to ELECTRICAL department')
        print('--------------------------------------')
        print('courses available:','1.ECE','2.EEE',
              '3.ELECTRICAL and ComputerScience engineering',sep='\n')
        c=int(input('enter the number of the course you prefer:'))
        if c==1:
            print('ECE')
            print('course fee: 3,10,000')
            num4=310000
        if c==2:
            print('EEE')
            print('course fee: 2,60000')
            num5=260000
        if c==3:
            print('ELECTRICAL and ComputerScience engineering')
            print('course fee: 4,60000')
            num6=460000
    if a==3:
        print('welcome to CIVIL department')
        print('--------------------------------------')
        print('courses available:','1.transportation engineering',
              '2.geo technical engineering','3.water resource engineering',sep='\n')
        d=int(input('enter the number of the course you prefer:'))
        if d==1:
            print('transportation engineering')
            print('course fee: 2,10,000')
            num7=210000
        if d==2:
            print('geo technical engineering')
            print('course fee: 2,60,000')
            num8=260000
        if d==3:
            print('water resource engineering')
            print('course fee: 3,60,000')
            num9=360000
    if a==4:
        print('welcome to MECHANICAL department')
        print('--------------------------------------')
        print('courses available:','1.Automotive engineering',
              '2.Industrial engineering','3. engineering mechanics',sep='\n')
        d=int(input('enter the number of the course you prefer:'))
        if d==1:
            print('Automotive engineering')
            print('course fee: 2,30,000')
            num10=230000
        if d==2:
            print('Industrial engineering')
            print('course fee: 2,20,000')
            num11=220000
        if d==3:
            print('engineering mechanics')
            print('course fee: 2,60,000')
            num12=260000
h=input('would you like to be a hosteller(yes/no):')
if h=='yes':
    print('mess:RS.10,000','ROOM :RS.20,000','total fee:RS.30,000',sep='\n')
    num13=30000
bus=input('note:bus facility is availed only for day scholars,would like to prefer the college bus(yes/no):')
if bus=='yes':
    print('note:bus facility is availed only for day scholars')
    print('transport fee:RS.1,00,000')
    num14=100000
print('your application is submitted')
bill=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14
print('your total bill:',bill)
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
                
if payment=='cash':
                print('you have selected cash on delivery:')             
                print('amount to be paid: ',bill)
                print('transaction successful!')
other=input('would you like to give any feedback(yes/no):')
if other=='yes':
        feed=input('your comment here:')
        print('thank you for your response!')
else:
        print('thank you')






        
        
        
        
