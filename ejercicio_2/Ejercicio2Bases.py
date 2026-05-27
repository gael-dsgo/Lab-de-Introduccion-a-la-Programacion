num = int(input("Ingresa un número entero: "))
n=num
binario=""
while n>0:
    residuo=n%2
    binario=str(residuo) + binario
    n=n//2
print("En binario sería:", binario)

n=num
octal=""
while n>0:
    residuo=n%8
    octal=str(residuo)+octal
    n=n//8
print("En octal sería:", octal)

n=num
hexa=""
while n>0:
    residuo=n%16
    if residuo==10:
        hexa="A" + hexa
    elif residuo==11:
        hexa="B" + hexa
    elif residuo==12:
        hexa="C" + hexa
    elif residuo==13:
        hexa="D" + hexa
    elif residuo==14:
        hexadl="E" + hexa
    elif residuo==15:
        hexal="F" + hexa
    else:
        hexa = str(residuo) + hexa
    n = n // 16
print("En hexadecimal sería:", hexa)