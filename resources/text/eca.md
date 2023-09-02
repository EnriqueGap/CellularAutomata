1. [Introduction](#introduction)

2. [Definition](#definition)

3. [Automaton classification](#automaton-classification)

4. [Evolve your own ECA](#evolve-your-own-eca)

## Introduction

**S. Wolfram** studied elemental celullar automata, dynamics and classification. Following his rules of evolution and behavior over time he proposes a clasification

- Stable (point fixed)

- Periodics

- Chaotics

- Complex

[Stephen Wolfram: A New Kind of Science | Online—Table of Contents](https://www.wolframscience.com/nks/)

**Cellular automata are a discrete dynamic sistem, with a simple construction and a complex self-organized behavior**  Every cellular atomata are divided in four universality classes. Three classes shows a behavior analogous to limit points, limit cycles and chaotic attractors. The fourth class is capable to universal computing. Then the behavior properties given a infinite time are undecidable.

### Definition

El autómata celular elemental es una colección unidimensional de celdas con dos posibles estados $\{0,1\}$, evoluciona a través de pasos en de tiempo discretos de acuerdo a un conjunto de reglas basadas en los estados de sus celtas vecinas

- $a_{i}(t)$ Indica el estado de la celda i-ésima $(i=1,\dots N)$ en el instante discreto $t$
- La dinámica de dicho elemento se define a partir de una vecindad
    
    $$
    a_{i}(t+1)=F(a_{i-1}(t), a_{i}(t), a_{i+1}(t))
    $$
    
    Where the values of $F$ in a transition table compuesta por las posibles ternas formadas con el alfabeto $k=\{0,1\}$ (transition table)
    
    $$
    a_{i-1}(t), a_{i}(t), a_{i+1}(t) \to a_{i}(t+1)
    $$
    
En total, existen $2^3$ posibles ternas y luego $2^8$ posibles tablas de transiciones sobre estas ternas

Wolfram se dió cuenta de que existen todas estas posibles combinaciones conociendose como las reglas 0, 1, …, 255.

Como todo sistema dinámico, necesita una condición inicial a proporcionar en la cinta.

A pesar de ser un sistema determinista, no es predecible.

### Automaton classification

Un problema fundamental en la teoría de autómatas celulares es la clasificación.

Una clasificación satisfactoria divide un AC en grupos con propiedades relacionadas.

### Wolfram's Classification

- **Class I** (24): La evolución del sistema lleva a un estado homogéneo, sin estructuras espaciales ni temporales de ningún tipo
- **Class II** (194): La evolución del sistema da lugar a estructuras separadas de tipo estable o periódico
- **Class III** (26): La evolución da lugar a patrones caóticos. Espacialmente surgen estructuras fractales y temporalmente hay ciclos de longitud muy grandes.
- **Class IV** (12): La evolución genera estructuras complejas localizadas

In his book, he uses Entropy of Shanon, Espatial and temporary to create index and make this classes.

[Wolfram, Universality Complexity Cellular Automata](https://content.wolfram.com/uploads/sites/34/2020/07/universality-complexity-cellular-automata.pdf)

## Evolve your own ECA
