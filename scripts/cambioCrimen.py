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
 
             #print str(row)
        if('\"Crime_type\"'+':'+'"Anti-social behaviour"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Anti-social behaviour"', '\"Crime_type\"'+':'+'1') 
        if('\"Crime_type\"'+':'+'"Bicycle theft"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Bicycle theft"', '\"Crime_type\"'+':'+'2')
        if('\"Crime_type\"'+':'+'"Burglary"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Burglary"', '\"Crime_type\"'+':'+'3')
        if('\"Crime_type\"'+':'+'"Criminal damage and arson"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Criminal damage and arson"', '\"Crime_type\"'+':'+'4')
        if('\"Crime_type\"'+':'+'"Drugs"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Drugs"', '\"Crime_type\"'+':'+'5')
        if('\"Crime_type\"'+':'+'"Other crime"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Other crime"', '\"Crime_type\"'+':'+'6')
        if('\"Crime_type\"'+':'+'"Other theft"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Other theft"', '\"Crime_type\"'+':'+'7')
        if('\"Crime_type\"'+':'+'"Possession of weapons"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Possession of weapons"', '\"Crime_type\"'+':'+'8')
        if('\"Crime_type\"'+':'+'"Public disorder and weapons"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Public disorder and weapons"', '\"Crime_type\"'+':'+'9')
        if('\"Crime_type\"'+':'+'"Public order"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Public order"', '\"Crime_type\"'+':'+'10')
        if('\"Crime_type\"'+':'+'"Robbery"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Robbery"', '\"Crime_type\"'+':'+'11')
        if('\"Crime_type\"'+':'+'"Shoplifting"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Shoplifting"', '\"Crime_type\"'+':'+'12')
        if('\"Crime_type\"'+':'+'"Theft from the person"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Theft from the person"', '\"Crime_type\"'+':'+'13')
        if('\"Crime_type\"'+':'+'"Vehicle crime"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Vehicle crime"', '\"Crime_type\"'+':'+'14')
        if('\"Crime_type\"'+':'+'"Violence and sexual offences"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Violence and sexual offences"', '\"Crime_type\"'+':'+'15')
        if('\"Crime_type\"'+':'+'"Violent crime"' in linea):
            linea=linea.replace('\"Crime_type\"'+':'+'"Violent crime"' , '\"Crime_type\"'+':'+'16')


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
