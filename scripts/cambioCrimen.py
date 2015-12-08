#!/usr/bin/env python
import csv
from os import listdir
from os import walk
import os,sys
from datetime import datetime, date, time, timedelta
import calendar
# -*- coding: utf-8
#Variable para la ruta al directorio
path = 'todos-crimenes6.json' 
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
    #reader = csv.reader(Acsv)
    #reader = (Acsv)
    f = open ("todos-crimenes-tipo.json", "w")
    linea=Acsv.readline()
    while linea!="":   
        linea=Acsv.readline()
             #print str(row)
        if("Anti-social behaviour" in linea):
            linea=linea.replace('"Anti-social behaviour"', '1')
        if("Bicycle theft" in linea):
            linea=linea.replace('"Bicycle theft"', '2')
        if("Burglary" in linea):
            linea=linea.replace('"Burglary"', '3')
        if("Criminal damage and arson" in linea):
            linea=linea.replace('"Criminal damage and arson"', '4')
        if("Drugs" in linea):
            linea=linea.replace('"Drugs"', '5')
        if("Other crime" in linea):
            linea=linea.replace('"Other crime"', '6')
        if("Other theft" in linea):
            linea=linea.replace('"Other theft"', '7')
        if("Possession of weapons" in linea):
            linea=linea.replace('"Possession of weapons"', '8')
        if("Public disorder and weapons" in linea):
            linea=linea.replace('"Public disorder and weapons"', '9')
        if("Public order" in linea):
            linea=linea.replace('"Public order"', '10')
        if("Robbery" in linea):
            linea=linea.replace('"Robbery"', '11')
        if("Shoplifting" in linea):
            linea=linea.replace('"Shoplifting"', '12')
        if("Theft from the person" in linea):
            linea=linea.replace('"Theft from the person"', '13')
        if("Vehicle crime" in linea):
            linea=linea.replace('"Vehicle crime"', '14')     
        if("Violence and sexual offences" in linea):
            linea=linea.replace('"Violence and sexual offences"', '15')  
        if("Violent crime" in linea):
            linea=linea.replace('"Violent crime"', '16')

        #transformo vector de string en cadena y automatica elimino corchetes
        #cad=",".join(row)
        
        f.write(linea)
        linea=Acsv.readline()

    #cerrar el del csv
    Acsv.close()
    #cerrar el que escribe f
    f.close()
    
    b = datetime.now()
    delta = b - a
    print 'Tiempo Proceso: '+str(delta.seconds)+ ' segundos'


creandobigfile(path)
