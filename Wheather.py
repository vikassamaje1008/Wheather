import requests
import json
from datetime import datetime

#Fetching the data from api using requests module
api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(api_url)
data = response.text
parse_jason=json.loads(data)


while True:
 #Asking user to input the full date.
 date1=int(input("Enter the date.:"))
 month=int(input("Enter the month.:"))
 year=int(input("Enter the year.:"))
 print("")
 print("Enter 1 to get weather.")
 print("Enter 2 to get wind speed.")
 print("Enter 3 to get pressure.")
 print("Enter 0 to Exit.")
 choice=int(input("Enter your choice.:"))
 print("")
 if(choice!=0):
  def date_check(date1,month,year):
   list_count=len(parse_jason["list"])
   i_list=0
   datenotfound=False
   date=f"{year}-0{month}-{date1}"
   for list in data:
    api_date=parse_jason["list"][i_list]["dt_txt"]
    if(date==api_date[:10]):
     print(f"{date1}-0{month}-{year}")
     break
    else:
     i_list =i_list+1
     if(i_list>=list_count):
      print(f"{date}")
      datenotfound=True
      break
   return i_list,datenotfound
 
  def data1(choice,i_list,datenotfound):
      if(datenotfound!=True):
       if choice == 1:
           temp_list=parse_jason["list"][i_list]["main"]["temp"]
           return f"temp for above date is {temp_list}"
       elif choice == 2:
           speed_list=parse_jason["list"][i_list]["wind"]["speed"]
           return f"wind speed for above date is {speed_list}"
       elif choice == 3:
           pressure_list=parse_jason["list"][i_list]["main"]["pressure"]
           return f"pressure for above date is {pressure_list}"
       else:
          return "not a valid choice"
      else:
        return "Above ate not found."
  
  i_list,datenotfound=date_check(date1,month,year)
  print(data1(choice,i_list,datenotfound))
 else:
   break

