#gerando codigos de criptografia classica 
import random

import cripto_bib as crb
#1) cifra de cesar
def cifrcesar_encriptor(texto,chave):
    #1--encriptor= (x + b)modbase
    base=26
    palavra=texto.upper()
    palavra_encriptada=""
    for i, letra in enumerate(palavra):
        if letra.isalpha():#se o caracter estiver entre a e z  
            valor_chave = ord(chave[i % len(chave)]) - ord('A')#encontra o valor da chave na tabela ascii
            posicao = crb.calcular_mod(base, ord(letra) - ord('A') + valor_chave)#acha o valor da letra encriptada e retorna a letra encriptada
            letra_encriptada = chr(posicao + ord('A'))#encontra a letra encriptada na tabela ascii
            palavra_encriptada += letra_encriptada#forma a string com a nova palavra 
        else:
            palavra_encriptada += letra
    return palavra_encriptada#retorna a palavra encriptada

def cifrcesar_decriptor(texto,chave):
    #basicamente a mesma coisa da anterior mas a chave e invertida de acordo com a formula de decriptaçao
    #2--decriptor=(y-b)modbase
    base=26
    palavra=texto.upper()
    palavra_decriptada=""
    for i, letra in enumerate(palavra):
        if letra.isalpha():#se o caracter estiver entre a e z  
            valor_chave = ord(chave[i % len(chave)]) - ord('A')#encontra o valor da chave na tabela ascii
            posicao = crb.calcular_mod(base, ord(letra) - ord('A') + valor_chave)#acha o valor da letra decriptada e retorna a letra decriptada
            letra_decriptada = chr(posicao + ord('A'))#encontra a letra decriptada na tabela ascii
            palavra_decriptada += letra_decriptada#forma a string com a nova palavra 
        else:
            palavra_decriptada += letra
    return palavra_decriptada#retorna a palavra decriptada

def cifr_por_substuicao_encriptor(texto):
    #1)--encriptor= pi(texto)
    # vai aver uma substituiçao de cada letra por uma equivalente na chave
    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#com base no alfabeto 
    random.shuffle(alfabeto)
    pi = ''.join(alfabeto)#lembrando que a funçao pi e uma permutaçao aleatoria do alfabeto 
    print(f"a funçao pi ultilizada para encriptar e: {pi}")
    palavra=texto.upper()
    palavra_encriptada=""
    for letra in palavra:
        if letra.isalpha():
            posicao = pi.index(letra)
            letra_encriptada = chr(posicao + ord('A'))
            palavra_encriptada += letra_encriptada
        else:
            palavra_encriptada += letra
    return palavra_encriptada,pi#retorna pi junto para usar na decriptaçao 

def cifr_por_substituicao_decriptor(texto, pi):
    #2)--decriptor= pi^-1(texto)

    palavra = texto.upper()
    palavra_decriptada = ""

    for letra in palavra:
        if letra.isalpha():

            posicao = pi.index(letra)

            letra_decriptada = chr(posicao + ord('A'))#converte a letra encriptada de volta a original usando a funçao pi^-1

            palavra_decriptada += letra_decriptada

        else:
            palavra_decriptada += letra

    return palavra_decriptada
#3)cifra afin
#encrip=ax+b mod base
#decrip=a-1 (y-b)modbase
def cifra_afin_encriptor(texto, a, b, base):
    # validar que a chave 'a' e valida antes de qualquer coisa
    if crb.maximo_div_comum(a, base) != 1:
        return print("Chave 'a' invalida: mdc(a, base) precisa ser 1")
    else:
        palavra=texto.upper()
        palavra_encriptada=""
        for letra in palavra:
            if letra.isalpha():
                letra = letra.upper()
                x = ord(letra) - ord('A')  # converte letra em numero (0 a 25)

                y = crb.calcular_mod(base,(a*x)+b)  # aqui entra a formula: (a*x + b) mod base

                nova_letra = chr(y + ord('A'))  # converte numero de volta em letra
                palavra_encriptada += nova_letra
            else:
                palavra_encriptada+= letra  # mantem espacos/pontuacao sem alterar

    return palavra_encriptada
