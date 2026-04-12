# Q07. Reverse a Number (while loop)
#
# Ask the user for a positive integer.
# Print the reverse of the number using a while loop.
#
# Sample Input 1:   Enter a number: 1234
# Sample Output 1:  Reversed: 4321
#
# Sample Input 2:   Enter a number: 5000
# Sample Output 2:  Reversed: 5

# --- YOUR CODE HERE ---
n = input("Enter a number: ")
rev = 0
rem = 0
l = len(n)
n = int(n)
i = 0
while i < l:
    rem = n%10
    rev = 10*rev + rem
    n = int(n/10)
    i = i + 1
print(f"Reversed: {rev}")
