# Name : Zachary Monk
# Python Version: 3.5.2
# Program Number: FatStats 2
# Date: 13 JUL 2017
# Description: A python program to evaluate and visualize data from weight logs

#Source:

#imports
import numpy as np
import matplotlib.pyplot as plt


# Adjust Plot size
plt.figure(figsize=(12, 9))    

#Open the file
data_file = open('weight_log.csv', 'r')

#Global Variables:
weight_list = []
date_list = []
avg_list = []
sum = 0
avg = 0
day_count = 0
old_month = '09'

'''Example Lines:
"June 20, 2017 at 09:47AM",218.3,pounds,28.82
Month, Day, Year, at Time, Weight, Fat %
'''

#Split Lines
lines = data_file.read().splitlines()

### Single Line ###
line_items = lines[1].split(',')
print(line_items)

#Titles:
date1 = line_items[0].split(' ')
date2 = line_items[1].split(' ')
weight = line_items[2]
fat = line_items[4]
month = date1[0]
day = date1[1]
year = date2[1]
time = date2[3]
total_weight = 0
avg_weight = 0


print(month,day,year,time,weight,fat)


for i in range(1,len(lines),1):
    line_items = lines[i].split(',')
    date1 = line_items[0].split(' ')
    date2 = line_items[1].split(' ')
    weight = float(line_items[2])
    fat = float(line_items[4])
    month = date1[0]
    day = float(date1[1])
    year = float(date2[1])
    time = date2[3]
    weight_list.append(weight)
    total_weight += weight
    end = len(lines)-1
    
    if i == end:
        avg_weight = (total_weight / end)
        print(avg_weight)
        print (weight_list)

'''
	if old_month == month:
		sum += float(data)
		day_count += 1
		avg = sum / day_count
	if old_month != month:
		print('Month: %.2s   Average: %.2f' % (old_month,avg))
		sublist = [year,old_month,avg]
		avg_list.append(sublist)
		sum = float(data)
		day_count = 1
		old_month = month
	if i == len(lines)-1:
		print('Month: %.2s   Average: %.2f' % (old_month,avg))
		sublist = [year,old_month,avg]
		avg_list.append(sublist)
		sum = float(data)
		day_count = 1
		old_month = month
		'''

for i in range(0,(len(avg_list)-1),1):
	print(avg_list[i])
    
plt.ylabel('Weight in .lbs')
plt.xlabel('Date')
plt.title('Zach\'s FatStats')
plt.plot(weight_list)
plt.show()
