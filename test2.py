def sumay(x,y,z):
    if x>z and y>z:
        suma=x+y
        return suma
    elseif x>y and z>y:
        suma=x+z
        return suma
    else:
        suma=y+z
        return suma

total=sumay(10,11,12)
print total
