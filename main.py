from PIL import Image
import streamlit as st
import src.eca as eca
import matplotlib.pyplot as plt
from re import match

with open("./resources/text/eca.md") as eca_file:
	eca_text = eca_file.read()
icon = Image.open("./resources/images/page_icon.png")
st.set_page_config(page_title="Cellular Automata",
                   page_icon=icon,
                   layout="wide",
                   initial_sidebar_state="auto"
)
st.header('Cellular Automata')

st.sidebar.image('./resources/images/sierpinski.jpeg')
st.sidebar.header('Cellular Automata')
nav=st.sidebar.radio('',['Home', 'Elementary Cellular Automaton', 'LIFE', 'Langton'], index=1)
st.sidebar.write('<br>'*10, unsafe_allow_html=True)
st.sidebar.write('2023<br>How to reach me<br>[Enrique Galicia](https://enriquegap.github.io)<br><br>', unsafe_allow_html=True)

if nav=='Elementary Cellular Automaton':
    st.subheader('Elementary Cellular Automaton')
    st.markdown('___')
    st.markdown(eca_text)
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

    if st.checkbox('Click here for give an initialization'):
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

    if st.checkbox('Click here for a random initialization'):
    	if (size_band!="")&(iterations!=""):
	    	automata = eca.ECA(size_band, iterations)
    		automata.setRule(rule)
    		automata.setBand()

    if st.button('Go!'):
    	number_initialization = int(''.join([str(i) for i in automata.band]), 2)
    	st.write("Initialization: ",number_initialization)
    	automata.evolveBand()
    	fig, ax = plt.subplots()
    	ax.matshow(automata.matrix, cmap="Greys")
    	ax.get_xaxis().set_visible(False)
    	ax.get_yaxis().set_visible(False)
    	st.pyplot(fig)
