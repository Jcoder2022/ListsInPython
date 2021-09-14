# lists in depth
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)  # will print exact same as above, ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

# To Access via index
print(names[0])
print(names[-1])  # will print Mary
print(names[-2])  # will print Sarah

# we may also use colon
# whenever we access index based items it creates a new list
print(names[2:])  # starting from index 2 to the end of list, o/p will be ['Mosh', 'Sarah', 'Mary']
print(names[2:4])  # will from 2 to 4 excluding index 4 element.  o/p will be ['Mosh', 'Sarah']
print(names[:])  # will consider start as zero and last. o/p will be  ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

# Assume name John was not considered to have h.

names[0] = 'Jon'
print(names)

# Exercise

# find a largest number in a list

list_of_int = [800,10, 20, 30, 40, 100, 50, 60, 70, 80, 90, 110, 110]
largest_number = 0
for number in list_of_int:
    if largest_number <= number:
        largest_number = number

print(largest_number)
