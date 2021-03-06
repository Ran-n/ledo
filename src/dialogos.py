#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/08/2019 23:50:00
#+ Editado:	11/08/2019 16:17:03
#------------------------------------------------------------------------------------------------
# diálogo que pide que lle metas o tipo de operación a realizar, pasamoslle o couso do gettext
def k_operacion(_):
    '''
    @resumo = encargáse de mostrar un diálogo ao usuario e recoller a súa resposta só se é correcta,
    se non repite a pregunta.
    @entrada = o gettext to programa global.
    @saida = a variable local coa resposta.
    '''
    while True:
        op__ = input(_(' > Codificas(c) ou decodificas(d)?: '))
        #se a resposta está dentro as posibilidades saimos do bucle
        if op__ in ('c', 'd'):
            break
    return op__
#------------------------------------------------------------------------------------------------
# dialogo para preguntar ao usuario pola chave de cifrado ou descifrado
def k_chave(_):
    return input(_(' > Chave de cifrado: '))
#------------------------------------------------------------------------------------------------
# dialogo para indicar o texto a cifrar ou descifrar
def k_texto_codificar(_):
    return input(_(' > Texto a cifrar ou descifrar: '))
#------------------------------------------------------------------------------------------------
