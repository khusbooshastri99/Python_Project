"This program helps to calculate how many cans we have to use for a given surface area."


import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
test_h = int(input("Height of wall is: "))
test_w = int(input("Width of wall is: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
