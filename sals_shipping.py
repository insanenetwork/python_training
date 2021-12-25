weight = 125
# price for shipping

if weight <= 5:
  ground_shipping = weight * 4 + 20
elif weight <= 10:
  ground_shipping = weight * 4 +20
elif weight <= 15:
  ground_shipping = weight * 4 + 20
else:
  ground_shipping = weight * 4 + 20
  print(f"The price for shipping for package is : {ground_shipping}")

#drone shipping 
if weight <= 20:
  ground_air = weight * 4.50
elif weight <= 40:
    ground_air = weight * 4.50
elif weight <= 60:
    ground_air = weight * 4.50
elif weight <= 80:
    ground_air = weight * 4.50
else:
    ground_air = weight *4.50

#print to the screen the shipping cost

print(f"The price for shipping your package by drones is: {ground_air}")
