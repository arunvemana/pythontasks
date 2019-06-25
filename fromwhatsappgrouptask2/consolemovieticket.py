from time import sleep
from faker import Faker
from  random import randint
from prettytable  import PrettyTable
import json
import os


fake = Faker()


# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

# # Display a title bar.
# print("\t**********************************************")
# print("\t***  Greeter - Hello old and new friends!  ***")
# print("\t**********************************************")
#
# # Print a bunch of information, in short intervals
# names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

# Print each name 5 times.
def GenerateEvent():
# generate events data with faker module
    events = {}
    for i in range(0,50):
        events[i] ={}
        events[i]['id'] = randint(1,100)
        events[i]['EventName'] = fake.name()
        events[i]['Address'] = fake.address()
        events[i]['date'] = str(fake.date_between(start_date='today', end_date='+1y'))
        events[i]['NoOfTickets'] = 100
        events[i]['AvailableTickets'] = randint(5,20)
    print(events)
    # creating json file with data
    json.dump(events,open("eventsdetails.json",'w'))
    # for i in data.keys():
    #     print(data[i]['eventname'])
    # read the data from file

    # for i in events.items():
    #     print(i)
    #     # print(events[i]['eventname'])
    #     # print(events[i]['avaliableseats'])
    #     # print(str(i['eventname']))

def BrowseEvents():
    # read data from the file
    eventdata = json.load(open("eventsdetails.json"))
    pretable = PrettyTable()
    pretable.field_names = ["Event Name","Date","Available Tickets"]
    for i in eventdata.keys():
        pretable.add_row([eventdata[i]['EventName'],eventdata[i]['date'],eventdata[i]['AvailableTickets']])
    print(pretable)
    eventid = input('enter the event name:-')
    eventid = eventid.replace(' ','')
    if eventid.isalpha():
        booktickets(eventid)
    else:
        print(eventid)
        print('enter correct event name')

def where_json(file_name):
    return os.path.exists(file_name)

def Userprofile(FirstUser,userchoice):
    if FirstUser:
        os.system('cls')
        print('***** Enter your new User Details **********')
        user = {}
        user[1] = {}
        user[1]['name'] = input('enter your name:-')
        user[1]['location'] = input('enter your location:-')
        user[1]['phonenumber'] = input('enter your phonenumber:-')
        user[1]['card'] = input('enter your payment card number:-')
        user[1]['carddate'] = input('enter your payment card expiry date:-')
        # print(user)
        with open('userdetails.json','w') as fu:
            json.dump(user,fu)
        print('your information is saved:')
        print('your tickets has to been booked')
        sleep(3)
        exit()
    elif userchoice == '1':
        userdata = json.load(open("userdetails.json"))
        no = len(userdata)
        no = no + 1
        userdata[no] = {}
        userdata[no]['name'] = input('enter your name:-')
        userdata[no]['location'] = input('enter your location:-')
        userdata[no]['phonenumber'] = input('enter your phonenumber:-')
        userdata[no]['card'] = input('enter your payment card number:-')
        userdata[no]['carddate'] = input('enter your payment card expiry date:-')
        print(userchoice + 'userchoice ')
        with open('userdetails.json','w') as fu:
            json.dump(userdata,fu)
        print('your information is saved!')
        print('your tickets has been booked!')
        sleep(3)
        exit()
    elif userchoice == '2':
        print('user detail update function still on developing function.')
        exit()
    else:
        exit()


def UserProfilecheck():
    os.system('cls')
    userchoice = input('1.new user \n2.existing user\n')
    if where_json('userdetails.json'):
        FirstUser = False
        Userprofile(FirstUser,userchoice)
    else:
        FirstUser = True
        Userprofile(FirstUser,userchoice)
        # userdata = json.load(open("eventsdetails.json"))



def booktickets(eventid):
    eventdata = json.load(open("eventsdetails.json"))
    for i in eventdata.keys():
        if eventdata[i]['EventName'].replace(' ','') == eventid:
            os.system('cls')
            nooftickets = input('how many tickets u want to book= ')
            if int(eventdata[i]['AvailableTickets']) >= int(nooftickets):
                os.system('cls')
                UserProfilecheck()
        else:
            os.system('cls')
            print('enter correct event name')
    sleep(2)


a = True
while a:
    # Clear the screen before listing names.
    os.system('cls')
    os.system('color 04')
    # Display the title bar.
    print("\t**********************************************")
    print("\t***  welcome to the ticket purchase site!  ***")
    print("\t**********************************************")

    print("\n\n")
    varinput = input("choose what u like to see! \n 1. Browse events \n 2. Create user \n")
    if varinput == '1':
        BrowseEvents()
    elif varinput == '2':
        UserProfilecheck()
    else:
        print('please give the correct choice')

    # Pause for 1 second between batches.
    sleep(1)
