# https://www.codewars.com/kata/57e921d8b36340f1fd000059
def shark(pontoon_distance, shark_distance, your_speed, shark_speed, dolphin):
    if dolphin:  shark_speed /= 2
    return "Alive!" if pontoon_distance / your_speed < shark_distance / shark_speed  else "Shark Bait!"