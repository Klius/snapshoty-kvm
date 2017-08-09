#!/usr/bin/env/python
__author__ = 'Klius'
#imports go here
import csv
import sys
import argparse
import time
import subprocess
from pprint import pprint

def main(argv):
    kvmIdMaquinas = getMachineIds()
    rutaCopias = "/ruta/a/carpeta/copias"
    rutaDiscos = "/ruta/a/los/discos/virtuales"
    parser = argparse.ArgumentParser(description='Make a qcow2 copy of the selected Machines')
    parser.add_argument("-a","--all",action='store_true',help="do copy of all the machines in the current node")
    args = parser.parse_args()
    if bool( args.all ):
        print("Snapshots de todas las maquinas Iniciado")
    else:
        print("Snapshot diario iniciado")
        rutaCopias += "diarios/"
        makeDailySnapshot(rutaCopias, rutaDiscos)

		
def makeDailySnapshot(rutaCopias, rutaDiscos):
	kvmIdMaquinas = getMachineIds()
	for x in range(0,len(kvmIdMaquinas)):
	    
	    maquina = kvmIdMaquinas[x]
	    maquina = maquina[0].split('#')
	    for i in range(0,len(maquina)):
			if( i == 0):
				rutaAlDisco = rutaCopias+maquina[0]+"_img"
				rutaDestino = rutaCopias+maquina[0]+"_img.qcow2"
			else:
				rutaAlDisco = rutaCopias+maquina[0]+"_img_"+maquina[i]
				rutaDestino = rutaCopias+maquina[0]+"_img_"+maquina[i]+".qcow2"
			
			print(time.strftime("%d/%m/%Y-%H:%M:%S")+"-->Empieza la copia de la maquina "+maquina[0])
			#ret = subprocess.call(['qemu-img', 'convert', '-p','-O','qcow2',rutaAlDisco,rutaDestino ])
			ret = subprocess.call('ls', shell=True)
			if ret != 0:
				if ret < 0:
					print ("Killed by signal", -ret)
				else:
					print ("Command failed with return code", ret)
			else:
				print (time.strftime("%d/%m/%Y-%H:%M:%S")+"-->Acaba la copia de la maquina "+maquina[0])
			
			
			
def getMachineIds():
    ids = []
    with open('machineids.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ids.append(row)
    
    return ids
            


if __name__ == "__main__":
	main(sys.argv[1:])
