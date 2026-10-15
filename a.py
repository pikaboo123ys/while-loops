# take input from user
num = int(input("enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10 # last digit
    sum += digit ** 3
    temp //= 10 # remove the last digit

# display results 
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
