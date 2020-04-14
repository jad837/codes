#leetcodeSubtracttheProductandSumofDigitsofanInteger
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
n=234
p=1
s=0
while n>0:
    d=n%10
    p*=d
    s+=d
    n=n//10
#    print(d)
#print(p)
#print(s)
print (p-s)