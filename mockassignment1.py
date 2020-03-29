#https://www.hackerrank.com/contests/launch-assessment-mock-2-batch-1/challenges/patterns-matching


n=int(input())
word=[]
for i in range(n):
    word.append(input())
pattern=input()
alphabets=[0]*52
count=0
series=[]
for i in range(len(pattern)):
    if ord(pattern[i]) >= 65 and ord(pattern[i])<= 90 :
        alphabets[ord(pattern[i])-65]+=1
        count+=1
        series.append(ord(pattern[i])-65)
    elif ord(pattern[i]) >= 97 and ord(pattern[i])<= 122 :
        alphabets[ord(pattern[i])-97+26]+=1
        count+=1
        series.append(ord(pattern[i])-97+26)

#print(alphabets[:26])
#print(alphabets[26:])
for i in range(n):
    check=list(alphabets)
    sequence=list(series)
    c=count
    s=0
    #print(word[i])
    flag=True
    for j in range(len(word[i])):
        if ord(word[i][j]) >= 65 and ord(word[i][j]) <=90 :
            if check[ord(word[i][j])-65] > 0 :
                check[ord(word[i][j])-65]-=1
                if sequence[s]!= (ord(word[i][j])-65):
                    flag=False
                c-=1
                s+=1
            else:
                flag=False
                break
        elif ord(word[i][j]) >= 97 and ord(word[i][j])<= 122 :
            if check[ord(word[i][j])-97+26] > 0:
                check[ord(word[i][j])-97+26]-=1
                c-=1
                if sequence[s]!=(ord(word[i][j])-97+26):
                    flag=False
                s+=1
            else :
                #print(word[i][j])
                continue
    if c==0 and flag==True:
        #print(word[i])
        print("true")
        continue
    print("false")

    