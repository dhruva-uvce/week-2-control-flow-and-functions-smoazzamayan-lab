# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
n = input("Enter a number: ")
l = len(n)
n = int(n)
i = 0
dig = 0
sum = 0
temp = n
while i < l:
    dig = temp%10
    sum = sum + dig
    temp = int(temp/10)
    i = i+1
print(f"Sum of digits of {n} = {sum}")
