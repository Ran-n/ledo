#!/usr/bin/python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	11/08/2019 15:33:43
#+ Editado:	11/08/2019 16:17:15
#------------------------------------------------------------------------------------------------
import utils as u
#------------------------------------------------------------------------------------------------
class traductora:
    # clase constructora, pasamoslle o idioma que usaremos para discernir os strings
    def __init__(self, lang):
        self.lang = lang
        self.en = u.cargar_json('../media/traducs/en')
        self.es =u.cargar_json('../media/traducs/es')

    def traducir(self, string):
        if self.lang == 'gl':
            return string
        elif self.lang == 'en':
            return self.en[string]
        elif self.lang == 'es':
            return self.es[string]
        else:
            print('*> Idioma Errado\n*> Wrong language\n*> Idioma equivocado')
            exit()
#------------------------------------------------------------------------------------------------
