import math
situation = input("SAS, SSS :\n").upper()

if situation == "SAS":
  side_a = int(input("Side a :\n"))
  angle_a = math.degrees(int(input("Angle A:\n")))
  side_b = int(input("Side b :\n"))
  angle_b = math.asin(math.sin(angle_a)*(side_b/side_a))
  print(math.degrees(angle_b))

if situation == "sss":
  a = input("side 1:\n")
  b = input("side 2\n")
  c = input("side 3:\n")
