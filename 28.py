
def sum (n):

    n1 = int(n)
    n2 = int(str(n) * 2)  
    n3 = int(str(n) * 3)  
    n4 = int(str(n) * 4)

    res = n1 + n2 + n3 + n4

    print(f"res = n1 + n2 + n3 + n4 = {n1} + {n2} + {n3} + {n4} = {res}")
    return res 
    
print(sum(3))
