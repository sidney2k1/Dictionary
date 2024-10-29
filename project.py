testdict={"Codingal":5,"is":2,"the":3,"best":8,"site":5,"for":9,"coding":7,"at":8,"home":7,".":10}
print("the original dictionary"+str(str(testdict)))
K=int(input("Enter a number between 1-10:"))
res=0
for key in testdict:
    if testdict[key]==K:
        res+=1
print("frequency of key is:"+str(res))