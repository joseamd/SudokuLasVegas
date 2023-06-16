# -*- coding: utf-8 -*-
"""Doc sudoku.py
############################################################### 
This module provides methods to asynchronously read a File
to obtain the results of these reads.
###############################################################
"""
import sys
import random
import copy 

from filehandle import * #reader module

class sudoku():
	"""
	Solve a sudoku representation
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

	:param debug: debug 
	:param filename: file path to read
	:param outputname: file path to save
	:type debug: boolean
	:type filename: String
	:type outputname: String
	"""
	
	def __init__(self,debug=False,filename=None,outputname=None):
		"""
		"""
		self.debug = debug
		# self.filename = filename
		# self.outputname = outputname
		self.matrix = []
		self.queens = []

	def start(self,matrix):
		"""
		"""

		accum = [0]*10
		self.readfile = copy.deepcopy(matrix)
		self.matrix = copy.deepcopy(matrix)

		# create queen vector
		for rows in self.matrix:
			for value in rows:
				accum[value] +=1

		accum.pop(0)
		for element in range(0,len(accum)):
			number = accum.index(max(accum))
			self.queens.append(number+1)
			accum[number] = -1

		if self.debug:
			print ("Aplicando algoritmo ... ")
		
		# print " self.matrix ",self.matrix
		return self.solve(self.matrix)

		# if self.debug:
			# print "Guardando respuesta en: "+str(outputname)
		# self.save_sudoku()

	def valid_position(self,matrix=None, row_index=None, col_index=None,value=None):
		# """
		# Verify whether given number in row_index, col_index position of matrix
		# its is feasible 

		# :param matrix: sudoku matrix representation 
		# :type matrix: list
		# :param row_index: row index in matrix representation 
		# :type row_index: int
		# :param col_index: column index in matrix representation 
		# :type col_index: int
		# :param value: value to save in its location
		# :type value: int
		# """
		# dado un valor verifico que no este en la fila
		# con all, verifico si todos los elementos son true
		# recorro todos la fila
		row_valid = all([value != self.matrix[row_index][valid] for valid in range(9)])
		if row_valid:
			# si es valido en fila
			# dado un valor verifico que no este en la columna
			# con all, verifico si todos los elementos son true
			# recorro todos la fila
			col_valid = all([value != self.matrix[valid][col_index] for valid in range(9)])
			if col_valid:
				# Si es valido en mascara (submatris)
				row_mask, col_mask = 3 *(row_index/3), 3 *(col_index/3)
				for posX in range(row_mask, row_mask+3):
					for posY in range(col_mask, col_mask+3):
						if self.matrix[posX][posY] == value:
							return False
				return True
		return False

	def sudoku_candidates(self,matrix=None,row_index=None,queen=None):
		"""
		Returns a random position where set queen in matrix

		:param matrix: sudoku matrix representation 
		:type matrix: list
		:param row_index: row index in matrix representation 
		:type row_index: int
		:param queen: queen to evaluate position
		:type queen: int
		:return: coordiantes array 
        :rtype: array with coordiantes x and y 
		"""
		#lista de posibilidades
		posibities = []
		# hago validacion en columna ya conozco la fila row_index
		for col_index in range(0,len(matrix[row_index])):
			# si esta posicion es modificable
			if self.matrix[row_index][col_index] == 0:
				#si esta es valida
				if self.valid_position(matrix,row_index,col_index,queen):
					# agrego esta a la lista de posibilidades
					posibities.append([row_index,col_index])

		# si no hay posibilidades, pare este no es un camino
		if len(posibities) == 0:
			return -1, -1
		# retorne este opcion factible aleatoria
		feasible = random.randrange(0,len(posibities))
		if self.debug:
			print (" queen ", queen ," in row ",row_index," posibities ", posibities , " feasible ",posibities[feasible])

		#retorno
		return posibities[feasible]



	def sudoku_vegas(self,matrix=None):
		# """
		# Verify whether if all queen are insert in matrix, else return wront path

		# :param matrix: sudoku matrix representation 
		# :type matrix: list
		# :return: success or wront path
        # :rtype: boolean
		# """
		# arranco sin exito
		flag_inserted=False
		# por cada reina en el arreglo
		for queen in range(0, len(self.queens)):
			# recorro todas las filas
			for row_index in range(0,9):
				# is existe reina en esta fila
				if not self.queens[queen] in self.matrix[row_index]:
					# escojo un camino valido
					coors = self.sudoku_candidates(self.matrix,row_index,self.queens[queen])
					# si no hay camino falle
					if coors[0] == -1:
						# empiezo con la matriz nuevamente
						self.matrix = copy.deepcopy(self.readfile)
						# reporto que he fallado
						return flag_inserted
					# Si todo va bien, encontre camino, guardo en la matrix
					self.matrix[ coors[0] ][ coors[1] ]= self.queens[queen]

		# todas reinas han sido insertadas
		flag_inserted=True
		# todas las reinas han  sido insertadas
		return flag_inserted


	def solve(self,matrix=None):
		"""
		:param matrix: sudoku matrix representation 
		:type matrix: list
		"""
		# estado del algoritmo
		state = self.sudoku_vegas(matrix)
		while not state:
			if self.debug:
				print (" Fail! ")
			# vuelva a intentar
			state = self.sudoku_vegas(matrix)
			
		if self.debug:
			print (" Success! ")

		print (" self.matrix ",self.matrix)
		return self.matrix
		# for rows in self.matrix:
		# 	print str(rows)
