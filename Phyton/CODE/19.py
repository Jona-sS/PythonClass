import conv
import conv.distance
import conv.temperature
#conv anlegen ->tempereatur und distance einfügen
def test_conversion():
    # Test temperature conversion
    temp_celsius = 100
    temp_fahrenheit = conv.temperature.celsius2fahrenheit(temp_celsius)
    if conv.temperature.fahrenheit2celsius(temp_fahrenheit) == temp_celsius: print("Temperature conversion passed")
    # Test distance conversion
    distance_meter = 10
    distance_inch = conv.distance.meter2inch(distance_meter)
    if conv.distance.inch2meter(distance_inch) == distance_meter: print("Distance conversion passed")
if __name__ == "__main__":
    test_conversion()