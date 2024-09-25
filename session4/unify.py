def unify(A,B):
    B = list(dict.fromkeys(B))    #to remove all duplicates in B
    A = list(dict.fromkeys(A))    #to remove all duplicates in A
    C=A    #put all value in A into C
    for i in B:    #check each value of B in different iteration
        flag = False    #declaration of flag for tracking purpose
        for j in range(len(A)):    #Looping base on number of value in A and put an increasing counter in J for each value in A
            if i == A[j]:    #check for same value between i and all value of j
                flag = True    #if result true then raise flag
        if flag == False:    #check if flag is not raised
            C.append(i)    #put value i into C
    C.sort()    #sort value of C in ascending for aesthetic purpose
    return C    #give the C as result from function

#Test run below
A=[1,2,3,8,9,0]
B=[2,3,4,6]
print(unify(A,B))
