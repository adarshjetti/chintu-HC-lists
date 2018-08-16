"""import traceback
from io import StringIO
import sys

cars={'toyota':'camry','honda':'civic','bmw':'beetle'}
print(cars)
print(cars['toyota'])
for brand,car in cars.items():
    if car=='civic':
        print(brand)
cars['tata']='nano'

print(cars.items())
print(str(len(cars)))
for b,c in cars.items():
    print(c+"-->"+b)
for x in range(len(cars)):
    print(x)
i=0
for key in cars.keys():
    print(key+":"+str(i))
    i=i+1
i=3
b=5
while i>=0:
    print(i)
    print("adarsh "*+i)
    i=i-1

a=None
b=None
c=29
d='adarsh'
e='2012-08-27'
x=[a,b]

if not all(x):
    print("hurray!")

print(x)
if any(x):
    print("any-success")

if all(x):
    print("all-success")

for y in x:
    print(y)
if None in x:
    print(x.index(None))
    x[x.index(None)]="chintu"

makeitastring='\n'.join(map(str, x))
print(makeitastring)


from twilio.rest import Client

t="dhruva is a baby"

def send_sms(text):
    account_sid="AC69c43dd61fec55f6ff83dcedfc417265"
    auth_token="77dfa616b04d10a7f74e48f786e8f186"

    client=Client(account_sid,auth_token)

    client.messages.create(
        to="+12149911965",
        from_="+19723664883",
        body=text
    )
send_sms(t)
log.close()
try:
    
    #traceback.print_stack(file=s)
    log = open("log.txt", "w")
    traceback.print_exc(file=log)

log_file_name="C.txt"
log = open(log_file_name, "w")
try:
    msg=None
    s = StringIO()
    s.write('Call Location:\n')
    msg = msg + s.getvalue()
except:
    traceback.print_exc(file=log)
    log.close()
sys.stdout.flush()

sys.stdout=open("tumry.txt", "w")

#advocates_dictionary = pass_advocates_dictionary
print("adarsh")
sys.stdout=sys.__stdout__ # returns output to the console though stdout is not closed.
print("dhruva")
sys.stdout.close()
b="config"
a="   config               "
print(len(a))
l
if b==a:
    print("success-chintu")
c=a.strip()
if b==a.strip():
    print("success-ponni")
print(len(c))

f = open('C:\\Users\\Adars\\PycharmProjects\\SeleniumBasics\\ChintuCourt\\Causelist_folders\\CauseList 2018-08-06\\CauseList 2018-08-06.txt', 'rb')
f.seek(0) # Move to the start of file
print(len(f.read()))
length=4472

import os
print(len([iq for iq in os.scandir('C:\\Users\\Adars\\PycharmProjects\\SeleniumBasics\\ChintuCourt\\Causelist_folders\\')]))

print(os.path.basename(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

file_name=os.listdir('C:\\Users\\Adars\\PycharmProjects\\SeleniumBasics\\ChintuCourt\\Causelist_folders')
print(file_name)

print(len(file_name))

for n in file_name:
    print(n)

x=0
for y in range(10):
    x=x+1
    print("y:"+str(y))
    print("x:"+str(x))

a=[1,2,5]
z=[1,2,5]

if a==z:
    print("success!")

b={1:5,2:10,3:15}
y={1:5,2:10,3:16}

if b==y:
    print("hurray!")"""
a='xylophone'
b=None
c=[a,b,25,'car','umbrella']
print(c)
if None in c:
    print(len(c))
    print(c.index(None))
c.append(c.pop(c.index(None)))
print(c)
#c.append(c.pop(c.index(None)))

#print(c)

y=[]
print(bool(y))
if not y:
    print("hurray!")


