# importação de bibliotecas.
import os           # para comandos ao SO.
import random       # para gerar numbers aleatórios.

#nome = input('Digite o seu nome: ')
nome = 'João'
print(f'\nSeja bem vindo {nome}!\n')
input('Pressione ENTER para começar: ')
os.system('cls')    # Limpa a tela.


vidas = 6  # Limite de erros.

# lista com 10 animais.
lista_palavras = ['gato', 'cachorro', 'tigre', 'elefante', 'onca',
                  'arara', 'gaviao', 'macaco', 'jacare', 'porco']

# Sorteia e converte para maiúsculo.
palavra_selecionada = random.choice(lista_palavras).upper()

# Quantidade de underlines.
palavra_codificada = ['_'] * len(palavra_selecionada)


# Cabeçalho do jogo.
def menu(palavra_selecionada):
    print(f'\nA palavra tem {len(palavra_selecionada)} letras.')
    print('Dica: animal.')
    print(f'Vidas = {vidas}\n')

    for letra in palavra_codificada:
        print(letra, end=' ')  # _ _ _ _ _ _
    print()  # Pula linha.


# Jogo
while '_' in palavra_codificada and vidas > 0:

    menu(palavra_selecionada)

    letra = input('Digite uma letra: ').upper()  # Digita uma letra.

    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra == palavra_selecionada[i]:
            palavra_codificada[i] = letra
            acertou = True

    if acertou:
        print('Parabéns a letra!\n')
    else:
        print('Errou, essa letra não existe!\n')
        vidas = vidas - 1

if '_' in palavra_codificada:
    print(f'\nNão foi dessa vez! 😥')
else:
    print(f'\nVocê ganhou! 😁')

print(f'A resposta é {palavra_selecionada}\n')
