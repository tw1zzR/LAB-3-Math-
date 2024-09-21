
angle1 = float(input("Введіть перший кут опуклого п'ятикутника: "))
angle2 = float(input("Введіть другий кут опуклого п'ятикутника: "))
angle3 = float(input("Введіть третій кут опуклого п'ятикутника: "))
angle4 = float(input("Введіть четвертий кут опуклого п'ятикутника: "))

sum_angle = angle1 + angle2 + angle3 + angle4

angle5 = 540 - sum_angle

print(f"Величина п'того кута опуклого п'ятикутника дорівнює: {angle5}.")