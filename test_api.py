import requests
from random import randrange

api_url = 'http://api.open-notify.org/iss-now.json'

i = str(randrange(20))
api_url = "http://numbersapi.com/"+i 

response = requests.get(api_url)

if(response.status_code==200):
    print(response.text[len(i):])
else:
    print(response.status_code)

version = ""
while(version!=i):
    print("Let try!")
    version = input("go on _")

print("Congratulate you! The number is " + i)