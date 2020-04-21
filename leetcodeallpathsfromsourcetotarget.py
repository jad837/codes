#leetcodeallpathsfromsourcetotarget
#https://leetcode.com/problems/all-paths-from-source-to-target/
from collections import defaultdict
grid = [[1,2], [3], [3], []] 
s=0
d={}
target=len(grid)-1
