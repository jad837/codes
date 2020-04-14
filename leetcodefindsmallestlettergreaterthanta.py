#leetcodefindsmallestlettergreaterthantarget
#https://leetcode.com/problems/find-smallest-letter-greater-than-target/
def binary_search(arr,l,r,target):
    pass
letters = ["c", "f", "j"]
target = "k"


#countarr=[0]*26
#neg=ord('a')
n=len(letters)
l,r=0,n-1
m=0
if letters[r] <= target:
    #print("hi")
    print(letters[0])
elif letters[l] > target:
    #print("hi")
    print(letters[0])
else:
    while l<=r:
        m = l+(r-l)//2
        if letters[m] == target:
            while letters[m] == target :
                m = (m+1)%n
            #print(m)
            break
        elif letters[m] < target:
            l=m+1
        else:
            r=m-1
        #m = l+(r-l)//2
#print(m)
if letters[m]>target:
    print(letters[m])
elif letters[m]<target:
    while letters[m]<=target:
        m= (m+1)%n
    print(letters[m])
