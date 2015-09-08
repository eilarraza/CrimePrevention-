#!/usr/bin/env python
import csv

import os,sys
# -*- coding: utf-8
#Variable para la ruta al directorio
path = '/home/ubuntu/descargas/llevando_csv_to_json' 
#Lista vacia para incluir los archivos

#lista vacia para incluir directorio y archivo 

#Lista con todos los ficheros del directorio

#definiendo una funcion a llamar luego
def creandobigfile(nombreFusionar):
    
    #creo el mega archivo en el dir data-britanica-crimenes
    reader = csv.reader(open(nombreFusionar, 'rb'))
    f = open ("todos-crimenes3.csv", "a")
    for index,row in enumerate(reader):
        #print str(row)
        #transformo vector de string en cadena y automatica elimino corchetes
        cad="".join(row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11])
        f.write(cad+'\n')

#Crea una lista de los ficheros csv que existen en el directorio y los incluye a la lista.

nombreFichero="2015-05-btp-street.csv"

#print "longitud de la lista = ", len(lstFiles)
#paso la lista con ruta completa de directorios con sus archivos
#for item in lstFiles2:
creandobigfile(nombreFichero)

#fin
