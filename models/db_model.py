# -*- coding: utf-8 -*-


# requires=IS_NOT_EMPTY()                -> Deixa o campo como obrigatório
# format='%(nome)s'                      -> Exibe nome da categoria invés do id no formulário de produtos

Categorias = db.define_table('categorias',
     Field('nome', 'string', label='Categoria', requires=IS_NOT_EMPTY()), format='%(nome)s'
)
Produtos = db.define_table('produtos',
    Field('categoria_id', 'reference categorias', label='Categoria'), # Exibe id da categoria
    Field('nome', 'string', requires=IS_NOT_EMPTY()),
    Field('imagem', 'upload'),
    Field('preco'),
    Field('quantidade', 'integer'),
    Field('descricao', 'text', label='Descrição')
)
Pagamentos = db.define_table('pagamentos',
     Field('nome', requires=IS_NOT_EMPTY())
   # Field('nome', 'string', label='Pagamento', requires=IS_NOT_EMPTY()), format='%(nome)s'
)
Vendas = db.define_table('vendas',
    Field('usuario_id', 'reference auth_user', label='Usuario'),
    Field('produto_id', 'reference produtos', label='Produto'),
    Field('quantidade', 'integer'),
    Field('endereco', 'string'),
    Field('data_venda', 'datetime', label=T('Data da Venda')),
    Field('valor'),
    Field('pagamento_id', db.pagamentos, label='Forma de pagamento', requires=IS_IN_DB(db, 'pagamentos.id', '%(nome)s'))
   # Field('pagamento_id', 'reference pagamentos', label='Forma de pagamento')
)

