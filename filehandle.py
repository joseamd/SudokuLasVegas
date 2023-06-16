# -*- coding: utf-8 -*-
"""Doc reader.py
############################################################### 
This module provides methods to asynchronously read a File
to obtain the results of these reads.
###############################################################
"""

import sys
import copy

class filehandle():
	"""
	Read a file with sudoku representation
	by example

	0 2 0 6 0 0 0 0 0
	0 7 6 1 0 0 9 0 0
	0 0 0 7 0 0 2 0 0
	8 0 0 0 0 9 0 0 4
	2 1 0 0 8 3 0 0 0
	4 0 0 0 0 0 0 0 7
	0 0 0 0 0 0 0 6 5
	0 0 4 0 6 7 0 0 0
	0 0 0 0 0 0 0 3 0

	Where 0 is permissible change

	:param debug: debug 
	:param filename: file path to read
	:type debug: boolean
	:type filename: String
	"""
	def __init__(self,debug=False,filename=None):
		"""
		Class constructor
		"""
		self.matrix=[]		# matris de numeros. lista de listas
		self.filename = filename # ruta del archivo
		self.debug = debug	# hay depuracion

	def setfile_toread(self,filename=None):
		"""
		:param filename: file path to read
		:type filename: String
		"""
		self.filename = filename

	def get_matrix(self):
		"""
		Returns matrix
     	:returns: list with list inside
        :rtype: list

		"""
		# retorno una copia profunda
		return copy.deepcopy(self.matrix) 

	def getfile_path(self):
		"""
		Returns file path
     	:returns: path file
        :rtype: int

		"""
		return self.filename

	def read_file(self):
		"""
		Read filename and create a list with list inside
		"""
		if self.debug:		# muestro mensaje si hay depuracion
			print ("Leyendo el archivo "+str(filename))
		# self.read_file()	# leo el archivo

		self.file_txt = open(self.filename,'r') # abro como solo lectura
		line = self.file_txt.readline()	# linea a linea
		while line!="":		# mientras no halla algo que leer
			if self.debug:	# si hay depuracion muetro la matris
				print (map(int, line.split(" ")))
			self.matrix.append(map(int, line.split(" ")) )	#agrego esta lista a la lista
			line = self.file_txt.readline()	# leo la linea 
		self.file_txt.close()	# cierro el archivo

		if self.debug:		# muestro mensaje si hay depuracion
			print ("Finalizada lectura ... ")


	def save_sudoku(self,outputname="archivo.txt",matrix =None):
		"""
		Write
		"""
		file_txt = open(outputname,'w')
		for rows in matrix:
			for value in rows:
				file_txt.write(str(value)+" ")
			
			file_txt.write("\n")
		
		file_txt.close()



# by
# Jefferson (JAPeTo)
# Jorge solis
# Eduardo saavedra

