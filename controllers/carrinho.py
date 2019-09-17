# -*- coding: utf-8 -*-
# Controller para gerencia o carrinho
def index():
    categorias = db(db.categorias).select() # Lista todas categorias
    return locals()


def adicionar():
    # Busca informações do produto de acordo com id passado no request.args[0]
    produto = db(Produtos.id==request.args[0]).select().first()

    # Verifica se carrinho já possui item
    if len(session.carrinho) == 0:
        session.carrinho = []

    # Adiciona item no carrinho
    session.carrinho.append(produto)

    # Redireciona para controller atual no action index
    redirect(URL('index'))

def limpar():

    # Verifica se carrinho existe e limpa
    if session.carrinho:
        session.carrinho.clear()

    # Redicionar para controller atual e action index
    redirect(URL('index'))

def teste():

    return dict(message="teste")


