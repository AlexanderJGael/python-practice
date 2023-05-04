import sys

total = int(sys.argv[1]) + int(sys.argv[2])

if total <= 0:
    print("You have chosen the path of destitution.")
elif total <=100:
    print("You have chosen the path of plenty.")
else:
    print("You have chosen the path of excess.")
