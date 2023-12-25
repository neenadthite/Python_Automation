# coding: utf-8
import os
import re

with open('sensorlog', 'r') as file:
    for line in file:
        if 'Heat' in line:
            print (line)
            result = re.search('([^\s]+)°C', line)
            print (result)
            if result:
                temperaturereading = result.group()
                print(result.group())

with open('sensorlog', 'r') as file:
    for line in file:
        if 'Moisture' in line:
            print (line)
            result = re.search('([^\s]+)g.m-3', line)
            print (result)
            if result:
                humidityreading = result.group()
                print(result.group())

with open('sensorlog', 'r') as file:
    for line in file:
        if 'Visibility' in line:
            print (line)
            result = re.search('([^\s]+)cd', line)
            print (result)
            if result:
                luminescencereading = result.group()
                print(result.group())

# Opening a file
file1 = open('finalreading', 'a')

a = 'Temperature : ' + temperaturereading + '\n'
b = 'Humidity : ' + humidityreading + '\n'
c = 'Luminescence : ' + luminescencereading + '\n'
d = [a,b,c]

# Writing multiple strings
# at a time
file1.writelines(d)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('finalreading', 'r')
print(file1.read())
file1.close()
