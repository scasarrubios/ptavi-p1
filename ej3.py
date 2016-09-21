#!/usr/bin/python3
# -*- coding: utf-8 -*-

fichero = open('/etc/passwd', 'r')

lineas = fichero.readlines()

datos = {}

for linea in lineas:
    elems = linea.split(':')
    datos[elems[0]] = elems[-1][:-1]

busquedas = ['imaginario', 'root']

for user in busquedas:
    try:    
        print(user, '-->', datos[user])

    except KeyError:   
        print('Usuario no encontrado')

