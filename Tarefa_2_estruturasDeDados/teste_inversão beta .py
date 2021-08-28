def inserir(destino, inddestino, origem, indorigem):
    destino[inddestino] = ConversorAsc2(origem[indorigem])

def liVazia(ult, pri):
    if ult == pri:
        return True
    else:
        return False

def ConversorAsc2 (c):
    #Em cada condicional é verificado se, o ID da letra fornecida está entre os ID's das letras maiuscula e minusculas
    #minusculas com acento, se estiver enão esta é substituida por a letra sem acento.
    #Caso o ID não seja de uma letra com acento, ela é apenas retornada, pois não precisa ser substituida.
    if ord(c) >= 65 and ord(c) <= 90:
        letra_mudada = chr(ord(c)+32)
    elif ord(c) < 192:
        letra_mudada = c
    elif (ord(c) >= 192) and (ord(c) <= 197) or ((ord(c) >= 224) and (ord(c) <= 229)):
        letra_mudada = 'a'
    elif (ord(c) >= 200) and (ord(c) <= 203) or ((ord(c) >= 232) and (ord(c) <= 235)):
        letra_mudada = 'e'
    elif (ord(c) >= 204) and (ord(c) <= 207) or ((ord(c) >= 236) and (ord(c) <= 239)):
        letra_mudada = 'i'
    elif (ord(c) >= 210) and (ord(c) <= 214) or ((ord(c) >= 242) and (ord(c) <= 246)):
        letra_mudada = 'o'
    elif (ord(c) >= 217) and (ord(c) <= 220) or ((ord(c) >= 249) and (ord(c) <= 252)):
        letra_mudada = 'u'
    elif ord(c) == 200 or ord(c) == 231:
        letra_mudada = 'c'
    return letra_mudada

entrada = input("Digite uma frase:")
primeiro = 0
ultimo = 0
maxTam = len(entrada)
frase = [0]*len(entrada)  #alocação de tamanho de acordo com a entrada

#Inserindo letra por letra na lista(vetor), utilizando variaves de controle
for i in range(len(entrada)):
    if frase[ultimo] == 0 and ultimo <= maxTam:
        inserir(frase, ultimo, entrada, ultimo)
        ultimo = ultimo + 1

#invertendo as letras do frase.
inicio = 0
esp = 0
aux = 0
for i in range(len(frase)):
    #este trecho enverte aspalavras excerto ultima palavra da frase
    if frase[i] == " ":
        esp = i
        for j in range(esp-1, inicio-1, -1):
            inserir(frase, j, entrada, aux)
            aux = aux+1
        inicio = esp
        aux = esp+1
    #Ja este trecho é apenas para inver ter a ultima palavra da frase
    if i == len(frase)-1:
        inicio = esp
        aux = esp + 1
        esp = i
        for j in range(esp, inicio, -1):
            inserir(frase, j, entrada, aux)
            aux = aux+1

for i in range(len(frase)):
    print(frase[i], end=" ")




