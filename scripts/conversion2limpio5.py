#!/usr/bin/env python
import csv
#este programa elimina el campo ID crimen que no es usable, 
#tambien reemplaza el caracter ; por '' siempre y cuando se encuentre seguido de caracteres que sean ';\r\n'
#tambien reemplaza el caracter ; por , cuando este no termina en ';\r\n'

reader = csv.reader(open('todos-crimenes4.csv', 'rb'))
#print "Crime ID"," Month "," Reported by ","Falls within","Longitude","Latitude","Location","LSOA code","LSOA name","Crime type","Last outcome category","Context"
#omito la primera linea que es la cabecera
#salto=0
for index,row in enumerate(reader):
    #print 'Persona: ' + str(index + 1)
    #print '------------'
    row2=""
	#descarto que en el campo tipo de crimenes se encuentren ciudades tambien 	 
	locacion=row[6]
    #con .join creo el array como una cadena larga, la idea es eliminar las comillas dobles de las cadenas
    if '"' in locacion:
	    #limpiamos las comillas dobles de la columna que la tenga, pero dejamos la coma
	    locacion.replace('"', ' ')
	    row[6]=locacion
    if not (( 'Crime ID' in " ".join(row)) or ( 'Reported by' in " ".join(row))):
        #Crime ID lo transforme en String y se omite para evitar embasuramiento
        print  '{'+'"Month":'+'"'+row[1]+'"'+','+ '"Reported_by":'+'"'+row[2]+'"'+','+'"Falls_within":'+'"'+ row[3]+'"'+','+'"Longitude":'+ row[4]+','+'"Latitude":'+row[5]+','+'"Location":'+'"'+ row[6]+'"'+','+'"LSOA_code":'+'"'+row[7]+'"'+','+'"LSOA_name":'+'"'+row[8]+'"'+','+'"Crime_type":'+'"'+ row[9]+'"'+','+'"Last_outcome_category":'+'"'+row[10]+'"'+','+'"Context":'+'"'+row[11]+'"'+'}'
 
