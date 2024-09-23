
weight = float(input("Please enter weight: "))
measurement = input("What measurement have you used? Type 'L' for pounds or 'K' for kilograms: ")




if measurement == "L" or measurement == "l":
    new_weight = weight * 0.45359237
    print(f"You weigh {new_weight} kg")
elif measurement == "K" or measurement == "k":
    new_weight = weight * 2.2046
    print(f"You weigh {new_weight} lbs")
else:
    print("Please enter a valid measurement")
