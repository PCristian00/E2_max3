def max_3(a,b,c):
    if a >= b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c


x=float(input("Inserire primo numero:"))
y=float(input("Inserire secondo numero:"))
z=float(input("Inserire terzo numero:"))
max=(max_3(x,y,z))
print("Il numero più grande è "+str(max))