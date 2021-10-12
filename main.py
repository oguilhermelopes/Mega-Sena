from random import sample
from time import sleep

print('-=-'*11)
print('    GERADOR DE JOGOS DA MEGA')
print('-=-'*11)
print()
print()

#Inicia a lista dos palpites
palpites = list()

#Quantidade de jogos que pretende apostar
j = int(input('Quantos jogos deseja fazer: '))
print('-=-'*11)
print()
#Quantidade de numeros que pretende jogar entre 6-15
n = int(input('Quantos numeros deseja sortear: '))
print('-=-'*11)
print()

#Gerando os Palpites
for p in range(j):
    sorteio = sorted(sample(range(1, 61), n))
    palpites.append(sorteio[:])
    #Exibe os numeros sorteados
    print(f'Jogo {p+1}: {sorteio}')
    print('-=-'*11)
    sleep(0.5)
print()    
