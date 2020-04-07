
# Python3 Program to find  
# best buying and selling days 
  
# This function finds the buy sell 
# schedule for maximum profit 
def stockBuySell(price, n): 
    profit=0
    if (n == 1): 
        return
    
    i = 0
    while (i < (n - 1)): 
        
        while ((i < (n - 1)) and 
                (price[i + 1] <= price[i])): 
            i += 1
        
        if (i == n - 1): 
            break
        
        buy = i 
        i += 1
        
        while ((i < n) and (price[i] >= price[i - 1])): 
            i += 1
         
        sell = i - 1
        profit+=(price[sell]-price[buy])  
       
    print(profit)


price = [1,2,3,4,5]
n = len(price) 

stockBuySell(price, n) 

