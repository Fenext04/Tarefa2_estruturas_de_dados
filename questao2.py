import time

fila = [1,2,3,4,5, None]
valor = int(input("Insira um valor para furar a fila: "))

primeira_posicao = 0
ultima_posicao = 5
auxiliar = 0


print(fila)
print(f"Primeira posição: {fila[primeira_posicao]}")
print(f"Ultima posição: {fila[ultima_posicao]}")
print(f"{valor} está no final da fila, furando a fila e indo para a primeira posição...")
comprimento_fila = len(fila) - 1
fila[ultima_posicao] = valor
for c in range(comprimento_fila,-1,-1):
    if (c < comprimento_fila):
        print(fila)
        auxiliar = fila[c+1]
        fila[c+1] = fila[c]
        fila[c] = auxiliar
        time.sleep(2)
print(fila)


