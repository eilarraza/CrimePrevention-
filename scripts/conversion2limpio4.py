#!/usr/bin/env python
import csv
#este programa elimina el campo ID crimen que no es usable, 
#tambien reemplaza el caracter ; por '' siempre y cuando se encuentre seguido de caracteres que sean ';\r\n'
#tambien reemplaza el caracter ; por , cuando este no termina en ';\r\n'

reader = csv.reader(open('todos-crimenes3.csv', 'rb'))
#print "Crime ID"," Month "," Reported by ","Falls within","Longitude","Latitude","Location","LSOA code","LSOA name","Crime type","Last outcome category","Context"
#omito la primera linea que es la cabecera
#salto=0
for index,row in enumerate(reader):
    #print 'Persona: ' + str(index + 1)
    #print '------------'
    #con .join creo el array como una cadena larga
        row2=""
    if not (( 'Crime ID' in " ".join(row)) or ( 'Reported by' in " ".join(row))):
        #reemplazo ;\r\n con \r\n
        if (';\r\n' in " ".join(row)):
            #para guardar en row debe ser iterada desde row2 por medio de un split
            #reuno todo el vector en un string pero separados por ,
            row2 =",".join(row).replace(';\r\n', '\r\n')
            #convierto toda la cadena ahora a vector rompiendolo por la ,
            row=row2.split(',')
        if  ( ';' in " ".join(row)):
            #para guardar en row debe ser iterada desde row2 por medio de un split
            #reuno todo el vector en un string pero separados por ,
            row2=",".join(row).replace(';', ',')
            row=row2.split(',')
        #Crime ID lo transforme en String y se omite para evitar embasuramiento
        print  '{'+'"Month":'+'"'+row[1]+'"'+','+ '"Reported_by":'+'"'+row[2]+'"'+','+'"Falls_withi$
        print '\n'
        #if index >100:
        #   break

