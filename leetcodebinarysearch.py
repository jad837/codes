#leetcodePalindromeNumber
#https://leetcode.com/problems/palindrome-number/

n=int(input())
arr=[]
while(n>0):
    arr.append(n%10)
    n=n//10
x=len(arr)
for i in range(x//2):
    if arr[i]!=arr[x-1-i]:
        print("False")
        break

