# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Este é controller painel administrativo da loja
# Responsável por add produtos e gerenciar a loja
# -------------------------------------------------------------------------

@auth.requires_membership('funcionario')
def index():
    response.title = "Painel administrativo"
    produtos = db(Produtos).count()
    vendas = db(Vendas).count()
    clientes = db(db.auth_membership.group_id == 1).count()
    funcionarios = db(db.auth_membership.group_id == 2).count()
    return locals()

@auth.requires_membership('funcionario')
def categorias():
    categorias = db(Categorias).select()
    # categorias = SQLFORM.grid(Categorias)
    return dict(categorias=categorias)


@auth.requires_membership('funcionario')
def produtos():

    return dict()
@auth.requires_membership('funcionario')
def vendas():

    return dict()

@auth.requires_membership('funcionario')
def pagamentos():

    return dict()

@auth.requires_membership('funcionario')
def clientes():

    return dict()


def funcionarios():

    return dict()