def facy(A):
    if A>0:    # make sure negative and 0 doesn't ruin the code
        if A != 1:     #checks if A is currently not 1
            return A * facy(A-1)  # return the value of A multiplied by A-1 and so on by looping to A-2, A-3 and so on
        else: 
            return 1    #Value to return at 1 to prevent infinite loop
    else:
        return "number can't be 0 and below"    #Just some error msg

#Test run below
check = int(input("Put whole number to do factorial:"))
print(facy(check))
