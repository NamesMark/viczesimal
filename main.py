viczesimal = ['0','1','2','3','4','5','6','7','8','9','A','Á','B','C','Č','D','Ď','E','É','Ě']

def viczToDec(vicz): # prop is string
    decimal = 0
    vicz = vicz[::-1]
    for i in range(len(vicz) -1, -1, -1):
        print("i: ",i, ", vicz[i]: ",vicz[i], ", index: ",viczesimal.index(vicz[i]))
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

print(decToVicz(5814, ''))

print ('E * É * Ě = '),
print(decToVicz(viczToDec('E')*viczToDec('É')*viczToDec('Ě'),''))