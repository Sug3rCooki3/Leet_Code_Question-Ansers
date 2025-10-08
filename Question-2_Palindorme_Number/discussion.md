Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


For attempt 1: it was done by converting the integers to string and reversed it using [::-1]

For attempt 2: I have done it without converting the integers to strings. 
def reverse is using while loops to reverse the number. 

Example: if the number is 1234 
in the function i = 1234
then it will initialize rev = 0
it wil then go through the while loop of i and since i = 1234 the statement becomes true, so it will then run
digit = i % 10 is getting the remainder of the number so 1234 / 10 = 123.4, remainder being 4 so digit becomes 4
next rev = rev * 10 + digit, is moving that digit number we saved (4) to the left, and since rev is 0 it becomes 0 * 10 + 4 = 4, rev = 4.
lastly it will return rev back so that rev's new value will be 4. 

it will then continue to loop over and over until i is 0
and finally palindrome is just checking if the original value i is the same as rev. 
