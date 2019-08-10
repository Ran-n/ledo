#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/08/2019 21:17:48
#+ Editado:	11/08/2019 01:23:57
#------------------------------------------------------------------------------------------------
import json
from pathlib import Path
#------------------------------------------------------------------------------------------------
# función encargada de cargar ficheiros tipo json coa extensión dada se se dá
def cargar_json(fich):
	if Path(fich).is_file():
		return json.loads(open(fich).read())
	else:
		open(fich, 'w').write('{}')
		return json.loads(open(fich).read())
#------------------------------------------------------------------------------------------------
# función de gardado de ficheiros tipo json coa extensión dada se se da
def gardar_json(fich, contido, sort=False):
	open(fich, 'w').write(json.dumps(contido, indent=1, sort_keys=sort, ensure_ascii=False))
#------------------------------------------------------------------------------------------------
# se exsite, carga o ficheiro e devolveo
def cargar_fich(fich, encoding='utf-8-sig'):
	# de non existir o ficheiro o que facemos e cargar os refráns de media pois modificamos a dirección de fich
	if not Path(fich).is_file():
		fich = '../media/refráns.txt'
	# abrimos unha conexión de lectura co ficheiro
	fich_conex = open(fich,"r", encoding=encoding)
	# lemos o que contén
	fich_contido = fich_conex.read()
	# e pechámolo
	fich_conex.close()
	# devolvemos o contido do ficheiro
	return fich_contido
#------------------------------------------------------------------------------------------------
# gardamos nun ficheiro o contido na variable contido
def gardar_fich(fich, contido, encoding='utf-8-sig'):
	saida = open(fich, "w", encoding=encoding).write(contido)
#------------------------------------------------------------------------------------------------
# se non existe, crea unha carpeta
def crear_carp(carp):
	if Path(carp).is_dir() == False:
		Path(carp).mkdir(parents=True, exist_ok=True)
#------------------------------------------------------------------------------------------------
# imprime un diccionario en modo bonito
def pJson(diccionario, sort=False):
	print(json.dumps(diccionario, indent=4, sort_keys=sort))
#------------------------------------------------------------------------------------------------
# función que devolve verdadeiro ou falso dependendo de se a entrada está dentro
# das respostas positivas ou negativas válidas e verdadeiro ou falso para o tipo
# de resposta que deu nun principio si verdadeiro non falso
def snValido(resposta):
	sis = ('si', 's', 'yes', 'y')
	nons = ('non', 'no', 'n')

	if resposta in sis:
		# valido e resposta
		return True, True
	# non poñer nada conta como dicir non
	elif resposta in nons or resposta == '':
		return True, False
	else:
		return False, False
