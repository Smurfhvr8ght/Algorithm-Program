def unify(A,B):
    C=A
    for i in B:
        flag = False
        for j in range(len(A)):
            if i == A[j]:
                flag = True
        if flag == False:
            C.append(i)
    C.sort()
    return C

#Test run below
A=[1,2,3,8,9,0]
B=[2,3,4,6]
print(unify(A,B))
