from cmath import sqrt

sides = "hypotenuse, opposite, adjacent"
unites=  "CM, M, Feet, KM"
print("what is your unit of measurment?\n "+ unites)
unit = input()
print("which side are you missing?\n "+ sides)
side = input()
if side == "hypotenuse":
    opposite=  int(input("opposite?\n"))
    adjacent=  int(input("adjacent?\n"))
    hypotenuse= sqrt(opposite**2 + adjacent**2)
    print(f"the Hypotenuse will be equal to {hypotenuse}")
    print(unit)

if side == "opposite":
    hypotenuse=  int(input("hypotenuse?\n"))
    adjacent=  int(input("adjacent?\n"))
    opposite= sqrt(hypotenuse**2 - adjacent**2)
    print(f"the opposite will be equal to {opposite}")
    print(unit)

if side == "adjacent":
    hypotenuse=  int(input("hypotenuse?\n"))
    opposite=  int(input("opposite?\n"))
    adjacent= sqrt(hypotenuse**2 - opposite**2)
    print(f"the adjacent will be equal to {adjacent}")
    print(unit)
