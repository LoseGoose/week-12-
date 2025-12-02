# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature in Fahrenheit.
input_temp = float(input("Enter today's temperature in Fahrenheit: "))
# Prints whether it’s cold, warm, or hot using comparison operators.
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”
if input_temp < -10 or input_temp > 110:
    print("Extreme temperature warning!")
elif input_temp < 60:
    print("It's cold today.")
elif 60 <= input_temp <= 80:
    print("It's warm today.")
else:
    print("It's hot today.")

