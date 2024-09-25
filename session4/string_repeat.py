def sr(T,S):
    A=""    #To keep track of the current result
    if len(T) == len(S):
        x=0    #counter to make sure that value in tupple is checked as needed
        for j in S:    #get value of each letter in string and put it to j at different iteration
            for i in range(T[x]):    #to loop a certain number of time base on the value of tupple from position x
                 A += j    # put string to result variable
            x+=1    #increase the counter
    return A    #returen value of result

#Test run below
T = (1,2,3)
S = "Ben"
print(sr(T,S))
