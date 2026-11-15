#Class Jogador para molde e uso com construtor __init__
class Jogador:
    def __init__(self, nome="", escolha="", numero=0):
        self.nome = nome
        self.escolha = escolha
        self.numero = numero

#Para as escolhas dos jogadores
ESCOLHAS = ["P", "I"]
ESCOLHA_EXTENSO = {"P": "par", "I":"ímpar"}


#funções auxiliares
def resultado_soma(a, b):
    soma = a.numero + b.numero
    return "P" if soma % 2 == 0 else "I", soma

def decidir_vencedor(a, b):
    resultado,_ = resultado_soma(a, b)
    if a.escolha == resultado:
        return a
    return b
    