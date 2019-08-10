#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2019 21:27:20
#+ Editado:	10/08/2019 01:23:08
#------------------------------------------------------------------------------------------------
import utils as u
#------------------------------------------------------------------------------------------------
class codificar:
    # función inicial que recolle as variables pasadas e as pon dentro do obxecto
    # todas as variables son strings
    def __init__(self, chave_ini, texto_ini, abc):
        self.__abc = list(abc)
        # aqui non é preciso cortar pois xa se corta ao facer a función autochave
        self.__chave_ini = [ele for ele in list(chave_ini) if ele in self.__abc]
        self.__texto_ini = [ele for ele in list(texto_ini) if ele in self.__abc]
        #collemos o valor da lonxitude do texto en plano
        self.__lonxitude_texto = len(self.__texto_ini)
        #definimos e inicializamos a lonxitude da lista a devolver
        self.__texto_transposto = [None] * len(self.__texto_ini)
        self.__autochave = None
        self.__texto_codificado = None
#------------------------------------------------------------------------------------------------
    # función que se encarga de realizar todos os pasos individuais e inaccsibles dende fora da codificación
    def __codificacion(self):
        # primeiro facemos a transposición, o cal neste caso é a republicana
        self.__transposicion_republicana()
        # utilizando os caracteres transpostos crease a autochave do estilo da de vigenere
        self.__crear_autochave()

        # pasase a chave e o texto transposto aos seus valores numéricos
        # obtemos os números da mensaxe codificada facendo a suma de chave e texto transposto
        self.__suma_modulada()

        # pasamos eses números a caracteres dentro do abecedario e retornamos o valor como un string
        self.__texto_codificado = ''.join(u.num2letra(self.__texto_codificado, self.__abc))
#------------------------------------------------------------------------------------------------
    '''Move as letras do principio co final e colocaas primeiro a última e logo a primeira
    Por exemplo:
    indixena
    ainnedxi'''
    def __transposicion_republicana(self):
        #creamos outra lista co mesmo valor ca inicial pero cos valores revertidos
        caracs_contrario = list(self.__texto_ini)
        caracs_contrario.reverse()
        # número que indica o valor do medio da lonxitude do texto
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

        # vamos poñendo na lista final os da parte fina de 2 en dous comezando na posición 0
        self.__texto_transposto[::2] = fin
        # e os da parte inicial de 2 en 2 dende a posición 1
        self.__texto_transposto[1::2] = ini
#------------------------------------------------------------------------------------------------
    # función que collendo a chave engadelle o texto transposto ata que a chave resultante teña a mesma lonxitude ca o texto
    def __crear_autochave(self):
        self.__autochave = list(self.__chave_ini+self.__texto_transposto)[:self.__lonxitude_texto]
#------------------------------------------------------------------------------------------------
    # operación que se encarga de sumar os dous valores de entrada e devolver un número de resultado dentro da lónxitude do abc
    def __suma_modulada(self):
        #facemola suma
        #facemos o módulo
        self.__texto_codificado = [x%len(self.__abc) for x in [y+z for y,z in zip(u.letra2num(self.__texto_transposto, self.__abc), u.letra2num(self.__autochave, self.__abc))]]
#------------------------------------------------------------------------------------------------
    # función que chama á operación de codificación e devolve o texto codificado
    def get_texto_codificado(self):
        self.__codificacion()
        return self.__texto_codificado
#------------------------------------------------------------------------------------------------
