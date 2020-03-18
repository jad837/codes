import PrintMatrix

# Implement your solution by completing the below function
def letterCombinations(digits):
    res = []
    letters_for_numbers= ["", "", "abc", "def", "ghi", "jkl", 
            "mno", "pqrs", "tuv", "wxyz"]
    #find no of digits from string of digits and separate them
    numbers=[]
    length = len(digits)
    #length of string as well as digits array is same eg. 23 output = ad , ae ,etc.
    for i in range(length):
        numbers.append(int(digits[i]))
    letter_queue = [] 
    letter_queue.append("") 
  
    while len(letter_queue) != 0: 
        s = letter_queue.pop() 
  
        # If complete word is generated 
        # push it in the list 
        if len(s) == length: 
            res.append(s) 
        else: 
  
            # Try all possible letters for current digit 
            # in number[] 
            for letter in letters_for_numbers[numbers[len(s)]]: 
                letter_queue.append(s + letter) 
  
    # Return the generated list 
    
    return sorted(res)

    

if __name__ == '__main__':
    digits = input()
    result = letterCombinations(digits)
    PrintMatrix.OneDMatrix(result, " ")
