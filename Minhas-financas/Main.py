from Categoria import Categoria
from transacao import Transacao
from Ultilitários import cadastrar_categoria, cadastrar_transacao, saldo_total

categoria_receitas = cadastrar_categoria("Receitas")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_contas = cadastrar_categoria("Contas fixas")
categoria_lazer = cadastrar_categoria("Lazer")

cadastrar_transacao(descricao="Salário", valor=10000.0, categoria=categoria_receitas)

cadastrar_transacao(descricao="Mesada da mamãe", valor=50.0, categoria=categoria_receitas)

cadastrar_transacao(descricao="Ingresso do show", valor=-150, categoria=categoria_lazer)

cadastrar_transacao(descricao="Conta de luz", valor=-100, categoria=categoria_contas)

cadastrar_transacao(descricao="Disney", valor=-4000, categoria=categoria_viagens)

total = saldo_total()
print(f"Saldo total: {total}")