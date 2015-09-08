#!/usr/bin/env python
import csv

reader = csv.reader(open('todos-crimenes.csv', 'rb'))
#print "Crime ID"," Month "," Reported by ","Falls within","Longitude","Latitude","Location","LSOA code","LSOA name","Crime type","Last outcome category","Context"
#omito la primera linea que es la cabecera
#salto=0
for index,row in enumerate(reader):
    #print 'Persona: ' + str(index + 1)
    #print '------------'
    #con .join creo el array como una cadena larga
    if not (( 'Crime ID' in " ".join(row)) or ( 'Reported by' in " ".join(row))) :
        #Crime ID lo transforme en String para evitar embasuramiento
        print  '{'+'"Month":'+'"'+row[1]+'"'+','+ '"Reported by":'+'"'+row[2]+'"'+','+'"Falls within":'+'"'+ row[3]+'"'+','+'"Longitude":'+ row[4]+','+'"Latitude":'+row[5]+','+'"Location":'+'"'+ row[6]+'"'+','+'"LSOA code":'+'"'+row[7]+'"'+','+'"LSOA name":'+'"'+row[8]+'"'+','+'"Crime type":'+'"'+ row[9]+'"'+','+'"Last outcome category":'+'"'+row[10]+'"'+','+'"Context":'+'"'+row[11]+'"'+'}'
        print '\n'
   
    #if index > 2:
    #    break
    



