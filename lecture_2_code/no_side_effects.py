def no_side_effects(cities):
	    print(cities)
	    cities = cities + ["Birmingham", "Bradford"]
	    print(cities)
locations = ["London", "Leeds", "Glasgow", "Sheffield"]
no_side_effects(locations)
print(locations)

