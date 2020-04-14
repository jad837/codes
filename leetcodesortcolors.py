#leetcodesortcolours
#https://leetcode.com/problems/sort-colors/

a=[2,0,2,1,1,0]
zero_pos,l=0,0
tp,r=len(a)-1,len(a)-1
while(l<=r):
    if a[l]==2:
        a[l],a[r]=a[r],a[l]
        r-=1
    elif a[l] == 0:
        a[zero_pos],a[l] = a[l],a[zero_pos]
        zero_pos+=1
        l+=1
    else:
        l+=1