#------------------------------------------------------------------------------------------------
# función para ler o ficheiro de configuración e devolver as variables adecuadas
def read_config(abc, maiusculas, raiz, lang, entradax, saidax, fentrada, fsaida, carac_saida):
    texto_config = '''### FICHEIRO DE CONFIGURACIÓN ###
## Non cambiar a parte esquerda do igual ou producirase un erro.
## Borrar o ficheiro para restablecer valores orixinais.
### CONFIGURATION FILE ###
## Do not change the left part of the equality sign or an error will occur.
## Remove the file to set the original values back.

# Variable que se encarga de indicar as letras que serán usadas para encriptar e desencriptar.
# se unha letra non está e métese no texto a encriptar será eliminada do texto e encriptarase só cas que estén no abc.
# Variable to set the letters that will be used to encrypt and decrypt.
# if a letter is not in this variable and appears on the text it will be removed at encryption/decryption time.
'''+abc+''' = abcdefghijklmnñopqrstuvwxyz

# Indica se queres que se fagan minúsculas as maiúsculas do texto de entrada.
# Para conservalas como maiúsculas: "si", "s", "yes", "y".
# Para facelas minúsculas: "non", "no", "n".
# Tells the program if you want to make the upper case letters in the text into lower case.
# To keep them as upper case: "si", "s", "yes", "y".
# To convert them into lower case: "non", "no", "n".
'''+maiusculas+''' = s

# Directorio raiz.
# Root directory.
'''+raiz+''' = ..

# Indica o idioma dos diálogos.
# Idiomas permitidos: inglés (en), galego (gl), español (es).
# Sets the language for the dialogs.
# Allowed languages: english (en), gallician(gl), spanish (es).
'''+lang+''' = gl

# Indica se se colle o texto de entrada de ficheiro ou de entrada estándard.
# Para coller datos por ficheiro: "si", "s", "yes", "y".
# Para coller datos por pantalla: "non", "no", "n".
# Variable that indicates whether the text to encrypt/decrypt comes from a file or standard input (stdin).
# To get the text from a file: "si", "s", "yes", "y".
# To get the text from stdin: "non", "no", "n".
'''+entradax+''' = s

# indica se se mostra o texto de saida en ficheiro ou de saida estándard.
# Para sacar datos por ficheiro: "si", "s", "yes", "y".
# Para sacar datos por pantalla: "non", "no", "n".
# Variable that indicates whether the text to encrypt/decrypt goes to a file or standard output (stdout).
# To set the text to a file: "si", "s", "yes", "y".
# To set the text to stdout: "non", "no", "n".
'''+saidax+''' = s

# Nome do ficheiro de entrada de ser usado.
# Name of the input file if any.
'''+fentrada+''' = entrada.txt

# Nome do ficheiro de saida de ser usado.
# Name of the output file if any.
'''+fsaida+''' = saida.txt

# Caracter que indica a saída do programa.
# Character to indicate the exit of the program.
'''+carac_saida+''' = .
'''
    fich = '../.config'
    # se o ficheiro xa existe
    if Path(fich).is_file():
    	config = {}
    	'''
    	Lemos todas as liñas do ficheiro e quitamoslle os \n
    	De todas as liñas só nos quedamos coas que non comezan por un comentario
    	Das liñas de configuración o que facemos e separalas por igual e quedarnos
    	co segundo elemento de valor e o primeiro de clave, co cal a orde dos elementos pode ser alterada.
    	Poderíase facer que mirase o nome da variable pero da pereza e non ten
    	sentido e mentres non a cambien non importa.
    	Facemos que o da esquerda da variable sexa a clave do diccionario e o da dereita o valor.
    	'''
    	for x in open(fich):
    		''' facemos isto porque debe ser máis eficiente ca facer senón strip
    		cada vez que chamemos a x'''
    		x = x.strip()
    		if not x.startswith('#') and x != '':
    			config[x.split('=')[0].strip()] = x.split('=')[1].strip()
    	return config
    # se non existe o que facemos e crealo cos valores por defecto postos na variable e recargar a operacion
    else:
    	open(fich, 'w').write(texto_config)
    	return read_config(abc, maiusculas, raiz, lang, entradax, saidax, fentrada, fsaida, carac_saida)
#------------------------------------------------------------------------------------------------
# recibindo un array con letras e un abecedario vai substituindo cada letra pola súa posición no abecedario
def letra2num(letras, abc):
	"""
	Recibe un lista de letras e devolve unha de posicións das letras dentro do abecedario.
	> letras: lista das letras das que queremos obter o valor da posición dentro do abecedario
	> abc: lista de letras dentro do abecedario
	< lista cos valores posicionais das letras no alfabeto
	"""
	# con un bucle vamos recorrendo as letras e as que estén no abecedario metémos a súa posición nun array que devolvemos
	return [abc.index(elto) for elto in letras if elto in abc]
#------------------------------------------------------------------------------------------------
# recibe un array de números e substitueos polas letras correspondentes ás posicións dos mesmos
def num2letra(numaros, abc):
	"""
	Recibe un lista de números e devolve unha cos valores desas posicións dentro do abecedario.
	> numaros: lista cos números que usaremos para obter os valores dentro do abecedario
	> abc: lista de letras dentro do abecedario
	< lista cas letras correspondentes as posicións dadas polos números
	"""
	# non miramos que sexa menor cá lonxitude total do abecedario porque non debería darse
	# a posibilidade pois non é posible que o usuario toque nada entre as operacións de tradución
	return [abc[ele] for ele in numaros]
#------------------------------------------------------------------------------------------------
