#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2019 21:27:20
#+ Editado:	09/08/2019 16:45:21
#------------------------------------------------------------------------------------------------
import utils as u
#------------------------------------------------------------------------------------------------
class codificar:
    # función inicial que recolle as variables pasadas e as pon dentro do obxecto
    # todas as variables son strings
    def __init__(self, chave_ini, texto_ini, abc):
        self.__abc = list(abc)
        self.__chave_ini = [ele for ele in list(chave_ini) if ele in self.__abc]
        self.__texto_ini = [ele for ele in list(texto_ini) if ele in self.__abc]
        #collemos o valor da lonxitude do texto en plano
        self.__lonxitude_texto = len(self.__texto_ini)
        #definimos e inicializamos a lonxitude da lista a devolver
        self.__texto_trasposto = [None] * len(self.__texto_ini)
        self.__autochave = None
        self.__texto_codificado = None

        self.codificacion()

        #print(self.__texto_trasposto)
#------------------------------------------------------------------------------------------------
    # función que se encarga de realizar todos os pasos individuais e inaccsibles dende fora da codificación
    def codificacion(self):
        # primeiro facemos a transposición, o cal neste caso é a republicana
        self.__transposicion_republicana()
        # utilizando os caracteres transpostos crease a autoclave do estilo da de vigenere
        # pasase a chave e o texto transposto aos seus valores numéricos

        # obtemos os números da mensaxe codificada facendo a suma de chave e texto transposto
        # pasamos eses números a caracteres dentro do abecedario e retornamos o valor
#------------------------------------------------------------------------------------------------
    '''Move as letras do principio co final e colocaas primeiro a última e logo a primeira
    Por exemplo:
    indixena
    ainnedxi'''
    def __transposicion_republicana(self):
        #creamos outra lista co mesmo valor ca inicial pero cos valores revertidos
        caracs_contrario = list(self.__texto_ini)
        caracs_contrario.reverse()
        metade__ = int(self.__lonxitude_texto/2)

        # lonxitude impar
        if (self.__lonxitude_texto%2 != 0):
            #agora esas listas incial e revertida truncámolas á metade dos caracteres
            ini = list(self.__texto_ini[:metade__])
            #á final engadímoslle a do medio
            fin = list(caracs_contrario[:metade__+1])

        # lonxitude par
        else:
            #agora esas listas incial e revertida truncámolas á metade dos caracteres
            ini = list(self.__texto_ini[:metade__])
            fin = list(caracs_contrario[:metade__])

        self.__texto_trasposto[::2] = fin
        self.__texto_trasposto[1::2] = ini
#------------------------------------------------------------------------------------------------
def __crear_autoclave(self):
    
#------------------------------------------------------------------------------------------------
