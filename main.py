from Jogo import Jogador
from Jogo import ESCOLHAS  
from Jogo import ESCOLHA_EXTENSO
from Jogo import decidir_vencedor
from Jogo import resultado_soma

#funções para entrada de dados
def entrada_numero(nome):
    while True:
        numeroTxt = input(f"{nome} informe um número (0-5): ").strip()
        if numeroTxt.isdigit() and 0 <= int(numeroTxt) <= 5:
            break
        print("valor inválido!")
    return int(numeroTxt)

def entrada_escolha():
    while True:
        escolhaTxt = input("Escolha par(P) ou ímpar(I): ").strip().upper()
        if escolhaTxt in ESCOLHAS:
            break
        print("Escolha inválida!")
    return escolhaTxt

#jogo
def par_impar():
    j1 = Jogador()
    j2 = Jogador()

    #para jogador 1:
    j1.nome = input("Jogador 1 informe seu nome: ")
    j1.escolha = entrada_escolha()
    j1.numero = entrada_numero(j1.nome)

    #para o Jogador 2:
    j2.nome = input("Jogador 2 informe seu nome: ")
    j2.escolha = "I" if j1.escolha == "P" else "P"
    print(f"{j1.nome} ficará com {ESCOLHA_EXTENSO[j1.escolha]} | {j2.nome} ficará com {ESCOLHA_EXTENSO[j2.escolha]}")
    j2.numero = entrada_numero(j2.nome)

    #Processamento do jogo
    vencedor = decidir_vencedor(j1, j2)
    resultado,soma = resultado_soma(j1, j2)

    #resultado final
    print(f"\n*{j1.nome}: {j1.numero}\n*{j2.nome}: {j2.numero}\n*SOMA: {soma} ({ESCOLHA_EXTENSO[resultado]})")
    print(f"*RESULTADO FINAL: jogador {vencedor.nome} venceu!")

if __name__ == "__main__":
    par_impar()