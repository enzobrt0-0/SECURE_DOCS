
import math as m


def calcular_mod(base, numero):
    if base == 0:
        return print("BASE NAO PODE SER ZERO : ERRO")
    else:
        return numero % base


def maximo_div_comum(num1, num2):
    #usa a funçao gcd para calcular o maximo divisor com auxilio da math
    return m.gcd(num1, num2)


def minimo_div_comum(num1, num2):
    return abs(num1 - num2) // m.gcd(num1, num2)


def numeros_primos(num1, num2):
    #se o maximo divisor comum for 1 , os numeros sao primos
    if m.gcd(num1, num2) == 1:
        print(f'os numeros :{num1} e {num2} sao primos')
        return True
    else:
        print(f'os numeros :{num1} e {num2} nao sao primos')
        return False


def algoritmo_de_euclides(numerador, divisor):
    # o algoritmo tem como objetivo divisoes sucessivas
    if divisor == 0:
        return numerador
    else:
        return algoritmo_de_euclides(numerador, numerador % divisor)
def inverso_multiplicativo(numero, modulo):
    # testa todos os valores a * a(-1) == 1 mod m
    for x in range(1, modulo):
        if (numero * x) % modulo == 1:
            return x
    return None  # não existe inverso
def euclides_estendido(numero, exponente):
    # caso base: se expoente = 0, retorna mdc = a e coeficientes (1,0)
    if exponente == 0:
        return numero, 1, 0
    # chamada recursiva
    mdc, x1, y1 = euclides_estendido(exponente, numero % exponente)
    # atualiza coeficientes
    x = y1
    y = x1 - (numero // exponente) * y1
    return mdc, x, y
def exp_mod(numero, expoente, modulo):
    resultado = 1
    numero = numero % modulo  # reduz base
    while expoente > 0:
        if expoente % 2 == 1:      # se expoente é ímpar
            resultado = (resultado * numero) % modulo
        numero = (numero * numero) % modulo     # quadrado da base
        expoente//= 2             # divide expoente por 2
    return resultado
def phi_euler(n):
    # começa com resultado = n
    resultado = n
    fator = 2  # primeiro primo

    # percorre possíveis fatores até √n
    while fator * fator <= n:
        if n % fator == 0:  # se 'fator' divide n
            while n % fator == 0:
                n //= fator  # remove todas as ocorrências do fator
            resultado -= resultado // fator  # aplica fórmula (1 - 1/p)
        fator += 1  # próximo número

    # se sobrou um primo maior que √n
    if n > 1:
        resultado -= resultado // n

    return resultado
def teorema_chines_resto(congruencias, modulos):
    # produto de todos os modulos
    produto_total = 1
    for mod in modulos:
        produto_total *= mod

    soma = 0
    # percorre cada congruência (valor e módulo)
    for congruencia, mod in zip(congruencias, modulos):#combina as duas listas para percorrer cada congruência de forma organizada.
        parte = produto_total // mod        # parte do produto
        inverso = inverso_multiplicativo(parte, mod)  # inverso de parte mod mod
        soma += congruencia * parte * inverso

    return soma % produto_total  # solução única módulo produto_total




