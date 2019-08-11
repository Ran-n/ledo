#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	29/06/2019 23:00:28
#+ Editado:	11/08/2019 17:35:15
#------------------------------------------------------------------------------------------------
import utils as u
import dialogos as dg
import codificar as c
import decodificar as dc
import traduccions as t
#-----------------------
import gettext
import sys
#------------------------------------------------------------------------------------------------
def manual():
    # facemos que se repita todo até que explicitamente se diga de sair
    while True:
        print('\n')
        # se na config pon que si se lea dun ficheiro
        if u.snValido(__config[__str_entradax]) == (True, True):
            # o texto a codificar ou decodificar probén do ficheiro de entrada
            texto__ = u.cargar_fich(__config[__str_fentrada])
        else:
            texto__ = dg.k_texto_codificar(_)

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

        # se na config poñen que si se garde nun ficheiro
        if u.snValido(__config[__str_saidax]) == (True, True):
            # garda no ficheiro de saida o resultado
            u.gardar_fich(__config[__str_fsaida], resultado__)
        else:
            print(_('*> Resultado:\t'), resultado__)

        # se o usuario presiona o caracter de saida cortamos o bucle
        if input(_('\n*> Presiona {} se queres sair do programa: ').format(__config[__str_carac_saida])) == __config[__str_carac_saida]:
            break
#------------------------------------------------------------------------------------------------
def auto(args):
    # se na config pon que si se lea dun ficheiro
    if u.snValido(__config[__str_entradax]) == (True, True):
        # o texto a codificar ou decodificar probén do ficheiro de entrada
        texto__ = u.cargar_fich(__config[__str_fentrada])
    elif '-e' in args:
        texto__ = args[args.index('-e')+1]
    elif '-i' in args:
        texto__ = sys.stdin.read()
    else:
        exit()

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
        else:
            exit()

        # se na config poñen que si se garde nun ficheiro
        if u.snValido(__config[__str_saidax]) == (True, True):
            # garda no ficheiro de saida o resultado
            u.gardar_fich(__config[__str_fsaida], resultado__)
        else:
            print(resultado__)
    else:
        exit()
#------------------------------------------------------------------------------------------------
# función que se encarga de chamar ao obxecto de traducción
def _(string):
    return traduccions.traducir(string)
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
    '''
    Contidos da variable diccionario __config
    abc         -> abecedario
    maiusculas  -> determina se se cambian as maiúsculas por minúsculas no texto de entrada
    raiz        -> carpeta raiz para ler e crear arquivos
    lang        -> indica o idioma de saida na versión con diálogos
    entradax    -> determina se a entrada e por ficheiro ou stdin
    saidax      -> determina se a saida e por ficheiro ou stdout
    fentrada    -> ficheiro de entrada
    fsaida      -> ficheiro de saida
    carac_saida -> caracter de saida
    '''
    __str_abc = 'abc'
    __str_maiusculas = 'maiusculas'
    __str_raiz = 'raiz'
    __str_lang = 'lang'
    __str_entradax = 'entrada_x_fich'
    __str_saidax = 'saida_x_fich'
    __str_fentrada = 'fentrada'
    __str_fsaida = 'fsaida'
    __str_carac_saida = 'carac_saida'
    # lemos o ficheiro de configuración e sacamos os valores a un diccionario
    __config = u.read_config(__str_abc, __str_maiusculas, __str_raiz, __str_lang, __str_entradax, __str_saidax, __str_fentrada, __str_fsaida, __str_carac_saida)
    # aseguramonos de que o ficheiro teña ben posto o nome ao estar coa raiz antes
    __config[__str_abc] = u.especiais_abc(list(__config[__str_abc]))
    __config[__str_fentrada] = __config[__str_raiz] +'/'+ __config[__str_fentrada]
    __config[__str_fsaida] = __config[__str_raiz] +'/'+ __config[__str_fsaida]

    # creamos a instancia da clase que se encargará de traducir os strings
    traduccions = t.traductora(__config[__str_lang])

    # parte lóxica que se encarga de mandar á función de manual ou automatico
    if len(sys.argv)>1:
        if sys.argv[1]=='-?':
            print(_("\nExecución: 'python3 main.py -c/-d -p contrasinal [-e texto_entrada] [-i]'"))
            print(_(' -c = codificar'))
            print(_(' -d = descodificar'))
            print(_(' -e texto_entrada = texto a codificar ou decodificar'))
            print(_(' -p contrasinal = contrasinal\n'))

        elif sys.argv[1]=='-h':
        	print(_("\nExecución: 'python3 main.py -c/-d -p contrasinal [-e texto_entrada] [-i]'\n"))

        elif len(sys.argv)>3:
        	auto(sys.argv[1:])

        else:
        	print(_('Dame máis argumentos ou separa os que xa tes.'))
    else:
        manual()
#------------------------------------------------------------------------------------------------
