"""
Check Tutorial tab to know how to to solve.

The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123
"""

if __name__ == '__main__':
    n = int(input())
    print(''.join(list(map(str, [x for x in range(1, n + 1)]))))
