print("hola mundo")#imprim normal
print("como le va")
b = "nel pastel"
print(b)
print("------")
for a in range(5):#ciclo de cinco
    a+=1
    print(a)

if 10>5:#condiciones
    print("hi")
else:
    print("xd")
print("------")
def holis():#funcion
    print("funcion 1")
    print("funcion 2")#comentario
print("------")
for d in range(3):
    d+=1
    holis()#llamada de la funcion
print("------")
def mult(uno,dos):
    print(uno*dos)
mult(2.5,6)
mult(7,6)
print("------")
def fact(valor):#recursivo factorial 4
    if valor>0:
        mult=valor*fact(valor-1)
        return mult
    else:
        return 1
print(fact(4))
print("------")
milista=["a","b","c","d","e"]
print(milista[:])#toda la lista
print(milista[2])#posicion
print(milista[0:2])#posicion 0,1,2
milista.extend([2,3,4])#mas objetos en la lista
print("------")
milista.remove("b")
print("se removio" ,milista[:])
print("------")
tupla=("alex",15,1.75,15)#tupla/no se puede modificar
print(tupla[1])
print("------")
mitupla=list(tupla)#de tupla a lista

midiccionario={"hi":"xd"}
print(midiccionario["hi"])#devulve
