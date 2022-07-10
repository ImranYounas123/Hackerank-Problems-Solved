
def stairCase(n):
    for i in range(n):
        for j in range(n):
            if j >= 5-i:
                print("#",end= " ")
            else:
                print(" ", end=" ")
        print("\n")
stairCase(6)    