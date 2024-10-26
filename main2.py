testdict={"Codingal":2,"is":2,"the":2,"best":2,"site":1}
print("the original dictionary"+str(str(testdict)))
K=2
res=0
for key in testdict:
    if testdict[key]==K:
        res+=1
print("frequency of key is:"+str(res))