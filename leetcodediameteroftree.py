#leetcodediameteroftree
#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
        
        if not root:
            #print("empty")
            return
        inorder(root.left)
        print("node:",root.data,end=" ")
        inorder(root.right)

def insert_Node(root,key):
        q=[]
        q.append(root)
        while(len(q)):
            temp=q[0]
            q.pop(0)
            if not temp.left:
                temp.left = newNode(key)
                break
            else:
                q.append(temp.left)
            
            if not temp.right:
                temp.right = newNode(key)
                break
            else :
                q.append(temp.right)
def find_depth(node):
    
    if not node:
        return (0,0)
    #(diameter,depth)

    left = find_depth(node.left)
    right = find_depth(node.right)
    diameter = max([   left[0],   right[0],   left[1]+right[1]   ])
    print("Node is :",node.data)
    
    print("diameter is :",diameter)    
    return (diameter,   max([left[1],right[1]])+1) 
                

if __name__ == "__main__":
    #root = None
    #inorder(root)
    #arr=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    root = newNode(1)
    root.left = newNode(2)
    root.left.left=newNode(4)
    root.left.right = newNode(5)
    root.right = newNode(3)
    print(find_depth(root)[0])