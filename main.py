#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	29/06/2019 23:00:28
#+ Editado:	29/06/2019 23:40:03
#------------------------------------------------------------------------------------------------
import gettext
import sys
# ---
import utiles as u
#------------------------------------------------------------------------------------------------
def auto(args):
    print('auto')

def manual():
    print('manual')
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
    # fai que colla o idioma por defecta da persoa de entre as traduccións que hai
    _ = gettext.gettext
	#en = gettext.translation('caderno-viaxe', localedir='locales', languages=['en'])
	#en.install()
	#_ = en.gettext

    #
    if len(sys.argv)>1:
        if sys.argv[1]=='-?':
            print(_("\nExecución: 'python3 ledo.py -c/-d [-e entrada] [-s saida] -p password'"))
            print(_(" -c = codificar"))
            print(_(" -d = descodificar"))
            print(_(" [-e fich] = [opcional] entrada.txt por defecto"))
            print(_(" [-s fich] = [opcional] saida.txt por defecto"))
            print(_(" -p contrasinal = contrasinal\n"))

        elif sys.argv[1]=='-h':
        	print(_("\nExecución: 'python3 ledo.py -c/-d [-e entrada] [-s saida] -p password'\n"))

        elif len(sys.argv)>3:
        	auto(sys.argv[1:])

        else:
        	print(_("Dame máis argumentos ou separa os que xa tes"))
    else:
        manual()
#------------------------------------------------------------------------------------------------
