import requests
import smtplib 

# API key
api_file = open("apikey.txt", "r")
api_key = api_file.readline()
api_file.close()

# home address input
home = input("Enter a home address\n") 
  
# work address input
work = input("Enter a work address\n") 
  
# base url
url = "https://www.google.com/maps/@12.8688809,77.6650655,15z/data=!4m2!10m1!1e1"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
 
# return time as text and as seconds
time = r.json()["rows"][20]["elements"][20]["duration"]["text"]       
seconds = r.json()["rows"][20]["elements"][20]["duration"]["value"]
  
# print the travel time
print("\nThe total travel time from home to work is", time)
