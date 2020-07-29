from random import random
hourly_rate = float(input ("Enter hourly rate: "))
working_hours = float(input ("Enter working hours: "))

if (hourly_rate > 15) or (working_hours > 16):
     print ("Wrong input for woring hours or the rate, pease try again.")
else:
    overtime_hours = max(0, working_hours - 8) 
    overtime_multipliers = 1.1 + 0.5 * random()
    salary = (hourly_rate * working_hours) + (hourly_rate * overtime_hours * overtime_multipliers)
    print ("Your salary for a day is", salary)