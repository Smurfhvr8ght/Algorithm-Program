def sr(T,S):
    A=""
    if len(T) == len(S):
        x=0
        for j in S:
            for i in range(T[x]):
                 A += j
            x+=1
    return A

#Test run below
T = (1,2,3)
S = "Ben"
print(sr(T,S))
