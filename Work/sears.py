bill_thickness = 0.11 * 0.001
sears_height = 442 #metres
day = 1
bill = 1

while bill * bill_thickness < sears_height:
    bill *= 2
    day += 1
    bill_height = bill * bill_thickness
    print(f"Bill Height {bill_height}, Day {day}")




