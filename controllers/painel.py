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

# Lista as categorias
@auth.requires_membership('funcionario')
def categorias():
    categorias = db(Categorias).select()
    # categorias = SQLFORM.grid(Categorias)
    return dict(categorias=categorias)

@auth.requires_membership('funcionario')
def categoria():
    id = request.args[0]
    categoria = db(Categorias.id == id).select().first()
    return dict(categoria=categoria)

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


def view():
    tablename = 'categorias'
    registro = db([tablename].id==request.args[1]).select().first()

   # table = request.args[0]

    return dict(registro=registro)

def edit():
    # pega nome da tabela na url exemplo  categorias
    tablename = request.args[0]
    # Pega o id na url após nome da tabela categorias/3 e cria o form
    form = SQLFORM(db[tablename], request.args(1, cast=int))
    return dict(form=form)

def teste():
    categorias = SQLFORM.grid(Categorias)
    return dict(categorias=categorias)