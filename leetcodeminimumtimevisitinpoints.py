#leetcodeminimumtimevisitinpoints
#https://leetcode.com/problems/minimum-time-visiting-all-points/


points = [[1,1],[3,4],[-1,0]]
min_time=0
for i in range(1,len(points)):
    x=abs(points[i][0]-points[i-1][0])
    y=abs(points[i][1]-points[i-1][1])
    if x<y:
        min_time+=y
    else:
        min_time+=x
print(min_time) 