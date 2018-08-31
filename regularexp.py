#Que1-->Write a python code to find a valid email address from a text.
import re
email=str(input("ENTER AN EMAIL"))
matcher=re.finditer('\w[_a-zA-Z0-9.]*[@](gmail.com|yahoo.com)',email)
for m in matcher:
    print("Match is at :{},end :{},Pattern found :{}"\
          .format(m.start(),m.end(),m.group()))
print()

#Que2-->Find a valid Indian phone number from a text
import re
phone=input("ENTER PHONE NUMBER")
m=re.finditer('(\+91-)[6789]{1}[0-9]{9}',phone)
for i in m:
    print("Match is at :{},end :{},Pattern found :{}"\
          .format(i.start(),i.end(),i.group()))
print()

