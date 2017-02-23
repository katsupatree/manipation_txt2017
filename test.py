import pandas as pd
#as is equiv to <-
#Learning about classes, attribute =-attr. This is a complicated subject at the moment just know that the "." linked to class
#Name space
#Class attribute is only defined in the "Test". attr is linked to the class name (in this eg Test)
class Test:
    attr = "This is an attribute"

    def func(arg):
        return arg
#file not readable
fn = "data/DM TB10_4-P25 crude.txt"
pd.read_csv(fn, sep='\t')

file_obj = open(fn, "r")
fn = "data/DM TB10_4-P25 crude.txt"
pd.read_csv(fn, sep='\t')

file_obj = open(fn, "r")
file_obj
print (file_obj.read(5))
print (file_obj.read(5000)) ##Note that .read will read per character not per line

#not this command loads the file in temp memory and will only run through once

#to add to memory
file_obj = open(fn, "r")
lines = [] # where we will store our lines
#init python list or in other languages an array
count = 0
#command below it will read every line in txt file and loading it to memory and assigning it to the var "line"
for line in file_obj.readlines():
    lines.append(line)
    count += 1

lines[0:10]

#import data - lines of use
data_points = []
#creating a new list which has nothing in it at the moment
