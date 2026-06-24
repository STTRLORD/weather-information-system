import requests

city=input("enter city name ->")

api_key = "7eb8a15bd3714fae93a53908262406"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)

data = response.json()
if "error" in data :\
    print("city not found ")
else:
 print(f"city-> {data["location"]["name"]}")
 print(f"region-> {data["location"]["region"]}")
 print(f"country-> {data["location"]["country"]}")
 print(f"localtime-> {data["location"]["localtime"]}")
 print(f"current temp in c-> {data["current"]["temp_c"]}")
 print(f"current temp in f-> {data["current"]["temp_f"]}")
 print(f"condition-> {data["current"]["condition"]["text"]}")
 print(f"humidity-> {data["current"]["humidity"]}")
 print(f"feelslike-> {data["current"]["feelslike_c"]}")



