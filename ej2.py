#!/usr/bin/python3
# -*- coding: utf-8 -*-

fichero = open('/etc/passwd', 'r')

lineas = fichero.readlines()

for linea in lineas:
    elems = linea.split(':')
    print(elems[0], '-->', elems[-1][:-1])
#Otra manera print(linea[:linea.find(':')], '-->', linea[linea.rfind(':')+1:-1])
    

