def first_Occurence(arr,x):
    l=0
    r=len(arr)-1
    first_occurence = len(arr)-1
    while(l<=r):
        middle=l+(r-l)//2
        if arr[middle] >= x:
            first_occurence = middle
            r = middle - 1
        else:
            l = middle + 1
    return first_occurence
def range_search(arr,x):
    first = first_Occurence(arr,x)
    last = first_Occurence(arr,x+1)-1
    if first <= last :
        return (first,last)
    else:
        return (-1,-1)

if __name__ == "__main__":
    arr=[2,7,4,1,8,1]
    x=8
    