def cifra_afin_decriptor(texto, a, b, base):
    a_inverso = crb.inverso_multiplicativo(a, base)
    if a_inverso is None:
        return print("Chave 'a' invalida: nao existe inverso multiplicativo")

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            letra = letra.upper()
            y = ord(letra) - ord('A')  # converte letra cifrada em numero

            x = crb.calcular_mod(base,a_inverso*(y-b))

            letra_original = chr(x + ord('A'))
            resultado += letra_original
        else:
            resultado += letra

    return resultado

#4) cifra de vigenere
def cifra_vigenere_encriptar(texto, chave, base=26):
    chave = chave.upper()
    resultado = ""
    indice_chave = 0   # posição atual dentro da chave

    for letra in texto:
        if letra.isalpha():
            letra = letra.upper()
            x = ord(letra) - ord('A')

            letra_chave = chave[indice_chave % len(chave)]   # "roda" a chave
            k = ord(letra_chave) - ord('A')

            y = crb.calcular_mod(base, x + k)

            resultado += chr(y + ord('A'))
            indice_chave += 1        # so avanca a chave em letras (nao em espacos/pontuacao)
        else:
            resultado += letra

    return resultado


def cifra_vigenere_decriptar(texto, chave, base=26):
    chave = chave.upper()
    resultado = ""
    indice_chave = 0

    for letra in texto:
        if letra.isalpha():
            letra = letra.upper()
            y = ord(letra) - ord('A')

            letra_chave = chave[indice_chave % len(chave)]
            k = ord(letra_chave) - ord('A')

            x = crb.calcular_mod(base, y - k)

            resultado += chr(x + ord('A'))
            indice_chave += 1
        else:
            resultado += letra

    return resultado
#5) cifra de hill
def cifra_hill_encriptar(texto, matriz_chave, base=26):
    texto = texto.upper().replace(" ", "")  # normaliza: tudo maiusculo, sem espacos
    if len(texto) % 2 != 0:
        texto += "X"   # numero impar de letras: adiciona padding pra fechar o ultimo bloco

    resultado = ""
    for i in range(0, len(texto), 2):        # anda de 2 em 2 (tamanho do bloco = dimensao da matriz)
        bloco = texto[i:i+2]                 # pega o bloco atual (2 letras)
        x1 = ord(bloco[0]) - ord('A')        # converte 1a letra do bloco em numero (0 a 25)
        x2 = ord(bloco[1]) - ord('A')        # converte 2a letra do bloco em numero (0 a 25)

        # multiplica a matriz-chave pelo vetor [x1, x2], mod base
        # y1 = linha 1 da matriz * vetor  |  y2 = linha 2 da matriz * vetor
        y1 = crb.calcular_mod(base, matriz_chave[0][0]*x1 + matriz_chave[0][1]*x2)
        y2 = crb.calcular_mod(base, matriz_chave[1][0]*x1 + matriz_chave[1][1]*x2)

        resultado += chr(y1 + ord('A')) + chr(y2 + ord('A'))  # converte y1,y2 de volta em letras e concatena

    return resultado


