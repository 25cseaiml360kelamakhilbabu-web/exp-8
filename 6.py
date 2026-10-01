"""6,scenario : the smart-farm yield tracker
your are a data analyst for smart agriculture company.you are analyzing the dail harvest yield (in kilograms ) of 4 different crops -- tomatoes,carrotas,
potatoes and onions -- over a 7-day weel

here is the raw harvest data provided to you :

    python
    import numpy as np
    #row  represent crop :[tomatoes,carrots, potatoes,onions]
    #columns represent day:[monday,tuesday,wensday,thursday,friday,saturday,sunday]
    hartvest_data=np.array([
[50,55,60,52,58,65,70], # tomatoes
[30,32,28,35,33,40,42],#carrots
[100,95,105,110,98,120,125,],#potatoes
[40,38,42,45,41,50,55],#onions
])
your taskes:
 part 1: array properties & restructing
 
             write code to print the shape,number of dimenions (ndim),and total size (total data points)of the harvest_data array
             frame manager wants a report where the rows are the days of the weeks and the columns are the crops.use a numpy function to restructer the array to meet this requriment

 part 2 : statistical operstions
       3. weekly crop yield :calculate the average yield for each crop fopr the entire week ,
        4.dail averages: calculate the average yield across all crops for each individual day .
        5.best day :fin the maximum yield produced by any single crop on any single day,

part  3: broadcasting
        6.fertilizers bonus : due to a new fertilizers used mid way through the week, the expected yield foe all crops on friday ,saturday,and sunday increased

              you have a bouns array : daily_bouns = np.array([0,0,0,0,5,10,15]) (represting extra kgs per day).

              use broadcasting to add this bouns to the harvest_dta.
              crop shrinkage (adv broadcasting):during transport,different crops exprenice different rates of weight loss(shrinkage).
              tomatoes lose 5%,carrots lose 2%,potatoes lose 1%.and onions lose 3%.
              you have a shrinkage factor array: shrinkage=np.array([0.95,0.98,0.99,0.97)].

use broadcasting to multiply the current harvest_data(after the fertilizer bouns) by these shrinkage factors to get the final transport weght . (hint: you may need to reshape the shrinkage array first!)


"""
import numpy as np
# Harvest data
harvest_data = np.array([
    [50, 55, 60, 52, 58, 65, 70],   # Tomatoes
    [30, 32, 28, 35, 33, 40, 42],   # Carrots
    [100, 95, 105, 110, 98, 120, 125], # Potatoes
    [40, 38, 42, 45, 41, 50, 55]     # Onions
])

# Part 1: Array properties
print("Shape:", harvest_data.shape)
print("Dimensions:", harvest_data.ndim)
print("Total size:", harvest_data.size)

# Restructure: rows = days, columns = crops
daily_data = harvest_data.T

print("\nRestructured data:")
print(daily_data)

# Part 2: Statistical operations

# Average yield for each crop
crop_average = np.mean(harvest_data, axis=1)
print("\nWeekly crop average:", crop_average)

# Average yield for each day
day_average = np.mean(harvest_data, axis=0)
print("Daily average:", day_average)

# Maximum yield
best_day = np.max(harvest_data)
print("Maximum yield:", best_day)

# Part 3: Broadcasting

# Fertilizer bonus
daily_bonus = np.array([0, 0, 0, 0, 5, 10, 15])

new_data = harvest_data + daily_bonus

print("\nAfter fertilizer bonus:")
print(new_data)

# Shrinkage
shrinkage = np.array([0.95, 0.98, 0.99, 0.97])

# Reshape for broadcasting
shrinkage = shrinkage.reshape(4, 1)

# Final transport weight
final_weight = new_data * shrinkage

print("\nFinal transport weight:")
print(final_weight)
