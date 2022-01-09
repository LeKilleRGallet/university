from datetime import datetime
import pytz

def my_utctime():
    my_datetime = datetime.utcnow()
    print(my_datetime)

    my_str = my_datetime.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Day/Month/Year: {my_str}")

    my_str = my_datetime.strftime("%m/%d/%Y %H:%M:%S")
    print(f"Month/Day/Year: {my_str}")

def city_timezone(city=''):
    if city == "NYC":
        return datetime.now(pytz.timezone("America/New_York"))
    elif city == "London":
        return datetime.now(pytz.timezone("Europe/London"))
    elif city == "Tokyo":
        return datetime.now(pytz.timezone("Asia/Tokyo"))
    elif city == "CDMX":
        return datetime.now(pytz.timezone("America/Mexico_City"))
    elif city == "Sydney":
        return datetime.now(pytz.timezone("Australia/Sydney"))
    elif city == "Bogota":
        return datetime.now(pytz.timezone("America/Bogota"))
    elif city == "Barranquilla":
        return datetime.now(pytz.timezone("America/Bogota"))
    else:
        return datetime.now(pytz.timezone("UTC"))

print(f"NYC: {city_timezone('NYC')}")
print(f"London: {city_timezone('London')}")
print(f"Tokyo: {city_timezone('Tokyo')}")
print(f"CDMX: {city_timezone('CDMX')}")
print(f"Sydney: {city_timezone('Sydney')}")
print(f"Bogota: {city_timezone('Bogota')}")
print(f"Barranquilla: {city_timezone('Barranquilla')}")
print(f"UTC: {city_timezone()}")

my_var: str = "Hello"