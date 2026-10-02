import cripto_bib as crb
import criptobib_classic as cc


def ler_int(mensagem):
    return int(input(mensagem))


def ler_lista_int(mensagem):
    # le uma lista de inteiros separados por virgula, ex: "3,1,4,2"
    bruto = input(mensagem)
    return [int(x.strip()) for x in bruto.split(",")]


def menu_matematica():
    while True:
        print("\n---- Biblioteca de matematica (cripto_bib) ----")
        print("1) Calcular mod")
        print("2) Maximo divisor comum (mdc)")
        print("3) Minimo multiplo comum (mmc)")
        print("4) Verificar se dois numeros sao coprimos")
        print("5) Algoritmo de Euclides (mdc recursivo)")
        print("6) Inverso multiplicativo")
        print("7) Euclides estendido")
        print("8) Exponenciacao modular")
        print("9) Funcao phi de Euler")
        print("10) Teorema chines do resto")
        print("0) Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            base = ler_int("Base: ")
            numero = ler_int("Numero: ")
            print("Resultado:", crb.calcular_mod(base, numero))

        elif opcao == "2":
            n1 = ler_int("Numero 1: ")
            n2 = ler_int("Numero 2: ")
            print("MDC:", crb.maximo_div_comum(n1, n2))

        elif opcao == "3":
            n1 = ler_int("Numero 1: ")
            n2 = ler_int("Numero 2: ")
            print("MMC:", crb.minimo_div_comum(n1, n2))

        elif opcao == "4":
            n1 = ler_int("Numero 1: ")
            n2 = ler_int("Numero 2: ")
            crb.numeros_primos(n1, n2)

        elif opcao == "5":
            numerador = ler_int("Numerador: ")
            divisor = ler_int("Divisor: ")
            print("MDC:", crb.algoritmo_de_euclides(numerador, divisor))

        elif opcao == "6":
            numero = ler_int("Numero: ")
            modulo = ler_int("Modulo: ")
            resultado = crb.inverso_multiplicativo(numero, modulo)
            print("Inverso multiplicativo:", resultado if resultado is not None else "nao existe")

        elif opcao == "7":
            numero = ler_int("Numero: ")
            expoente = ler_int("Expoente: ")
            mdc, x, y = crb.euclides_estendido(numero, expoente)
            print(f"mdc={mdc}, x={x}, y={y}")

        elif opcao == "8":
            numero = ler_int("Base: ")
            expoente = ler_int("Expoente: ")
            modulo = ler_int("Modulo: ")
            print("Resultado:", crb.exp_mod(numero, expoente, modulo))

        elif opcao == "9":
            n = ler_int("Numero: ")
            print("Phi de Euler:", crb.phi_euler(n))

        elif opcao == "10":
            congruencias = ler_lista_int("Congruencias (separadas por virgula): ")
            modulos = ler_lista_int("Modulos (separados por virgula): ")
            print("Solucao:", crb.teorema_chines_resto(congruencias, modulos))

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def menu_cifras():
    while True:
        print("\n---- Cifras classicas (criptobib_classic) ----")
        print("1) Cesar - encriptar")
        print("2) Cesar - decriptar")
        print("3) Substituicao - encriptar")
        print("4) Substituicao - decriptar")
        print("5) Afim - encriptar")
        print("6) Afim - decriptar")
        print("7) Vigenere - encriptar")
        print("8) Vigenere - decriptar")
        print("9) Hill - encriptar")
        print("10) Hill - decriptar")
        print("11) Permutacao - encriptar")
        print("12) Permutacao - decriptar")
        print("13) Fluxo - encriptar")
        print("14) Fluxo - decriptar")
        print("0) Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            texto = input("Texto: ")
            chave = input("Chave (palavra): ")
            print("Resultado:", cc.cifrcesar_encriptor(texto, chave))

        elif opcao == "2":
            texto = input("Texto: ")
            chave = input("Chave (palavra): ")
            print("Resultado:", cc.cifrcesar_decriptor(texto, chave))

        elif opcao == "3":
            texto = input("Texto: ")
            resultado, pi = cc.cifr_por_substuicao_encriptor(texto)
            print("Resultado:", resultado)
            print("Guarde essa permutacao pi para decriptar depois:", pi)

        elif opcao == "4":
            texto = input("Texto cifrado: ")
            pi = input("Permutacao pi usada na encriptacao: ")
            print("Resultado:", cc.cifr_por_substituicao_decriptor(texto, pi))

        elif opcao == "5":
            texto = input("Texto: ")
            a = ler_int("Chave a: ")
            b = ler_int("Chave b: ")
            base = ler_int("Base (ex: 26): ")
            print("Resultado:", cc.cifra_afin_encriptor(texto, a, b, base))

        elif opcao == "6":
            texto = input("Texto cifrado: ")
            a = ler_int("Chave a: ")
            b = ler_int("Chave b: ")
            base = ler_int("Base (ex: 26): ")
            print("Resultado:", cc.cifra_afin_decriptor(texto, a, b, base))

        elif opcao == "7":
            texto = input("Texto: ")
            chave = input("Chave (palavra): ")
            print("Resultado:", cc.cifra_vigenere_encriptar(texto, chave))

        elif opcao == "8":
            texto = input("Texto cifrado: ")
            chave = input("Chave (palavra): ")
            print("Resultado:", cc.cifra_vigenere_decriptar(texto, chave))

        elif opcao == "9":
            texto = input("Texto: ")
            a = ler_int("Matriz [0][0]: ")
            b = ler_int("Matriz [0][1]: ")
            c = ler_int("Matriz [1][0]: ")
            d = ler_int("Matriz [1][1]: ")
            print("Resultado:", cc.cifra_hill_encriptar(texto, [[a, b], [c, d]]))

        elif opcao == "10":
            texto = input("Texto cifrado: ")
            a = ler_int("Matriz [0][0]: ")
            b = ler_int("Matriz [0][1]: ")
            c = ler_int("Matriz [1][0]: ")
            d = ler_int("Matriz [1][1]: ")
            print("Resultado:", cc.cifra_hill_decriptar(texto, [[a, b], [c, d]]))

        elif opcao == "11":
            texto = input("Texto: ")
            chave = ler_lista_int("Chave, permutacao de indices (ex: 2,0,3,1): ")
            print("Resultado:", cc.cifra_permutacao_encriptar(texto, chave))

        elif opcao == "12":
            texto = input("Texto cifrado: ")
            chave = ler_lista_int("Chave, permutacao de indices (ex: 2,0,3,1): ")
            print("Resultado:", cc.cifra_permutacao_decriptar(texto, chave))

        elif opcao == "13":
            texto = input("Texto: ")
            seed = ler_int("Semente (seed): ")
            print("Resultado:", cc.cifra_fluxo_encriptar(texto, seed))

        elif opcao == "14":
            texto = input("Texto cifrado: ")
            seed = ler_int("Semente (seed): ")
            print("Resultado:", cc.cifra_fluxo_decriptar(texto, seed))

        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def main():
    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1) Biblioteca de matematica (cripto_bib)")
        print("2) Cifras classicas (criptobib_classic)")
        print("0) Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menu_matematica()
        elif opcao == "2":
            menu_cifras()
        elif opcao == "0":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
