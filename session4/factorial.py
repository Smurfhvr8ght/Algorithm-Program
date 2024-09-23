def facy(A):
    if A>0:
        if A != 1:
            return A * facy(A-1)
        else: 
            return 1
    else:
        return "number can't be 0 and below"

#Test run below
check = int(input("Put whole number to do factorial:"))
print(facy(check))
