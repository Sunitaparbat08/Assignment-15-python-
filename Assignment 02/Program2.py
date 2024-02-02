angle1 = int(input("Enter the angle 1:"))
angle2 = int(input("Enter the angle 2:"))
angle3 = int(input("Enter the angle 3:"))
if (angle1==90  and angle2 + angle3 == 90 or angle1+angle2==90 ):
    print("it is right angle triangle")
else:
    print ("it is not right angle triangle")    