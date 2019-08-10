#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	29/06/2019 23:00:28
#+ Editado:	10/08/2019 13:31:50
#------------------------------------------------------------------------------------------------
import utils as u
import dialogos as dg
import codificar as c
import decodificar as dc
#-----------------------
import gettext
import sys
#------------------------------------------------------------------------------------------------
def manual():
    # o texto a codificar ou decodificar probén do ficheiro de entrada
    texto__ = u.cargar_fich(__config[__str_fentrada])
    # facemos que se repita todo até que explicitamente se diga de sair
    while True:
        # se non é c só pode ser d
        if dg.k_operacion(_) == 'c':
            # se nos dixeron maiúsculas non facemos todo o texto minúsculo
            # se non continuamos tal cal
            if u.snValido(__config[__str_maiusculas]) == (True, False):
                texto__ = texto__.lower()

            # metemos a chave, contido do ficheiro e abecedario para a codificación
            cod = c.codificar(dg.k_chave(_), texto__, __config[__str_abc])
            resultado__ = cod.get_texto_codificado()
        else:
            # pedimoslle a clave e metemola xunto co contido do ficheiro e abecedario para a codificación
            decod = dc.decodificar(dg.k_chave(_), texto__, __config[__str_abc])
            resultado__ = decod.get_texto_decodificado()

        # garda no ficheiro de saida o resultado
        u.gardar_fich(__config[__str_fsaida], resultado__)

        # se o usuario presiona o caracter de saida cortamos o bucle
        if input(_(' *> Presiona '+__config[__str_carac_saida]+' se queres sair: ')) == __config[__str_carac_saida]:
            break
#------------------------------------------------------------------------------------------------
def auto(args):
    # o texto a codificar ou decodificar probén do ficheiro de entrada
    texto__ = u.cargar_fich(__config[__str_fentrada])

    if '-p' in args:
        contrasinal = list(args[args.index('-p')+1])
        if '-c' in args:
            # se nos dixeron maiúsculas non facemos todo o texto minúsculo
            # se non continuamos tal cal
            if u.snValido(__config[__str_maiusculas]) == (True, False):
                texto__ = texto__.lower()

            # metemos a chave, contido do ficheiro e abecedario para a codificación
            cod = c.codificar(contrasinal, texto__, __config[__str_abc])
            resultado__ = cod.get_texto_codificado()

        elif '-d' in args:
            # pedimoslle a clave e metemola xunto co contido do ficheiro e abecedario para a codificación
            decod = dc.decodificar(contrasinal, texto__, __config[__str_abc])
            resultado__ = decod.get_texto_decodificado()

        # garda no ficheiro de saida o resultado, só se mete a opción da chave
        u.gardar_fich(__config[__str_fsaida], resultado__)
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
    # fai que colla o idioma por defecta da persoa de entre as traduccións que hai
    _ = gettext.gettext
	#en = gettext.translation('caderno-viaxe', localedir='locales', languages=['en'])
	#en.install()
	#_ = en.gettext

    '''
    Contidos da variable diccionario __config
    abc         -> abecedario
    raiz        -> carpeta raiz para ler e crear arquivos
    fentrada    -> ficheiro de entrada
    fsaida      -> ficheiro de saida
    carac_saida -> caracter de saida
    '''
    __str_abc = 'abc'
    __str_maiusculas = 'maiusculas'
    __str_raiz = 'raiz'
    __str_fentrada = 'fentrada'
    __str_fsaida = 'fsaida'
    __str_carac_saida = 'carac_saida'
    # lemos o ficheiro de configuración e sacamos os valores a un diccionario
    __config = u.read_config(__str_abc, __str_maiusculas, __str_raiz, __str_fentrada, __str_fsaida, __str_carac_saida)
    # aseguramonos de que o ficheiro teña ben posto o nome ao estar coa raiz antes
    __config[__str_fentrada] = __config[__str_raiz] +'/'+ __config[__str_fentrada]
    __config[__str_fsaida] = __config[__str_raiz] +'/'+ __config[__str_fsaida]

    # parte lóxica que se encarga de mandar á función de manual ou automatico
    if len(sys.argv)>1:
        if sys.argv[1]=='-?':
            print(_("\nExecución: 'python3 main.py -c/-d -p password'"))
            print(_(" -c = codificar"))
            print(_(" -d = descodificar"))
            print(_(" -p contrasinal = contrasinal\n"))

        elif sys.argv[1]=='-h':
        	print(_("\nExecución: 'python3 main.py -c/-d -p password'\n"))

        elif len(sys.argv)>3:
        	auto(sys.argv[1:])

        else:
        	print(_("Dame máis argumentos ou separa os que xa tes"))
    else:
        manual()
#------------------------------------------------------------------------------------------------
