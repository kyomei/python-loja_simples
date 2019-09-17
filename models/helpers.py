# -*- coding: utf-8 -*-

def format_decimal(value):
    """Formata decimal e coloca separador de milhar."""
    return 'R$ {:20,.2f}'.format(value).replace(',', '|').replace('.', ',').replace('|', '.')