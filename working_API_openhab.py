import requests
import json
import contextlib
import os
import time
import socket

ip=socket.gethostbyname(socket.gethostname())


def light_check():
 
 answer = input("Are your lights on?\n")
 s = answer.lower()
 while not (s == "yes" or s == "no"):
  answer = input("Are your lights on?\n")
  s = answer.lower() 

 if (s=="yes"):
     print("Lights closing in 5 seconds\n")
     time.sleep(5) 
     status="OFF" 
 
 elif (s=="no"):
	 print("Lights starting in 5 seconds\n")
	 time.sleep(5)
	 status="ON"
 else:
   print("something went wrong")
   
 return status
 


def get_item(address):
 items= requests.get('http://%s:8080/rest/items'%address)
 allvalues=json.loads(items.content)

 devices_list=[]
 i=0
 length=(len(allvalues))-1
 last_ID=(len(allvalues))

 while i<=length:
  allvalues=json.loads(items.content)[i]
  devices_list.append(allvalues.get('name'))
  print()
  print('item ID number'+str(i+1)+':    '+ allvalues.get('name'))  
  i=i+1
 
 number=input("\ninsert ID number of device you would like to use \n enter only number within range 1 to %d \n"%last_ID).strip()
 ID= int(number)
 device_name='' 

 while not (0<=ID<=last_ID):
  print('INVALID INPUT: your number was out of range 1 to %d'%last_ID)
  number=input("\ninsert ID number of device you would like to use \n enter only number within range 1 to %d \n"%last_ID).strip()
  ID= int(number)

 if (ID<=last_ID):
    device_name=devices_list[ID-1]
    return device_name
    
 else:
  print('something went wrong')


def color_picker():
 
 ans=int(input('choose color ID \n1:blue\n2:red\n'))
 while not (ans == 1 or ans == 2):
  ans=int(input('choose color ID \n1:blue\n2:red\n'))

 if (ans==1):
  color="240,100,100"
  print('blue color chosen')
 elif (ans==2):
  color="360,100,100"
  print('red color chosen')
 else:
  color="0,100,0"
  print('incorrect input, lamp turned off')
 
 return color
 
   
def act():
 answer=int(input("Which action would you like to perform?(type in action ID number)\n 1 : Turn lights on/off\n 2 : Change light color\n")) 

 if (answer==1):
 	return light_check()
 elif(answer==2):
 	return color_picker() 
 else:
 	print('Invalid input')

  

result=(get_item(ip))
data=(act())



r= requests.post('http://%s:8080/rest/items/%s'%(ip,result),data=data)

if(r.status_code==200):
	print('Lights status succesfully changed')
else:
 	print('error occured, error code follows:')
 	print(r)




 
