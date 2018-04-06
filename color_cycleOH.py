import requests
import time




i=0

while i<=360:
  
  first=str(i)
  data=first+",100,100"
  r=requests.post('http://localhost:8080/rest/items/hue_0210_0017887911f3_2_color',data=data)
  i=i+1


print('The cycle is over')
data="240,100,100"
r=requests.post('http://localhost:8080/rest/items/hue_0210_0017887911f3_2_color',data=data)
print('Color blue chosen as final mode')


