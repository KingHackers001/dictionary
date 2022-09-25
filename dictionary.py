#! /usr/bin/env python3

import sys
import os
import time
from itertools import *

class colors:
	am = "\033[1;33m"
	rj = "\033[91m"
	ci = "\033[1;36m"
	vr = "\033[32m"
	vrf = "\033[42m"
	f = "\033[0m"

def banner():
	os.system("clear")
	sys.stdout.write(colors.ci + '''

      _ _      _   _
   __| (_) ___| |_(_) ___  _ __   __ _ _ __ _   _
  / _` | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
 | (_| | | (__| |_| | (_) | | | | (_| | |  | |_| |
  \__,_|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
                                            |___/
    ──────────────────────────────────────────────
				CREATOR BY: KING
 \n\n''' + colors.f)
time.sleep(2)                                                            
	

def lista():
	global ls
	global salida
	ls = []
	while True:
		try:
			salida = input(colors.ci + "Ingrese un Nombre para su diccionario " + colors.f + colors.rj + ">>  " + colors.f) + (".txt")
			print("")
			num = int((input(colors.ci + "Cuantos elementos desea combinar?" + colors.f + colors.rj + ">>  " + colors.f)))
			print("")
			break
		except ValueError:
			print(colors.rj + "\n ERROR Ingrese un Número!!" + colors.f)
			lista()
	for i in range (num):
		print("")
		x = (input(colors.ci + "Ingrese una palabra" + colors.f + colors.rj + " >>  " + colors.f))
		ls.append((x))
		print("")
	return(ls)
	return(salida)

def comb():
	print (colors.vr + "Por favor espere..." + colors.f)
	print("")
	time.sleep(2)
	global perm
	permutations(ls)
	perm = list(permutations(ls, 1)), list(permutations(ls, 2)), list(permutations(ls, 3)), list(permutations(ls, 4)), list(permutations(ls, 5)), list(permutations(ls, 6))
	
	return perm

def arch():
	repr(perm)
	f = open(salida, "w")
	f.write (repr(perm))
	f.close()


def conf():
	print ("\n".join([str(x) for x in ls]))
	print("")
	conf = (input(colors.am + 'Desea agregar más elementos? ' + colors.f + colors.vr + '[s/n]' + colors.f + colors.rj + ' >>  ' + colors.f))
	if conf == 's':
		iniciar()
	else:
		iniciar2()
def edit():
	ar = open(salida, "r")
	cad = ar.read().replace('\n','').replace('-', ' ')
	salto = ")"
	simbolo = "][(,' "
	for carac in salto:
		cad = cad.replace(carac,"\n")
	for carac in simbolo:
		cad = cad.replace(carac,"")
	
	def cambiAr():
		f = open(salida, "w")
		f.write (cad)
		f.close()

	cambiAr()
	print(colors.vr + "Proceso Terminado!!\n" + colors.f)
	print("")
	time.sleep(2)
	print(colors.vr + '\nVerifique el archivo "' + salida + '"' + colors.f)
	print("")
	
def iniciar():
	banner()
	lista()
	conf()

def iniciar2():
	comb()
	arch()
	banner()
	edit()
	

iniciar()
