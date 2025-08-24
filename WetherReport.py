import requests
import matplotlib.pyplot as plt
import pandas as pd


API_KEY = "e741391ec872d58329d3d6c36a2c141f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

cities = ["Atlanta", "Dhaka", "London"]

# fetch current data
def fetchWetherData(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # temperature in (C)
    }
    response = requests.get(BASE_URL, params=params)   # me http request to OpenWeather

    try:
        data = response.json()   # convert the response from API into a python dictionary
    except:
        data = None

    if response.status_code == 200:
        return data
    else:
        print("Error fetching data:", response.status_code)
        print("Response content:", data)   
        print("Full URL:", response.url)   # for debugging
        return None
    

# Fetch 5 days forecast data
def fetchForecastData(city):
    params = {
        "q" : city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()
    
    else:
        print("Error fetching forecast : ", response.status_code)
        print("Response content : ", response.text)
        return None


def displayWetherData(data):
    if "cod" in data and data["cod"] != 200:     # We can also use str(data["cod"]) : converts to a string for work consistently
        print(f"Error from API: {data.get('message', 'Unknown issue')}")   # here get means, access dictionary values.
        return

    print(f"City : {data['name']}")
    print(f"Weather : {data['weather'][0]['description']}")
    print(f"Temperature : {data['main']['temp']} °C")    # {data["main"]["temp"]} : mean nested dictionary acces. two dictionary here, data and main.
    print(f"Humidity : {data['main']['humidity']}%")
    print(f"Wind Speed : {data['wind']['speed']} m/s")

    
    
# Ploting
# def plotWetherTrend(days, temperatures):
#     plt.plot(days, temperatures, marker="o", color="blue")
#     plt.title("Temperature Trends")
#     plt.xlabel("Days")
#     plt.ylabel("Temperature (C)")
#     plt.show()


# Ploting multiple cities
def plotTrends(city, forecast):
    days = [entry["dt_txt"] for entry in forecast["list"][:8]]
    temps = [entry["main"]["temp"] for entry in forecast["list"][:8]]
    humidity = [entry["main"]["humidity"] for entry in forecast["list"][:8]]
    
    plt.figure(figsize=(10,5))
    plt.plot(days, temps, marker="o", color="red", label="Temperature (C)")
    plt.plot(days, humidity, marker="x", color="blue", label="Humidity (%)")
    plt.title(f"Weather trends for {city}")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
# save forecast in csv file
def saveForecastTocsv(city, forecast):
    rows = []
    for entry in forecast["list"]:
        rows.append({
            "datetime" : entry["dt_txt"],
            "temp" : entry["main"]["temp"],
            "humidity" : entry["main"]["humidity"],
            "weather" : entry["weather"][0]["description"]
        })
        
    df = pd.DataFrame(rows)
    filename = f"{city}_forecast.csv"
    df.to_csv(filename, index=False)
    print(f"Save forecast to {filename}")
    


# show a pie chart of weather condition
def plotWeatherPie(city, forecast):
    weatherCount = {}   # count occurances (how many times each weather condition appears in the forecast data)
    for entry in forecast["list"]:
        w = entry["weather"][0]["description"]
        weatherCount[w] = weatherCount.get(w, 0) + 1    #
        
    labels = list(weatherCount.keys())
    sizes = list(weatherCount.values())
    
    plt.figure(figsize=(7,7))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"weather distribution for {city} (next 5 days)")
    plt.show()
        

# Compare Weather between two cities
def compareWeather(cities):
    temps = []
    for city in cities:
        data = fetchWetherData(city)
        if data:
            temps.append((city, data["main"]["temp"]))
            
    cityNames = [t[0] for t in temps]
    cityTemps = [t[1] for t in temps]
    plt.bar(cityNames, cityTemps, color="skyblue")
    plt.title("Temperature Comparison")
    plt.xlabel("City")
    plt.ylabel("Temperature (C)")
    plt.show()
        


city = "Atlanta"


# print(data)
# print("RAW RESPONSE: ", data)


compareWeather(["Atlanta", "Dhaka"])
        
# if forecast:
#     days = [entry["dt_txt"] for entry in forecast["list"][:8]]  # next 8 times slots
#     temperatures = [entry["main"]["temp"] for entry in forecast["list"][:8]]
#     plotWetherTrend(days, temperatures)


for city in cities:
    print(f"Fetching current weather for {city} : ")
    data = fetchWetherData(city)
    displayWetherData(data)
    
    print(f"Fetching forecast for {city} : ")
    forecast = fetchForecastData(city)
    if forecast:
        plotTrends(city, forecast)
        saveForecastTocsv(city, forecast)
        plotWeatherPie(city, forecast)


