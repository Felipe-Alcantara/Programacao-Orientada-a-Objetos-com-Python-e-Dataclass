from Categoria import Categoria
from transacao import Transacao

lista_categorias = []
lista_transacoes = []
nome_arquivo = "Transação.txt"

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    lista_categorias.append(nova_categoria)
    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(descricao=descricao, valor=valor, categoria=categoria)
    lista_transacoes.append(nova_transacao)
    with open (nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Descrição: {descricao} | Valor: {valor} | Categoria: {categoria.nome}\n")
    return nova_transacao

def saldo_total():
    total = 0

    for t in lista_transacoes:
        total = total + t.valor
    with open (nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"valor total: {total}\n")
    return total
