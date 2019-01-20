# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .
[print(num) for num in range(1,21)]

# 4-4. One Million: Make a list of the numbers from one to one million, 
# and then use a for loop to print the numbers . (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .) 
# [print(num) for num in range(1, 1000001)]

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million . 
# Also, use the sum() function to see how quickly Python can add a million numbers . 

oneMillion = list(range(1,1000001))
print("Min > "+ str(min(oneMillion)))
print("Max > "+ str(max(oneMillion)))
print("Sum > "+ str(sum(oneMillion)))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 .
#  Use a for loop to print each number .

