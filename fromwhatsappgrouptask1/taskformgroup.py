import datetime
def PrintMenu():
    print('Enter your choices:- \n')
    print('1. Add customer')
    print('2. Delete customer')
    print('3. List of customer')
    print('4. Exit')

def AddCall():
    cust_id = input('cust_id = ')
    if len(cust_id)<3:
        print('given value is less the specific length')
        return
    else:
        cust_name = input('cust_name =')
        if len(cust_name)<2:
            print('given value is the less the specific length')
            return
        else:
            cust_address = input('cust_address=')
            Date_of_birthv = input('Date_of_birth (dd/mm/yyyy):-')
            Date_of_birth = Date_of_birthv.split('/')
            if len(Date_of_birth[0])<2 or len(Date_of_birth[1])<2 or len(Date_of_birth[2])<4 :
                print('please provide in correct formate(dd/mm/yyyy)')
            else:
                year = int(Date_of_birth[2])
                month =int(Date_of_birth[1])
                day = int(Date_of_birth[0])
                dob = datetime.datetime(year,month,day)
                age = (datetime.datetime.now()-dob)
                ageyears = int(age.days)/365
                if round(ageyears)>=15:
                    # print(round(ageyears))
                    mobile_number = input('mobilenumber=')
                    f = open("taskfile.txt","a+")
                    f.write(cust_id+','+cust_name+','+cust_address+','+Date_of_birthv+','+mobile_number+"\n")
                    return cust_name, cust_address, cust_id,round(ageyears),mobile_number

                else:
                    print('age required above 15 years')


def ListCall():
    num_lines = sum(1 for line in open('taskfile.txt'))
    print('total number of line= ' + str(num_lines))
    viewlines = input('type y to see all the lines=')
    if viewlines == 'y' or viewlines == 'Y':
        for line in open('taskfile.txt'):
            print(line)
    else:
        return


def DeleteCall():
    deletevar = input("enter id to delete=")
    with open('taskfile.txt','r') as f:
        lines = f.readlines()
        orignalcountv = len(lines)
    with open('taskfile.txt','w') as f:
        for line in lines:
            linesplit = line.split(',')
            if linesplit[0]!= deletevar:
                f.write(line)
    num_lines = sum(1 for line in open('taskfile.txt'))
    if orignalcountv != num_lines:
        print('line deleted')
    else:
        print('given customer id is not there give proper id  ')



a = True
while a:
    PrintMenu()
    a = input('give your choice=')
    if a == '4':
        break
    elif a == '1':
        print(AddCall())
    elif a == '2':
        DeleteCall()
    elif a == '3':
        ListCall()
    else:
        print('give correct choice(choice number is enough)')
