#!/bin/python

import sys, os, random, pygame
sys.path.append(os.path.join("objects"))
import SudokuSquare
import SudokuGrid
from GameResources import *
from filehandle import * #reader module
from sudoku import * #sudoku module

if sys.version_info[0] == 2:
    # print ("Python 2.x")
    import Tkinter as tk
    from tkFileDialog import asksaveasfilename,askopenfilename

           
if sys.version_info[0] == 3:
    # print ("Python 3.x")    
    import tkinter as tk 
    from tkinter.filedialog import asksaveasfilename,askopenfilename 


def getSudoku(puzzleNumber=None):
    """This function defines the solution and the inital view.
    Returns two lists of lists, inital first then solution."""
    inital = SudokuGrid.SudokuGrid()
    current = SudokuGrid.SudokuGrid()
    solution = SudokuGrid.SudokuGrid()
    
    inital.createGrid(27, puzzleNumber)
    current.createGrid(27, puzzleNumber)
    solution.createGrid(81, puzzleNumber)

    return inital, current, solution

def set_matrix(matriz):

	theSquares = []
	initXLoc = 10
	initYLoc = 80
	startX, startY, editable, number = 0, 0, "N", 0

	# print matriz
	for x in range(len(matriz)):
		for y in range(len(matriz)):
			if x in (0,1,2): startX = (x * 41) + (initXLoc + 2)
			if x in (3, 4, 5):  startX = (x * 41) + (initXLoc + 6)
			if x in (6, 7, 8):  startX = (x * 41) + (initXLoc + 10)
			if y in (0, 1, 2):  startY = (y * 41) + (initYLoc + 2)
			if y in (3, 4, 5):  startY = (y * 41) + (initYLoc + 6)
			if y in (6, 7, 8):  startY = (y * 41) + (initYLoc + 10)
			number = matriz[y][x]
			if number != None:
				editable = "N"
	        # print "startX ", startX , "startY ", startY , "number ", number  
			theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

	currentHighlight = theSquares[0]
	currentHighlight.highlight()

	return theSquares


def main():
	# root = tk.Tk(); root.withdraw()
	# fileName = askopenfilename(parent=root,title="Sudoku solver",filetypes=[("wav files","*.txt")])
	# print os.getcwd()+"/entradas/taller3.txt"
	# if fileName != "":
	mat_read = filehandle(False,os.getcwd()+"/entradas/taller3.txt")
	mat_read.read_file()
	matriz = mat_read.get_matrix()
	
	pygame.init()
	size = width, height = 400, 500
	screen = pygame.display.set_mode(size)

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	board, boardRect = load_image("board.png")
	boardRect = boardRect.move(10, 80)
	logo, logoRect = load_image("about.png")
	logoRect = logoRect.move(10, 10)


	puzzleNumber = int(random.random() * 20000) + 1
	pygame.display.set_caption("Simulacion Computacional 2015-II")
	inital, current, solution = getSudoku(puzzleNumber)

	theSquares = []
	initXLoc = 10
	initYLoc = 80
	startX, startY, editable, number = 0, 0, "N", 0

	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			if x in (0, 1, 2):  startX = (x * 41) + (initXLoc + 2)
			if x in (3, 4, 5):  startX = (x * 41) + (initXLoc + 6)
			if x in (6, 7, 8):  startX = (x * 41) + (initXLoc + 10)
			if y in (0, 1, 2):  startY = (y * 41) + (initYLoc + 2)
			if y in (3, 4, 5):  startY = (y * 41) + (initYLoc + 6)
			if y in (6, 7, 8):  startY = (y * 41) + (initYLoc + 10)
			number = matriz[y][x]	
			if number != None:
				editable = "N"
	        # print "startX ", startX , "startY ", startY , "number ", number  
			theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

	currentHighlight = theSquares[0]
	currentHighlight.highlight()

	screen.blit(background, (0, 0))
	screen.blit(board, boardRect)
	screen.blit(logo, logoRect)
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				root = tk.Tk(); root.withdraw()
				fileName = askopenfilename(parent=root,title="Sudoku solver",filetypes=[("wav files","*.txt")])
				if fileName != "":
					mat_read = filehandle(False,fileName)
					mat_read.read_file()
					matriz = mat_read.get_matrix()
					theSquares = set_matrix(mat_read.get_matrix())

			if event.type == pygame.KEYDOWN and event.key == pygame.K_F5:
				sdk = sudoku(True)
				matriz = sdk.start(matriz)
				theSquares = set_matrix(matriz)
				for num in theSquares:
					num.draw()

			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				root = tk.Tk(); root.withdraw()
				fileName = asksaveasfilename(parent=root,defaultextension=".txt")
				if fileName: 
					mat_save = filehandle()
					mat_save.save_sudoku(fileName,matriz)

			if event.type == pygame.MOUSEBUTTONDOWN:
				mousepos = pygame.mouse.get_pos()
				for x in theSquares:
					if x.checkCollide(mousepos):
						currentHighlight.unhighlight()
						currentHighlight = x
						currentHighlight.highlight()

		for num in theSquares:
			num.draw()
		pygame.display.flip()

if __name__ == "__main__":
	main()
