from PIL import Image
import streamlit as st
import time

icon = Image.open("./media/page_icon.png")
st.set_page_config(page_title="Cellular Automata",
                   page_icon=icon,
                   layout="wide",
                   initial_sidebar_state="auto"
)
st.header('Cellular Automata')

st.sidebar.image('media/sierpinski.jpeg')
st.sidebar.header('Cellular Automata')
nav=st.sidebar.radio('',['Home', 'Elementary Cellular Automaton', 'LIFE', 'Authors'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('2023')
st.sidebar.write('How to reach me')
st.sidebar.write('[Enrique Galicia](https://enriquegap.github.io)')

from random import randint
from matplotlib.pyplot import matshow, show, savefig
# CellularAutomata 1D
BAND_LENGTH = 150
MAX_ITERS = 500
rule_err = False
band_err = False

def ruleToBinary(rule:int) -> list[int]:
	if (rule>2**8 - 1)|(rule<0):
		binary_rule = "0"*8
		rule_err = True
	else:
		binary_rule = bin(rule)[2:]
		binary_rule = "0"*(8-len(binary_rule)) + binary_rule
	return [int(c) for c in binary_rule]

def initializeBand(band_init:int = None, random_init=True) -> list[int]:
	if band_init:
		random_init=False
	if random_init:
		band = randint(0,2**BAND_LENGTH - 1)
	elif (band_init >2**BAND_LENGTH - 1)|(band_init<0):
		band = 0
		band_err = True
	else:
		band = band_init

	band = bin(band)[2:]
	band = "0"*(BAND_LENGTH - len(band)) + band
	return [int(c) for c in band]

def iterateBand(band:list[int], rule:list[int]) -> list[int]:
	aux_band = [0]*BAND_LENGTH
	for i in range(1, BAND_LENGTH-1):
		if band[i-1] == 1:
			if band[i] == 1:
				if band[i+1] == 1:
					aux_band[i] = rule[0]
				elif band[i+1]==0:
					aux_band[i] = rule[1]
			elif band[i] == 0:
				if band[i+1] == 1:
					aux_band[i] = rule[2]
				elif band[i+1]==0:
					aux_band[i] = rule[3]
		elif band[i-1] == 0:
			if band[i] == 1:
				if band[i+1] == 1:
					aux_band[i] = rule[4]
				elif band[i+1] == 0:
					aux_band[i] = rule[5]
			elif band[i] == 0:
				if band[i+1] == 1:
					aux_band[i] = rule[6]
				elif band[i+1] == 0:
					aux_band[i] = rule[7]
	return aux_band


def getPlot(band_number:int, rule_number:int) -> None:
	matrix = []
	rule = ruleToBinary(rule_number)
	print(rule)
	band = initializeBand(band_number)
	print(band)
	matrix.append(band)
	band_itered = iterateBand(band, rule)
	for i in range(0,MAX_ITERS):
		band_itered = iterateBand(band_itered, rule)
		matrix.append(band_itered)
	matshow(matrix)
	savefig("sierpinski.png")
	show()
	
getPlot(2**25, 90)
