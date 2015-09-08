#!/usr/bin/env python
import csv
from os import listdir
from os import walk
import os,sys
from datetime import datetime, date, time, timedelta
import calendar
# -*- coding: utf-8
#Variable para la ruta al directorio
path = '/s3mnt3/procesed/' 
#Lista vacia para incluir los archivos
lstFiles = []
#lista vacia para incluir directorio y archivo 
lstFiles2 = []
#Lista con todos los ficheros del directorio
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
#definiendo una funcion a llamar luego
def creandobigfile(nombreFusionar):
    a = datetime.now()
    print 'anadiendo: '+nombreFusionar 
    #creo el mega archivo en el dir data-britanica-crimenes
    Acsv=open(nombreFusionar, 'rb')
    reader = csv.reader(Acsv)
    f = open ("todos-crimenes2.csv", "a")
    for index,row in enumerate(reader):
        #print str(row)
        #transformo vector de string en cadena y automatica elimino corchetes
        cad=",".join(row)
        f.write(cad+'\n')
    
    #cerrar el del csv
    Acsv.close()
    #cerrar el que escribe f
    f.close()
    
    b = datetime.now()
    delta = b - a
    print 'Tiempo Proceso: '+str(delta.seconds)+ ' segundos'

#Crea una lista de los ficheros csv que existen en el directorio y los incluye a la lista.
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".csv"):
            lstFiles.append(nombreFichero+extension)
            lstFiles2.append(root+'/'+nombreFichero+extension)
         
print 'Archivos a fusionar en uno solo:' 
for item in lstFiles:
    print item
               
print ('LISTADO FINALIZADO')
print "longitud de la lista = ", len(lstFiles)
#paso la lista con ruta completa de directorios con sus archivos
for item in lstFiles2:
    creandobigfile(item)

#fin
