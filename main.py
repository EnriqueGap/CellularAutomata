from PIL import Image
import streamlit as st
import time
import src.eca as eca
import matplotlib.pyplot as plt
from re import match

icon = Image.open("./media/page_icon.png")
st.set_page_config(page_title="Cellular Automata",
                   page_icon=icon,
                   layout="wide",
                   initial_sidebar_state="auto"
)
st.header('Cellular Automata')

st.sidebar.image('media/sierpinski.jpeg')
st.sidebar.header('Cellular Automata')
nav=st.sidebar.radio('sidebar',['Home', 'Elementary Cellular Automaton', 'LIFE', 'Authors'], label_visibility='collapsed')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('2023')
st.sidebar.write('How to reach me')
st.sidebar.write('[Enrique Galicia](https://enriquegap.github.io)')

if nav=='Elementary Cellular Automaton':
    st.subheader('Elementary Cellular Automaton')
    st.markdown('___')
    rule = st.selectbox('Select Rules',list(range(0,2**8)))
    iterations = st.text_input('Number of iterations')
    try:
    	iterations = int(iterations)
    except:
    	st.write("Please write a number for iterations")
    size_band = st.text_input('Size of the band')
    try:
    	size_band = int(size_band)
    except:
    	st.write("Please write a number to determine the size of the band")

    if not st.toggle('Random initialization', help='Switch to specify initialization', value=True):
    	initialization = st.text_input("Please give an initialization (Examples: 2**10, 123456789, etc...)")
    	if match(r"^2\*\*[0-9]+$", initialization):
    		initialization = eval(initialization)
    	try:
    		initialization = int(initialization)
    		if (initialization<0)|(initialization>2**size_band-1):
    			st.write("Please enter a valid initialization")
    		else:
    			automata = eca.ECA(size_band, iterations)
    			automata.setRule(rule)
    			automata.setBand(initialization)
    	except:
    		st.write("Please write a number for initialization")

    else:
    	if (size_band!="")&(iterations!=""):
	    	automata = eca.ECA(size_band, iterations)
    		automata.setRule(rule)
    		automata.setBand()   
    		 	
    if st.button('Go!'):
    	number_initialization = int(''.join([str(i) for i in automata.band]), 2)
    	st.write("Initialization: ",number_initialization)
    	automata.evolveBand()
    	fig, ax = plt.subplots()  ## <- Create matplotlib Figure & Axes
    	ax.matshow(automata.matrix, cmap="Greys")
    	ax.get_xaxis().set_visible(False)
    	ax.get_yaxis().set_visible(False)
    	st.pyplot(fig)  ## <- Tell Streamlit to show that figure
