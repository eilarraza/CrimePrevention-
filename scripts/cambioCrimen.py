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
    f = open ("todos-crimenes-tipo.csv", "w")
    for index,row in enumerate(reader):
        #print str(row)
		if("Anti-social behaviour" in row[9]):
		    row[9]=1
		if("Bicycle theft" in row[9]):
		    row[9]=2
		if("Burglary" in row[9]):
		    row[9]=3
		if("Criminal damage and arson" in row[9]):
		    row[9]=4
		if("Drugs" in row[9]):
		    row[9]=5
		if("Other crime" in row[9]):
		    row[9]=6
		if("Other theft" in row[9]):
		    row[9]=7
        if("Possession of weapons" in row[9]):
		    row[9]=8 
        if("Public disorder and weapons" in row[9]):
		    row[9]=9
        if("Public order" in row[9]):
		    row[9]=10
        if("Robbery" in row[9]):
		    row[9]=11
        if("Shoplifting" in row[9]):
		    row[9]=12
        if("Theft from the person" in row[9]):
		    row[9]=13
        if("Vehicle crime" in row[9]):
		    row[9]=14
        if("Violence and sexual offences" in row[9]):
		    row[9]=15
        if("Violent crime" in row[9]):
		    row[9]=16
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
