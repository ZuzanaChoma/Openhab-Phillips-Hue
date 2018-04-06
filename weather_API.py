import requests
import json
import contextlib
import os
import time
import socket
import json
import requests

API_key='95c94ddcc208a5aed5db0b3e649a42f2'


def get_city():
 
 city='Aalborg'

 print('current chosen city is ',city)
 answer=input('Would you like to choose different city?\n Y/N? (type Y for yes, N for no\n')
 change=answer.lower()
 
 while not (change == 'y' or change == 'n'):
  answer=input('Would you like to choose different city?\n Y/N? (type Y for yes, N for no\n')
  change=answer.lower()

 if (change=='y'):
  city=input('insert desired city name:\n')
  print(city)
  print(type(city))
  
 elif(change=='n'):
  print('city name stays the same:',city)
 else:
   print('something went wrong')
 
 return city

def change_color(temp):
 
 if (temp<0):
  data="240,100,100"
 elif (0<temp<5):
  data="300,100,100"
 elif (5<temp):
  data="360,100,100"
 else:
  data="100,100,100"
 
 return data

def get_temp(location,key):
 r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s'%(location,key))
 allvalues=json.loads(r.content)
 all_temp_data = allvalues.get('main') 
 temp_data=all_temp_data.get('temp')  
 kalvin = float(temp_data)
 celsius = kalvin-273.15
 return celsius



city_name=get_city()
while True:
 current_temp=get_temp(city_name,API_key)
 prev_temp=current_temp
 print ('current temperature in %s is %d degrees celsius'%(city_name,current_temp))
 time.sleep(60)

 difference= prev_temp-current_temp
 if difference<0:
 	print('the temperature has increased')
 elif difference>0:
 	print('the temperature has decreased')
 elif difference==0:
 	print('temperature stayed the same')
 else:
 	('nobody knows whats happening')

 color=change_color(difference)
 r=requests.post('http://localhost:8080/rest/items/hue_0210_0017887911f3_2_color',data=color)
 

