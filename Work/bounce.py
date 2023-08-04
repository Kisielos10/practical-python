# bounce.py
#
# Exercise 1.5
height = 100
bounce_factor = 0.6
count = 1

while count <= 10:
    height=height*bounce_factor
    print(count," ",round(height,4))
    count+=1