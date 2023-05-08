viczesimal = ['0','1','2','3','4','5','6','7','8','9','A','Á','B','C','Č','D','Ď','E','É','Ě']

def viczToDec(vicz): # prop is string
    decimal = 0
    vicz = vicz[::-1]
    for i in range(len(vicz) -1, -1, -1):
        print("i: ",i, ", vicz[i]:",vicz[i], ", 20^i: ",20**i, ", value: ",viczesimal.index(vicz[i]), )
        decimal += viczesimal.index(vicz[i]) * 20 ** i
    return decimal

def decToVicz(decimal, vicz): # prop is int
    remainder = decimal % 20
    vicz = viczesimal[remainder] + vicz
    if decimal > 20:
        decimal = decimal // 20
        return decToVicz(decimal, vicz)
    else:
        return vicz

def processInput(input): # prop is string
    block = ''
    for i in range(len(input)):
        if input[i] != '+' and input[i] != '-' and input[i] != '*' and input[i] != '/':
            block += input[i]
    


testValue = viczToDec('ČAČ')
print(testValue)

print(decToVicz(925231, ''))
print(decToVicz(884512, ''))

print ('5DC1Á-5AÁ5B = '),
print(decToVicz(viczToDec('5DC1Á')-viczToDec('5AÁ5B'),''))
print(viczToDec('51DĚ'))

print("42 is ",decToVicz(42, ''))
print("255 is ",decToVicz(255, ''))

print("22 is ",viczToDec('22'))
print("C5 is ",viczToDec('C5'))