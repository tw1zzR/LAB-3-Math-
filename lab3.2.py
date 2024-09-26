import sys

print("Щоб дізнатися величину п'того кута опуклого п'ятикутника, задайте чотири кути опуклого п'ятикутника.\n")

angle1 = float(sys.argv[1])
angle2 = float(sys.argv[2])
angle3 = float(sys.argv[3])
angle4 = float(sys.argv[4])

sum_angle = angle1 + angle2 + angle3 + angle4

if sum_angle >= 540:
    print("Такого не існує, спробуйте ще раз!")
elif sum_angle <= 0:
    print("Такого не існує, спробуйте ще раз!")
else:
    angle5 = 540 - sum_angle
    print(f"Величина п'того кута опуклого п'ятикутника дорівнює: {angle5}.")

