# A program to find the mean and median of a set of  numbers.
import math

totalNumbers = int(input("Enter the total number of inputs: "))
numbers = []
sum = 0
for i in range(1,totalNumbers + 1):
    enterNumber = int(input("Enter the number: "))
    numbers.append(enterNumber)

for i in range(totalNumbers):
    sum += numbers[i]
#Calculate the mean
mean = sum / totalNumbers
print("Mean = {}".format(mean))

#Median if total Number of inputs is odd
if totalNumbers % 2 != 0:
    results = totalNumbers / 2
    roundResults = math.ceil(results)
    medianOdd = numbers[roundResults -1 ]
    print("The median is {}".format(medianOdd))
else:
    evenResults = totalNumbers / 2
    roundEvenResults = round(evenResults)
    secondEvenResults = numbers[roundEvenResults -1] + numbers[roundEvenResults]
    finalEvenResults = secondEvenResults / 2
    print("The median is {}".format(finalEvenResults))