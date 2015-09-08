#!/usr/bin/env python
import csv

reader = csv.reader(open('files_incoming/2015-05-btp-street.csv', 'rb'))
print "Crime ID"," Month "," Reported by ","Falls within","Longitude","Latitude","Location","LSOA code","LSOA name","Crime type","Last outcome category","Context"
for index,row in enumerate(reader):
    #print 'Persona: ' + str(index + 1)
    #print '------------'
    print  '{'+'"Crime ID":'+row[0] +','+'"Month":'+ row[1] +','+ '"Reported by":'+'"'+row[2]+'"'+','+'"Falls within":'+'"'+ row[3]+'"'+','+'"Longitude":'+ row[4]+','+'"Latitude":'+'"'+row[5]+'"'+','+'"Location":'+ row[6]+','+'"LSOA code":'+'"'+row[7]+'"'+','+'"LSOA name":'+'"'+row[8]+'"'+','+'"Crime type":'+'"'+ row[9]+'"'+','+'"Last outcome category":'+'"'+row[10]+'"'+','+'"Context":'+'"'+row[11]+'"'+'}'
    print '\n'

