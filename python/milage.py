print("how many kilometers did you cycle today")
kms = input() #get user input
miles = float(kms)/1.60934 #convert from string to float and divide
miles = round(miles, 2) #round the result
print(f"That is equal to {miles} miles ")


# ROUND SYNTAX:
# round(thing to round, how many decimal points)

