#unionMasiva.py:
#recorre recursivamente  el directorio raiz, en busca de archivos
# con extension .csv y los lee registro a registro y los coloca
#en un archivo nuevo llamado todos-crimenes.csv
python unionMasiva.py
#conversion2limpio.py:
#lleva el archivo todos-crimenes.csv a todos-crimenes.json
python conversion2limpio.py > todos-crimenes.json
