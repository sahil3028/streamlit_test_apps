import requests
import dotenv
Api=dotenv.get_key("weather_dashbord/.env","API")
data={}
def get_data(city,days,type):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={Api}"
    response=requests.get(url)
    data=response.json()
    if data.get("cod") != "200":
        return None, None
    date=[i['dt_txt'] for i in data['list'][:(8*days)-1]]

    if type=="temperature":
        temp=[i['main']['temp'] for i in data['list'][:(8*days)-1]]
        return date,temp

    if type=="sky":
        # sky = [i['weather'][0]['main'] for i in data['list'][:(8 * days) - 1]]
        sky = [f"weather_dashbord/image/{i['weather'][0]['main']}.png" for i in data['list'][:(8 * days) - 1]]
        return date,sky


if __name__=="__main__":
    print(get_data("dhanbad",5))