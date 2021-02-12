# https://www.codewars.com/kata/5865a28fa5f191d35f0000f8
def take_umbrella(weather, rain_chance):
    return weather == "sunny" and rain_chance > 0.5 or weather == "rainy" or weather == "cloudy" and rain_chance > 0.2