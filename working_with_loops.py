# Sample code for Loops

print("Hello World")
# For Loop
startCounting = 1
startCounting=int(input('Where do you want to start:'))
#Range is a built-in function that will interate from start to stop
for i in range(startCounting,startCounting+10):
    print (f'The number is {i}')

# While Loop
count = 0
while count < 10:
    print (f'The Count is now {count}')
    count += 1
print (f'I completed the while loop')

