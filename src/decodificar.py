#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2019 23:33:38
#+ Editado:	10/08/2019 17:27:11
#------------------------------------------------------------------------------------------------
import utils as u
#------------------------------------------------------------------------------------------------
class decodificar:
    # función inicial que recolle as variables pasadas e as pon dentro do obxecto
    # todas as variables son strings
    def __init__(self, chave_ini, texto_ini, abc):
        self.__abc = list(abc)
        self.__texto_ini = [ele for ele in list(texto_ini) if ele in self.__abc]
        #collemos o valor da lonxitude do texto en plano
        self.__lonxitude_texto = len(self.__texto_ini)
        # cortámola á lonxitude do texto por se nos pon unha chave moi longa
        self.__chave_ini = [ele for ele in list(chave_ini) if ele in self.__abc][:self.__lonxitude_texto]
        #definimos e inicializamos a lonxitude da lista a devolver
        self.__autochave = None
        self.__texto_decodificado = None
#------------------------------------------------------------------------------------------------
    def __decodificacion(self):
        # restamos o texto e a chave, unha vez temos esta primeira resta usamos os resultados
        # para seguir restando ata que o texto remate
        self.__resta_automatica_modulada()
        # desfacemos a transposición
        self.__transposicion_monarquica()
#------------------------------------------------------------------------------------------------
    # vai restando os valores da clave aos do texto
    # como a clave e máis pequecha co texto vai collendo o resultado como
    # entrada para restar os seguintes valores, e así até que sexan de igual lonxitude
    def __resta_automatica_modulada(self):
        self.__texto_decodificado = u.letra2num(self.__texto_ini, self.__abc)
        self.__autochave = u.letra2num(self.__chave_ini, self.__abc)

        # forma antiga e menos eficiente de facelo
        '''
        chave__ = list(self.__autochave)

        # mentres a chave sexa mais pequena co texto continuamos restando
        while True:
            # facemos a resta e o módulo
            resta__ = [x%len(self.__abc) for x in [y-z for y,z in zip(self.__texto_decodificado, self.__autochave)]]

            # se a clave é mais pequecha debemos seguir iterando
            if len(self.__autochave) < self.__lonxitude_texto:
                # sumamos os números obtidos á chave INICIAL para restar outra vez o novo vector
                self.__autochave = (chave__ + resta__)[:self.__lonxitude_texto]
            else:
                # o resultado da resta son os números das letras do texto orixinal
                # collemos e pasámolos á letras
                self.__texto_decodificado = u.num2letra(resta__, self.__abc)
                break
        '''
        # facemos a primera resta e metemos o resultado na chave final
        self.__autochave = [x%len(self.__abc) for x in [y-z for y,z in zip(self.__texto_decodificado, self.__autochave)]]

        lonx_chave__ = len(self.__autochave)
        ''' se a autochave non é tan grande como o texto procedemos a restar
         vamos collendo do inicio da chave número a número e restandoo co primeiro non restado do texto na vez anterior
         ata que a lonxitude de clave e texto sexa a mesma.
         Poñemos esta comprobación aqui para non entrar no bucle se non é preciso'''
        if  lonx_chave__< self.__lonxitude_texto:
            # para cada elemento da chave facemos a resta se a lonxitude non é a adecuada
            for index, elto in enumerate(self.__autochave):
                    if lonx_chave__+index<self.__lonxitude_texto:
                        ''' facemos a resta do elemento co seu correspondente módulo e
                        engadímolo á autochave para que continue ata a lonxitude do texto'''
                        self.__autochave.append(((self.__texto_decodificado[lonx_chave__+index] - elto)%len(self.__abc)))
        # devolvemos o resultado como letra
        self.__texto_decodificado = u.num2letra(self.__autochave, self.__abc)
#------------------------------------------------------------------------------------------------
    # transposición que desfai á da codificación ou republicana
    def __transposicion_monarquica(self):
        inicial = [] #* int(len(texto_trasposto)/2)
        final = [] #* int(len(texto_trasposto)/2)
        for index, ele in enumerate(self.__texto_decodificado):
            #impar
            if index%2 != 0:
                # extend só é interesante se queremos facer un append inclusivo de listas
                inicial.append(ele)
            #par
            else:
                final.append(ele)

        #o [::-1] e como poñerlle .reverse()
        self.__texto_decodificado = ''.join(inicial + final[::-1])
#------------------------------------------------------------------------------------------------
    # función que chama á operación de codificación e devolve o texto codificado
    def get_texto_decodificado(self):
        self.__decodificacion()
        return self.__texto_decodificado
#------------------------------------------------------------------------------------------------
