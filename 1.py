"""Given N gold wires, each wire has a length associated with it.
At a time, only two adjacent small wres assembled at the end of a
large wire and the cost of forming is the sum of their length. Find
the minimum cost when all wires are assembled to form a single
wire.
For Example: Suppose, Arr[] = {7, 6, 8, 6, 1, 1}
{7, 6, 8, 6, 1, 1} - {7, 6, 8, 6, 2}, cost = 2
{7, 6, 8, 6, 2} - {7, 6, 8, 8}, cost = 8
{7, 6, 8, 8} - {13, 8, 8}, cost =13
{13, 8, 8} - {13, 16}, cost = 16
{13, 16} - {29}, cost = 29
2 + 8 + 13 + 16 + 29 = 68
Hence, the minimum cost to assemble all gold wires is : 68
Constraints:
1 <= N <= 30
1<= Arr[] <= 100
Example 1:
Input:
6 -> Value of N, represents size of Arr
7 -> Value of Arr[0], represents length of 1st wire
6 -> Value of Arr[1], represents length of 2nd wire
8 -> Value of Arr[2], represents length of 3rd wire
6 -> Value of Arr[3], represents length of 4th wire
-1 -> Value of Arr[4], represents length of 5th wire
1 -> Value of Arr[5], represents length of 6th wire
Output:
68
Example 2:
Input:
4 -> Value of N, represents size of Arr
12 -> Value of Arr[0], represents length of 1st wire
2 -> Value of Arr[1], represents length of 2nd wire
2 -> Value of Arr[2], represents length of 3rd wire
5-> Value of Arr[3], represents length of 4th wire
Output:
34
"""



n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

total_cost = 0

while len(arr) > 1:

    # sort the array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # take two smallest wires
    first = arr[0]
    second = arr[1]

    cost = first + second
    total_cost += cost

    # remove the first two wires
    arr.pop(0)
    arr.pop(0)

    # add new combined wire
    arr.append(cost)

print(total_cost)