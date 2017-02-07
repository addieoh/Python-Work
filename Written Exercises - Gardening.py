length = 8 #in feet
plant_space = 1 #in feet
soil_depth = 2 #in feet
gravel_depth = 3 #in feet

print ("Number of plants in semicircle:", (.5 * 3.1415926535 * (length / 4) ** 2) // (plant_space ** 2))

print ("Number of plants in circle:", (3.1415926535 * (length / 4) ** 2) // (plant_space ** 2))

print ("Total number of plants:", (.5 * 3.1415926535 * (length / 4) ** 2) // (plant_space ** 2) * 4 + (3.1415926535 * (length / 4) ** 2) // (plant_space ** 2))

print ("Volume of soil in semicircle in cubic yards:", (.5 * 3.1415926535 * soil_depth * (length / 4) ** 2) / 27)

print ("Volume of soil in circle in cubic yards:", (3.1415926535 * soil_depth * (length / 4) ** 2) / 27)

print ("Total volume of soil in cubic yards:",(3 * 3.1415926535 * soil_depth * (length / 4) ** 2) / 27)

print ("Total volume of gravel in cubic yards:", (((length ** 2) - (3 * 3.1415926535 * (length / 4) ** 2)) / 27) * gravel_depth)

