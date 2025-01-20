import requests

def get_current_weather():
    city = str(input("Enter yout city name :"))
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c3441106d89ec27031898e9391899a51'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        
        result = []
        
        weather = data['weather'][0]['description']
        main = data.get('main', {})
        pressure = main.get('pressure')
        humidity = main.get('humidity')
        wind = data['wind']['speed']
        result.append((weather, pressure, humidity, wind))
        return result        
    else:
        raise Exception("Fails to get data from api for your city/talika/village.")

def main():
    try:
        result = get_current_weather()
        for idx, (weather, pressure, humidity, wind) in enumerate(result):
            print()
            print("Weather :", weather)
            print("Pressure :", pressure)
            print("Humidity :", humidity)
            print("Wind :", wind)
            print()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()