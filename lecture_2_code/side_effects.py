def side_effects(cities):
    print(cities)
    cities += ["Birmingham", "Bradford"]
    print(cities)
 
locations = ["London", "Leeds", "Glasgow", "Sheffield"]
side_effects(locations)
print(locations) 