def cifra_hill_decriptar(texto_cifrado, matriz_chave, base=26):
    a, b = matriz_chave[0]   # desmonta a matriz-chave em a,b,c,d pra facilitar as contas
    c, d = matriz_chave[1]

    det = crb.calcular_mod(base, a*d - b*c)     # determinante da matriz 2x2, reduzido mod base
    det_inv = crb.inverso_multiplicativo(det, base)   # inverso do determinante mod base
    if det_inv is None:
        # sem inverso do determinante = matriz nao e invertivel mod base = chave invalida
        return print("Matriz-chave invalida: determinante sem inverso mod base")

    # matriz inversa = det_inv * [[d, -b], [-c, a]] mod base (formula da inversa 2x2)
    matriz_inversa = [
        [crb.calcular_mod(base, det_inv * d),    crb.calcular_mod(base, det_inv * (-b))],
        [crb.calcular_mod(base, det_inv * (-c)), crb.calcular_mod(base, det_inv * a)]
    ]

    resultado = ""
    for i in range(0, len(texto_cifrado), 2):   # anda de 2 em 2 pelo texto cifrado
        bloco = texto_cifrado[i:i+2]            # pega o bloco cifrado atual (2 letras)
        y1 = ord(bloco[0]) - ord('A')           # converte 1a letra cifrada em numero
        y2 = ord(bloco[1]) - ord('A')           # converte 2a letra cifrada em numero

        # multiplica a MATRIZ INVERSA pelo vetor [y1, y2], mod base -> recupera x1, x2 originais
        x1 = crb.calcular_mod(base, matriz_inversa[0][0]*y1 + matriz_inversa[0][1]*y2)
        x2 = crb.calcular_mod(base, matriz_inversa[1][0]*y1 + matriz_inversa[1][1]*y2)

        resultado += chr(x1 + ord('A')) + chr(x2 + ord('A'))  # converte x1,x2 de volta em letras

    return resultado
#6)cifra por permutaçao
def cifra_permutacao_encriptar(texto, chave):
    n = len(chave)                          # tamanho do bloco = tamanho da chave
    texto = texto.upper().replace(" ", "")
    while len(texto) % n != 0:
        texto += "X"                        # padding para fechar o ultimo bloco

    resultado = ""
    for i in range(0, len(texto), n):
        bloco = texto[i:i+n]
        bloco_cifrado = [""] * n
        for pos_destino in range(n):
            # a letra que vai para pos_destino veio da posicao chave[pos_destino] no bloco original
            bloco_cifrado[pos_destino] = bloco[chave[pos_destino]]
        resultado += "".join(bloco_cifrado)

    return resultado


def cifra_permutacao_decriptar(texto_cifrado, chave):
    n = len(chave)

    # calcula a permutacao inversa: se chave[j] = k, entao inversa[k] = j
    inversa = [0] * n
    for j in range(n):
        inversa[chave[j]] = j

    resultado = ""
    for i in range(0, len(texto_cifrado), n):
        bloco = texto_cifrado[i:i+n]
        bloco_original = [""] * n
        for pos_destino in range(n):
            bloco_original[pos_destino] = bloco[inversa[pos_destino]]
        resultado += "".join(bloco_original)

    return resultado
#7)cifra de fluxo
def gerar_keystream(seed, tamanho, base=26):
    # gerador congruencial linear: estado = (a*estado + c) mod base
    a, c = 5, 7
    estado = seed % base
    fluxo = []
    for _ in range(tamanho):
        estado = (a * estado + c) % base
        fluxo.append(estado)
    return fluxo


def cifra_fluxo_encriptar(texto, seed, base=26):
    qtd_letras = sum(1 for ch in texto if ch.isalpha())
    keystream = gerar_keystream(seed, qtd_letras, base)

    resultado = ""
    idx = 0
    for letra in texto:
        if letra.isalpha():
            letra = letra.upper()
            x = ord(letra) - ord('A')
            k = keystream[idx]
            y = crb.calcular_mod(base, x + k)
            resultado += chr(y + ord('A'))
            idx += 1
        else:
            resultado += letra
    return resultado


def cifra_fluxo_decriptar(texto_cifrado, seed, base=26):
    qtd_letras = sum(1 for ch in texto_cifrado if ch.isalpha())
    keystream = gerar_keystream(seed, qtd_letras, base)

    resultado = ""
    idx = 0
    for letra in texto_cifrado:
        if letra.isalpha():
            letra = letra.upper()
            y = ord(letra) - ord('A')
            k = keystream[idx]
            x = crb.calcular_mod(base, y - k)
            resultado += chr(x + ord('A'))
            idx += 1
        else:
            resultado += letra
    return resultado
