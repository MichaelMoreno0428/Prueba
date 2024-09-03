import streamlit as st
import numpy as np
import random as rd
import pandas as pd
import math as math
from Calculos import *
from Texts import *

#class Questionary stores the information of each exercises
class Questionary:
    def __init__(self, code, no_pregunta,complexity,topic, subtopic,version,pregunta,no_answers,a1_name,a2_name,a3_name,answer1,answer2,answer3,ayuda1,ayuda2,ayuda3,respuesta_P1,respuesta_P2,respuesta_P3,calculos):
        self.code = code ##### Topic, Subtopic, Complexity (1. Fácil, 2. Medio, 3. Díficil), No de la pregunta, Versión
        self.no_pregunta = no_pregunta
        self.complexity = complexity
        self.topic = topic
        self.subtopic = subtopic
        self.version = version
        self.pregunta_func=pregunta
        self.pregunta = ""
        self.no_answers = no_answers
        self.a1_name = a1_name
        self.a2_name = a2_name
        self.a3_name = a3_name
        self.answer1_func=answer1
        self.answer1 = ""
        self.answer2_func=answer2
        self.answer2 = ""
        self.answer3_func=answer3
        self.answer3 = ""
        self.ayuda1 = ayuda1
        self.ayuda2 = ayuda2
        self.ayuda3 = ayuda3
        self.respuestaP1_func=respuesta_P1
        self.respuesta_P1 = ""
        self.respuestaP2_func=respuesta_P2
        self.respuesta_P2 = ""
        self.respuestaP3_func=respuesta_P3
        self.respuesta_P3 = ""
        self.calculos = calculos
        self.generate_values()

    #Function to generate the values of the variables and relates them to the parameters of the class
    def generate_values(self):
        self.fuerzas = calcular_fuerzas()
        self.angulos = calcular_angulos()
        self.coordenadas = calcular_coordenadas()
        self.dimensiones = calcular_dimensiones()
        self.momentos = calcular_momentos()
        #self.calculos = getattr(self, self.calculos)()

        # Check if self.calculos is a string (method name)
        if isinstance(self.calculos, str):
            calculos_method = getattr(self, self.calculos)
            self.calculos = calculos_method()
        # If it's already a method, just call it
        elif callable(self.calculos):
            self.calculos = self.calculos()

        self.pregunta = self.pregunta_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer1 = self.answer1_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer2 = self.answer2_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer3 = self.answer3_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P1 = self.respuestaP1_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P2 = self.respuestaP2_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P3 = self.respuestaP3_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
       
    def regenerate_values(self):
        self.generate_values()

    def operations(self):
        operations_dict = {}

        for i in range(16):  # For each version
            angle = self.angulos[i]
            force = self.fuerzas[i]
            
            #Trigonometry according to the angle
            cos_value = Calculations.cosine(angle)
            sin_value = Calculations.sine(angle)
            tan_value = Calculations.tangent(angle)
            
            # Add values to the dictionary
            operations_dict[f'cos{i+1}'] = cos_value
            operations_dict[f'sin{i+1}'] = sin_value
            operations_dict[f'tan{i+1}'] = tan_value
            operations_dict[f'mag{i+1}_u'] = Calculations.magnitude(cos_value, sin_value)
            operations_dict[f'mag{i+1}_f'] = Calculations.magnitude(force * cos_value, force * sin_value)
        
        return operations_dict
    
   
    #Function to filter the questions according to the user's selection
    def filtrar_preguntas(preguntas, topic=None, subtopic=None, complexity=None):
        preguntas_filtradas = [
            pregunta for pregunta in preguntas
            if (topic is None or pregunta.topic == topic) and
               (subtopic is None or pregunta.subtopic == subtopic) and
               (complexity is None or pregunta.complexity == complexity)
        ]
        return preguntas_filtradas

#List of questions
preguntas = [

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------     Nivel fácil        ---------------------------------------------------
    #-------------------------------------------------     Code: 111####      ---------------------------------------------------
    
    Questionary(#1_1
        code = 1110011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[0], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(90-a[0], 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[0]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${90-a[0]:.0f}°$",
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations'
        ),

    Questionary(#1_2
        code = 1110012,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[1], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[1]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[1]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[1]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#1_3
        code = 1110013,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[2], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[2]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[2]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[2]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_4
        code = 1110014,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[3], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[3]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[3]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[3]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1110021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 1),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_2
        code = 1110022,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos2'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin2'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 2),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#2_3
        code = 1110023,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos3'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin3'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 3),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_4
        code = 1110024,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos4'],2),
        answer2=lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin4'],2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 4),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1110031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas del punto A son ({c[0]:.0f},{c[1]:.0f}) y las del punto B son ({c[3]:.0f},{c[4]:.0f})",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[4]-c[1])/(c[3]-c[0]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A8,
        ayuda3= A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[0], c[1], c[3], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1110032,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas del punto A son ({c[3]:.0f},{c[4]:.0f}) y las del punto B son ({c[0]:.0f},{c[1]:.0f})",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: (c[1]-c[4])/(c[0]-c[3]),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[3], c[4], c[0], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_3
        code = 1110033,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas del punto A son ({c[3]:.0f},{c[1]:.0f}) y las del punto B son ({c[0]:.0f},{c[4]:.0f})",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[4]-c[1])/(c[0]-c[3]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[3], c[1], c[0], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_4
        code = 1110034,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas del punto A son ({c[0]:.0f},{c[4]:.0f}) y las del punto B son ({c[3]:.0f},{c[1]:.0f})",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[1]-c[4])/(c[3]-c[0]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1=lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[0], c[4], c[3], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1110041,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas del punto A son ({c[0]:.0f}, {c[1]:.0f}) y las del punto B son ({c[3]:.0f}, {c[4]:.0f})",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3= A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[0], c[1], c[3], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_2
        code = 1110042,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas del punto A son ({c[3]:.0f}, {c[4]:.0f}) y las del punto B son ({c[0]:.0f}, {c[1]:.0f})",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3= A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[3], c[4], c[0], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_3
        code = 1110043,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas del punto A son ({c[3]:.0f}, {c[1]:.0f}) y las del punto B son ({c[0]:.0f}, {c[4]:.0f})",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt((c[0]-c[3])**2+(c[4]-c[1])**2),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A10,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P4(c[3], c[1], c[0], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_4
        code = 1110044,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector F1 está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de F1 (|F1|)?. Las coordenadas del punto A son ({c[0]:.0f}, {c[4]:.0f}) y las del punto B son ({c[3]:.0f}, {c[1]:.0f})",
        no_answers = 1,
        a1_name = "Magnitud F1 (|F1|)",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[0], c[4], c[3], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1110051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo del vector cartesiano $[({c[0]:.0f}) i + ({c[1]:.0f}) j] N$.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(c[0],c[1]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(c[0],c[1]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A11,
        ayuda2 = A12,
        ayuda3 = A13,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} F = \\sqrt{{Fx^2+Fy^2}} = {Calculations.magnitude(c[0],c[1]):.2f}}} \\text{{N}}$

        $\\textbf{{\\small 2. Cálculo del ángulo:}}$

        ${{\hspace{{4mm}} \\alpha ={Calculations.define_angle(c[0],c[1]):.2f}}}°$

        El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

        -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$ 
        
        """,     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------     Nivel medio        ---------------------------------------------------
    #-------------------------------------------------     Code: 112####      ---------------------------------------------------

    Questionary(#1_1
        code = 1120011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(f[0], f[0], f[1], f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#1_2
        code = 1120012,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['cos1']-f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(-f[0], f[0], -f[1], f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#1_3
        code = 1120013,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['cos1']-f[1]*calc['cos5'],-f[0]*calc['sin1']-f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(-f[0], -f[0], -f[1], -f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#1_4
        code = 1120014,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['cos1']+f[1]*calc['cos5'],-f[0]*calc['sin1']-f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(f[0], -f[0], f[1], -f[1], calc, 1, 5),   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",  
        calculos='operations',
        ),

    Questionary(#2_1
        code = 1120021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(-f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(-f[0], f[0], -f[1], -f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#2_2
        code = 1120022,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(f[0], f[0], -f[1], f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#2_3
        code = 1120023,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(f[0], -f[0], -f[1], -f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#2_4
        code = 1120024,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(-f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(-f[0], -f[0], -f[1], f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#3_1
        code = 1120031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"El cofre mostrado en la figura es desplazado mediante dos cuerdas. Si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$, determine las magnitudes de $F2$ y de la fuerza resultante $(F_R)$ de tal forma que esta se dirija a lo largo del eje X.",
        no_answers = 2,
        a1_name = "Magnitud $F2$ [kN]",
        a2_name = "Magnitud $F_R$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*calc['sin1'])/calc['sin5']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A18,
        ayuda3 = A19,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

        ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1) = {f[0]*calc['cos1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1) = {f[0]*calc['sin1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2)}}$  
        ${{\hspace{{4mm}} F2_y = -F2*sen(\\alpha_2)}}$  

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}\\text{{Esta sumatoria equivale a 0, dado que, la fuerza resultante actúa únicamente en el eje X. A partir de esta ecuación se despeja la magnitud de F2:}}$

        ${{\hspace{{4mm}}\\sum{{F_y}} = F1_y + F2_y = 0}}$  

        ${{\hspace{{4mm}} |F2| = \\dfrac{{F1*sen(\\alpha_1)}}{{sen(\\alpha_2)}} ={(f[0]*calc['sin1'])/calc['sin5']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 3. Sumatoria de fuerzas en X:}}\\text{{El valor de esta sumatoria equivale a la magnitud de la fuerza resultante, dado que, solo actúa en este eje.}}$
        
        ${{\hspace{{4mm}}\\sum{{F_X}} = F1_x + F2_x = F_R}}$  
        ${{\hspace{{4mm}}\\sum{{F_X}} = F_R = {f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5']:.2f} \\text{{ kN}} }}$  
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1120032,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"El cofre mostrado en la figura es desplazado mediante dos cuerdas. Si se sabe que $F2={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$, determine las magnitudes de $F1$ y de la fuerza resultante $(F_R)$ de tal forma que esta se dirija a lo largo del eje X.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F_R$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*calc['sin5'])/calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[1]*calc['cos2']+((f[0]*calc['sin5'])/calc['sin1'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A18,
        ayuda3 = A19,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

        ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1)}}$  
        ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1)}}$  
        ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {f[0]*calc['cos1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F2_y = -F2*sen(\\alpha_2) = {f[0]*calc['sin1']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}\\text{{Esta sumatoria equivale a 0, dado que, la fuerza resultante actúa únicamente en el eje X. A partir de esta ecuación se despeja la magnitud de F1:}}$

        ${{\hspace{{4mm}}\\sum{{F_y}} = F1_y + F2_y = 0}}$  

        ${{\hspace{{4mm}} |F2| = \\dfrac{{F2*sen(\\alpha_2)}}{{sen(\\alpha_1)}} ={(f[0]*calc['sin5'])/calc['sin1']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 3. Sumatoria de fuerzas en X:}}\\text{{El valor de esta sumatoria equivale a la magnitud de la fuerza resultante, dado que, solo actúa en este eje.}}$
        
        ${{\hspace{{4mm}}\\sum{{F_X}} = F1_x + F2_x = F_R }}$  
        ${{\hspace{{4mm}}\\sum{{F_X}} = F_R = {f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5']:.2f} \\text{{ kN}} }}$  
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1120041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Para el descenso del globo aerostático mostrado en la figura se requiere una fuerza vertical de $FR={f[0]:.0f} \\text{{ kN}}$. Determine las magnitudes de $F1$ y $F2$ si $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "",
        answer1 =lambda f, a, calc, c, d, m: np.round((f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']),2),
        answer2 =lambda f, a, calc, c, d, m: np.round(((((-f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1'])+f[0])/calc['cos5'],2),
        answer3 =lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A20,
        ayuda3 = A12,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        Se analiza de acuerdo con lo requerido en el enunciado a que equivale cada sumatoria.

        $\\underline{{Ecuación \\hspace{{2mm}} 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x = -F1*sen(\\alpha_1) + F2*sen(\\alpha_2) = 0}}$

        $\\underline{{Ecuación \\hspace{{2mm}} 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_y}} = -F_R }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = -F1*cos(\\alpha_1)-F2*cos(\\alpha_2) = -F_R}}$
        

        $\\textbf{{\\small 2. Despejar las magnitudes:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anterior, se despeja F2 de la Ecuación 2 y se reemplaza en la Ecuación 1 para despejar F1. Con el valor de F1 obtenido, se halla F2.

        De la ecuación 2 se despeja F2:  

        ${{\hspace{{4mm}} F2 = \\dfrac{{-F1*cos(\\alpha_1)+F_R}}{{cos(\\alpha_2)}}}}$

        Se reemplaza F2 en la ecuación 1:

        ${{\hspace{{4mm}} -F1*sen(\\alpha_1) + \\left(\\dfrac{{-F1*cos(\\alpha_1)+F_R}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2) = 0}}$

        ${{\hspace{{4mm}} -F1*sen(\\alpha_1)-F1*cos(\\alpha_1)*tan(\\alpha_2)+F_R*tan(\\alpha_2)=0}}$

        ${{\hspace{{4mm}} -F_R*tan(\\alpha_2)=F1(sen(\\alpha_1)+cos(\\alpha_1)*tan(\\alpha_2))}}$

        ${{\hspace{{4mm}} F1=\\dfrac{{F_R*tan(\\alpha_2)}}{{sen(\\alpha_1)+cos(\\alpha_1)*tan(\\alpha_2)}}}}$  

        ${{\hspace{{4mm}} F1={(f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']):.2f}}} \\text{{ kN}}$

        Con el valor de F1 se calcula F2:  

        ${{\hspace{{4mm}} F2 = {((((-f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1'])+f[0])/calc['cos5']:.2f}}} \\text{{ kN}}$
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_2
        code = 1120042,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Para el descenso del globo aerostático mostrado en la figura se requiere una fuerza vertical de $FR={f[0]:.0f} \\text{{ kN}}$. Determine la magnitud de $F1$ y el ángulo $\\alpha_1$, si $F2 = {f[1]:.0f} \\text{{ kN}}$ y $\\alpha_2 = {a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Ángulo $\\alpha_1$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]-f[1]*calc['cos5'])/Calculations.cosine(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5'])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A20,
        ayuda3 = A21,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        Se analiza de acuerdo con lo requerido en el enunciado a que equivale cada sumatoria.

        $\\underline{{Ecuación \\hspace{{2mm}} 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x = -F1*sen(\\alpha_1) + F2*sen(\\alpha_2) = 0}}$

        $\\underline{{Ecuación \\hspace{{2mm}} 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_y}} = F_R }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = -F1*cos(\\alpha_1)-F2*cos(\\alpha_2) = -F_R}}$
        
        $\\textbf{{\\small 2. Despeje del ángulo:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se obtiene una expresión para hallar el ángulo desconocido.

        De la ecuación 2 se despeja F1:

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_2)-FR}}{{cos(\\alpha_1)}}}}$

        Se reemplaza F1 en la ecuación 1:

        ${{\hspace{{4mm}} F1 = -\\left(\\dfrac{{-F2*cos(\\alpha_2)-FR}}{{cos(\\alpha_1)}}\\right)*sen(\\alpha_1)+F2*sen(\\alpha_2) = 0}}$

        ${{\hspace{{4mm}} F1 = -({{-F2*cos(\\alpha_2)+FR}})*tan(\\alpha_1)=-F2*sen(\\alpha_2)}}$

        ${{\hspace{{4mm}} \\alpha_1 = tan^{-1}\\left(\\dfrac{{-F2*sen(\\alpha_2)}}{{F2*cos(\\alpha_2)+FR}}\\right)}}$    

        ${{\hspace{{4mm}} \\alpha_1 ={Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5']):.2f} °}}$

        $\\textbf{{\\small 3. Despejar la magnitud:}}$

        Se puede retomar la ecuación de F1 mostrada en el paso anterior o despejarla de la ecuación 1:

        ${{\hspace{{4mm}} F1 = \\dfrac{{F2*sen(\\alpha_2)+F_R}}{{sen(\\alpha_1)}}}}$  
        ${{\hspace{{4mm}} F1 = {(f[0]-f[1]*calc['cos5'])/Calculations.cosine(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5'])):.2f} \\text{{ kN}}}}$
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1120051,
        no_pregunta = 5,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y dirección respecto al eje X positivo de la fuerza resultante de los vectores cartesianos $F_1=[({c[0]:.0f}) i + ({c[1]:.0f}) j] N$, $F_2=[({c[2]:.0f}) i + ({c[3]:.0f}) j] N$ y $F_3=[({c[4]:.0f}) i + ({c[5]:.0f}) j] N$",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(c[0]+c[2]+c[4],c[1]+c[3]+c[5]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(c[0]+c[2]+c[4],c[1]+c[3]+c[5]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A11,
        ayuda2 = A15,
        ayuda3 = A13,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X y Y de la fuerza resultante:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x + F3_x = ({c[0]}) i + ({c[2]}) i + ({c[4]}) i = {c[0]+c[2]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y + F3_y = ({c[1]}) j + ({c[3]}) j + ({c[5]}) j ={c[1]+c[3]+c[5]:.2f} \\text{{ N}} }}$  

        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(c[0]+c[2]+c[4],c[1]+c[3]+c[5]):.2f} }} \\text{{ N}}$

        $\\textbf{{\\small 3. Cálculo de la dirección:}}$

        ${{\hspace{{4mm}} \\alpha ={Calculations.define_angle(c[0]+c[2]+c[4],c[1]+c[3]+c[5]):.2f}}}°$

        El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

        -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
        -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$ 

        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------    Nivel díficil       ---------------------------------------------------
    #-------------------------------------------------     Code: 113####      ---------------------------------------------------

    Questionary(#1_1
        code = 1130011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de la fuerza $F$ a lo largo de los ejes $u-u$ y $v-v$, si se sabe que $|\\overrightarrow{{F}}|={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}°$ y $\\alpha_2={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Componente $u$ [kN]",
        a2_name = "Componente $v$ [kN]",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin1'])/Calculations.sine(180-a[0]-a[4]),2),
        answer2=lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin5'])/Calculations.sine(180-a[0]-a[4]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A24,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1,     
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P1(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1130021,
        no_pregunta = 2,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si la componente de la fuerza a lo largo del eje $u-u$ debe ser ${f[0]:.0f} \\text{{ kN}}$. Determine la magnitud de F y su componente a lo largo del eje $v-v$ si se sabe que $\\alpha_1={a[0]:.0f}°$ y $\\alpha_2={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = "Componente $v$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]*Calculations.sine(180-a[0]-a[4]))/calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin5'])/calc['sin1'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A25,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P2(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    Questionary(#3_1
        code = 1130031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes X y Y de la fuerza F si la componente $F_u$ es ${f[0]:.0f} \\text{{ kN}}$. Considere que $\\alpha_u={a[0]:.0f}°$, $\\alpha_v={a[8]:.0f}°$ y $\\alpha_Y={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Componente en X [kN]",
        a2_name = "Componente en Y [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['sin5'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A25,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P3(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    Questionary(#4_1
        code = 1130041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Para remolcar el bote se requiere una fuerza horizontal, a lo largo del eje X positivo, de ${f[0]:.0f}\\text{{ kN}}$. Determine las magnitudes de $F1$, $F2$ y el ángulo $\\alpha_2$ de forma que $F2$ sea mínima. Considere que $F1$ se ejerce a ${a[0]:.0f}$° del eje X ($\\alpha_1$).",
        no_answers = 3,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "Ángulo $\\alpha_2$",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.sine(180-90-a[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.sine(a[0]),2),
        answer3 = lambda f, a, calc, c, d, m: 180-90-a[0],
        ayuda1 = A27,
        ayuda2 = A28,
        ayuda3 = A29,
        respuesta_P1 = lambda f, a, calc, c, d, m: T2, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P4(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1130051,
        no_pregunta = 5,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud mínima de la fuerza resultante de las tres fuerzas ($FR$) y la fuerza $F2$ que las genera. Considere que $F1$ es ${f[0]:.0f}\\text{{ kN}}$, $F3$ es ${f[1]:.0f}\\text{{ kN}}$ y $\\alpha_1$ es ${85-Calculations.define_angle(f[1],f[0]):.2f}$°",
        no_answers = 2,
        a1_name = "Magnitud $FR$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[1],f[0])*Calculations.sine(85),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[1],f[0])*Calculations.sine(180-90-85),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A30,
        ayuda2 = A31,
        ayuda3 = A32,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P5_P1(f[1], f[0], a),
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P5_P2(f[1], f[0], a),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil       ---------------------------------------------------
    #-------------------------------------------------     Code: 121####       ---------------------------------------------------

    Questionary(#1_1
        code = 1210011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes del vector $F={f[0]:.0f} \\text{{ N}}$, si $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1']*calc['sin5'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1']*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1'],2),
        ayuda1 = A33,
        ayuda2 = A34,
        ayuda3 = A35,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta el procedimiento sugerido para hallar las componentes:
        
        $\\textbf{{\\small 1. Cálculo de las componentes X y Y:}}$

        Se recomienda primero proyectar el vector F en el plano XY y luego utilizar la trigonometría para determinar sus componentes.

        ${{\\text{{Componente en X (i):}}}} F*sen(\\theta_1)*sen(\\theta_2) = [{f[0]*calc['sin1']*calc['sin5']:.2f} {{\\text{{ i] N}}}}$     
        ${{\\text{{Componente en Y (j):}}}} F*sen(\\theta_1)*cos(\\theta_2) = [{f[0]*calc['sin1']*calc['cos5']:.2f} {{\\text{{ j] N}}}}$       

        $\\textbf{{\\small 2. Cálculo de la componente Z (k):}}$

        El ángulo $\\theta_1$ permite encontrar directamente la componente en Z.

        ${{\\text{{Componente en Z:}}}} F*cos(\\theta_1) = [{f[0]*calc['cos1']:.2f} {{\\text{{ k] N}}}}$

        De acuerdo con lo anterior el vector cartesiano de $F1$ es $[{f[0]*calc['sin1']*calc['sin5']:.2f} i + {f[0]*calc['sin1']*calc['cos5']:.2f} j + {f[0]*calc['cos1']:.2f} k]\\text{{ N}}$.       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1210021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados del vector $F={f[0]:.0f} \\text{{ N}}$, si $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['sin1']*calc['sin5'],f[0]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['sin1']*calc['cos5'],f[0]),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['cos1'],f[0]),2),
        ayuda1 = A36,
        ayuda2 = A37 ,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z:}}$

        ${{\hspace{{4mm}}\\text{{Componente en X: }}}} F*sen(\\theta_1)*sen(\\theta_2) = {f[0]*calc['sin1']*calc['sin5']:.2f} \\text{{ N}}$     
        ${{\hspace{{4mm}}\\text{{Componente en Y: }}}} F*sen(\\theta_1)*cos(\\theta_2) = {f[0]*calc['sin1']*calc['cos5']:.2f} \\text{{ N}}$      
        ${{\hspace{{4mm}} \\text{{Componente en Z: }}}} F*cos(\\theta_1) = {f[0]*calc['cos1']:.2f} \\text{{ N}}$    

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['sin1']*calc['sin5'],f[0]):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['sin1']*calc['cos5'],f[0]):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['cos1'],f[0]):.2f}°}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1210031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud del vector $\\overrightarrow{{F}}$ si $F_x = {f[0]:.0f}\\text{{ N}}$, $F_y = {f[1]:.0f}\\text{{ N}}$ y $F_z = {f[2]:.0f}\\text{{ N}}$.",
        no_answers = 1,
        a1_name = "Magnitud [N]]",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(f[0],f[1],f[2]),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A39,
        ayuda2 = A40,
        ayuda3="",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:

        $\\textbf{{\\small 1. Definir el vector cartesiano:}}$

        El vector cartesiano de $\\overrightarrow{{F}}$ es $[{f[0]:.0f}i+{f[1]:.0f}j-{f[2]:.0f}K]N$. Recuerde que las componentes $i, j, k$ se extienden a lo largo de los ejes X, Y y Z, respectivamente. 
        
        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        La magnitud se calcula como $\\sqrt{{F_x^2 + F_y^2 + F_z^2}}$ = $|\\overrightarrow{{F}}|={Calculations.magnitude3D(f[0],f[1],f[2]):.2f}\\text{{ N}}$       
        """,  
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1210041,
        no_pregunta = 4,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vectores 3D",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores del vector F si $F_x = {f[0]:.0f}\\text{{N}}$, $F_y = {f[1]:.0f}\\text{{N}}$ y $F_z = {f[2]:.0f}\\text{{N}}$.",
        no_answers = 3,
        a1_name = "Ángulo respecto a X $(\\alpha)$ [°]",
        a2_name = "Ángulo respecto a Y $(\\beta)$ [°]",
        a3_name = "Ángulo respecto a Z $(\\gamma)$ [°]",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[1],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[2],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        ayuda1 = A36,
        ayuda2 = A39,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector $\\overrightarrow{{F}}$.
        
        $\\textbf{{\\small 1. Cálculo de la magnitud:}}$

         La magnitud se calcula como $\\sqrt{{F_x^2 + F_y^2 + F_z^2}}=$ $|\\overrightarrow{{F}}|={Calculations.magnitude3D(f[0],f[1],f[2]):.2f}\\text{{ N}}$

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[1],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[2],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1210051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes del vector $\\overrightarrow{{F}}$ si su magnitud es ${f[0]:.0f} \\text{{ N}}$ y sus ángulos coordenados son $\\alpha_x = {a[0]:.0f}°$, $\\beta_y = {a[5]:.0f}°$ y $\\gamma_z = {a[4]:.0f}°$  ",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[5]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[4]),2),
        ayuda1 = "Los ángulos directores relacionan directamente al vector F con cada uno de los ejes.",
        ayuda2 = "$i$ representa la componente paralela al eje X, $j$ a la componente paralela a Y y $k$ a la componente paralela a Z.",
        ayuda3 = "Calcule las componentes de cada eje como la multiplicación de la fuerza por el coseno del ángulo que forma con dicho eje.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para calcular las componentes se multiplica la magnitud del vector F con el coseno del ángulo que forma la fuerza con el eje.
        
        $\\textbf{{\\small 1. Cálculo de las componentes:}}$

        ${{\hspace{{4mm}} \\text{{Componente en X: }} F_x = F*cos(\\alpha_x)={f[0]*Calculations.cosine(a[0]):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\text{{Componente en Y: }} F_y = F*cos(\\beta_y)={f[0]*Calculations.cosine(a[5]):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\text{{Componente en Z: }} F_z = F*cos(\\gamma_z)={f[0]*Calculations.cosine(a[4]):.2f} \\text{{ N}}}}$
        
        De acuerdo con lo anterior el vector cartesiano de F es:  $\\overrightarrow{{F}} = [({f[0]*Calculations.cosine(a[0]):.2f})i + ({f[0]*Calculations.cosine(a[5]):.2f}) j + ({f[0]*Calculations.cosine(a[4]):.2f}) k] N$.
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       --------------------------------------------------
    #-------------------------------------------------       Nivel medio       --------------------------------------------------
    #-------------------------------------------------     Code: 122####       ---------------------------------------------------

    Questionary(#1_1
        code = 1220011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante (FR) entre los vectores F1 y F2. Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$, $\\theta_1 = {a[1]:.0f}\\degree$ y $\\theta_2 = {a[0]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud FR [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A41,
        ayuda2 = A42,
        ayuda3 = A43,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*sen(\\tetha_2) = {f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1']:.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F1*\\dfrac{{5}}{{13}}*cos(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*cos(\\tetha_2) = {-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1']:.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} = {-f[0]*(12/13)+f[1]*(3/5):.2f}}}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{F}} = ({f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1']:.2f})i + ({-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1']:.2f})$ j + + ({-f[0]*(12/13)+f[1]*(3/5):.2f})$ k.
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrigtharrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5)):.2f}}}$       
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1220021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante (FR) entree los vectores F1 y F2. Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$, $\\theta_1 = {a[1]:.0f}\\degree$ y $\\theta_2 = {a[0]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*(12/13)+f[1]*(3/5),Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))),2),
        ayuda1 = A36,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*sen(\\tetha_2) = {f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1']:.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F1*\\dfrac{{5}}{{13}}*cos(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*cos(\\tetha_2) = {-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1']:.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} = {-f[0]*(12/13)+f[1]*(3/5):.2f}}}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{F}} = ({f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1']:.2f})i + ({-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1']:.2f})$ j + + ({-f[0]*(12/13)+f[1]*(3/5):.2f})$ k.
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrigtharrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5)):.2f}}}$       
        
        $\\textbf{{\\small 3. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*(12/13)+f[1]*(3/5),Calculations.magnitude3D(f[0]*(5/13)*calc['sin2']+f[1]*(4/5)*calc['sin1'],-f[0]*(5/13)*calc['cos2']+f[1]*(4/5)*calc['cos1'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1220031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de F1 y F2 para que la componente X de la fuerza resultante sea {f[0]:.0f} $\\text{{ N}}$ y la componente Z sea {f[1]:.0f} $\\text{{ N}}$ cuando $\\theta_1 = {a[1]:.0f}\\degree$ y $\\theta_2 = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Magnitud F1 [N]",
        a2_name = "Magnitud F2 [N]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]-(4/3)*f[1]*calc['sin1'])/((4/3)*calc['sin1']*(12/13)+(5/13)*calc['sin2']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((5/3)*(f[1]+(12/13)*((f[0]-(4/3)*f[1]*calc['sin1'])/((4/3)*calc['sin1']*(12/13)+(5/13)*calc['sin2']))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A44,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Sistema de ecuaciones - Sumatoria de fuerzas en X y Z:}}$

        $\\underline{{Ecuación 1}}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*sen(\\tetha_2)}}$
        ${{\hspace{{4mm}}  {f[0]} = F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) + F2*\\dfrac{{4}}{{5}}*sen(\\tetha_2)}}$

        $\\underline{{Ecuación 2}}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} }}$
        ${{\hspace{{4mm}} {f[1]} = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} }}$

        $\\textbf{{\\small 2. Despejar las magnitudes F1 y F2:}}$

        De la ecuación 2 se despeja F2 en términos de F1:

        ${{\hspace{{4mm}} = {f[1]} + F1*\\dfrac{{12}}{{13}} = F2*\\dfrac{{3}}{{5}} }}$
        ${{\hspace{{4mm}} = F2 = \\dfrac{{5}}{{3}}*\\left({f[1]} + F1*\\dfrac{{12}}{{13}}\\right) }}$

        Se reemplaza F2 en la ecuación 1:

        ${{\hspace{{4mm}} {f[0]} = F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) + \\left(\\dfrac{{5}}{{3}}*\\left({f[1]} + F1*\\dfrac{{12}}{{13}}\\right)\\right)*\\dfrac{{4}}{{5}}*sen(\\tetha_2)}}$
        ${{\hspace{{4mm}} {f[0]} - F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) = \\left(\\dfrac{{4}}{{3}}*\\left({f[1]} + F1*\\dfrac{{12}}{{13}}\\right)\\right)*sen(\\tetha_2)}}$
        ${{\hspace{{4mm}} {f[0]} - F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) = \\dfrac{{4}}{{3}}*{f[1]}*sen(\\tetha_2) + \\dfrac{{4}}{{3}}*sen(\\tetha_2)*F1*\\dfrac{{12}}{{13}} }}$
        ${{\hspace{{4mm}} {f[0]} - \\dfrac{{4}}{{3}}*{f[1]}*sen(\\tetha_2) = \\dfrac{{4}}{{3}}*sen(\\tetha_2)*F1*\\dfrac{{12}}{{13}} + F1*\\dfrac{{5}}{{13}}*sen(\\tetha_1) }}$
        ${{\hspace{{4mm}} F1*\\left(\\dfrac{{4}}{{3}}*sen(\\tetha_2)*\\dfrac{{12}}{{13}} + \\dfrac{{5}}{{13}}*sen(\\tetha_1)  \\rigth) = {f[0]} - \\dfrac{{4}}{{3}}*{f[1]}*sen(\\tetha_2) }}$
        ${{\hspace{{4mm}} F1 = \\dfrac{{{f[0]} - \\dfrac{{4}}{{3}}*{f[1]}*sen(\\tetha_2)}}{{\dfrac{{4}}{{3}}*sen(\\tetha_2)*\\dfrac{{12}}{{13}} + \\dfrac{{5}}{{13}}*sen(\\tetha_1) }}}}
       
        Reemplazando en las ecuaciones de F1 y F2 se obtiene: 
        F1 = {(f[0]-(4/3)*f[1]*calc['sin1'])/((4/3)*calc['sin1']*(12/13)+(5/13)*calc['sin2']):.2f}
        F2 = {(5/3)*(f[1]+(12/13)*((f[0]-(4/3)*f[1]*calc['sin1'])/((4/3)*calc['sin1']*(12/13)+(5/13)*calc['sin2']))):.2f}
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1220041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante (FR) entre los vectores $F_1=[({c[0]:.0f}) i + ({c[1]:.0f}) j + ({c[2]:.0f}) k] N$, $F_2=[({c[3]:.0f}) i + ({c[4]:.0f}) j + + ({c[5]:.0f}) k] N$.",
        no_answers = 1,
        a1_name = "Magnitud FR [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A42,
        ayuda2 = A40,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x = ({c[0]}) i + ({c[3]}) i = {c[0]+c[3]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y = ({c[1]}) j + ({c[4]}) j = {c[1]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z = ({c[2]}) k + ({c[5]}) k = {c[2]+c[5]:.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = ({c[0]+c[3]:.2f}) i + ({c[1]+c[4]:.2f}) j + ({c[2]+c[5]:.2f}) k.

        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}| = \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]):.2f} \\text{{ N}} }}$       
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1220051,
        no_pregunta = 5,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante (FR) entre los vectores $F_1=[({c[0]:.0f}) i + ({c[1]:.0f}) j + ({c[2]:.0f}) k] N$, $F_2=[({c[3]:.0f}) i + ({c[4]:.0f}) j + + ({c[5]:.0f}) k] N $.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round((c[0]+c[3])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((c[1]+c[4])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((c[2]+c[5])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]),2),
        ayuda1 = A42,
        ayuda2 = A36,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1_x + F2_x = ({c[0]}) i + ({c[3]}) i = {c[0]+c[3]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = F1_y + F2_y = ({c[1]}) j + ({c[4]}) j = {c[1]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = F1_z + F2_z = ({c[2]}) k + ({c[5]}) k = {c[2]+c[5]:.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = ({c[0]+c[3]:.2f}) i + ({c[1]+c[4]:.2f}) j + ({c[2]+c[5]:.2f}) k.

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {(c[0]+c[3])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {(c[1]+c[4])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {(c[2]+c[5])/Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]):.2f}°}}$
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       --------------------------------------------------
    #-------------------------------------------------       Nivel díficil       --------------------------------------------------
    #-------------------------------------------------     Code: 123##        ---------------------------------------------------

    Questionary(#1_1
        code = 1230011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante (FR). Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$ y se ubica en las coordenadas (-{d[0]:.0f}, -{d[3]:.0f}, -{d[6]:.0f}), $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud FR [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*Calculations.arccosine(d[3],Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A41,
        ayuda2 = A42,
        ayuda3 = A43,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = -F1*cos(\\tetha_1)-F2*\\left(\\dfrac{{x}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F3*sen(\\tetha_2) = {-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F2*\\left(\\dfrac{{y}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)+F4*(3/5) = {-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\tetha_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5) = {-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f}}}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{F}} = ({-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f})i + ({-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f})$ j +  ({-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f})$ k.
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrigtharrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)):.2f}}}$       
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #Questionary(#2_1
    #    code = 12321,
    #    no_pregunta = 2,
    #    complexity = D,
    #    topic = EQ,
    #    subtopic = V3D,
    #    version = 1,
    #    pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante (FR).Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$ y se ubica en las coordenadas (-{d[0]:.0f}, -{d[3]:.0f}, -{d[6]:.0f}), $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
    #    no_answers = 3,
    #    a1_name = A3X,
    #    a2_name = A3Y,
    #    a3_name = A3Z,
    #    answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
    #    answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
    #    answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*calc['sin1']+f[1]*(d[2]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
    #    ayuda1 = A36,
    #    ayuda2 = A37,
    #    ayuda3 = A38,
    #    respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #    Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
    #    ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = -F1*cos(\\tetha_1)-F2*\\left(\\dfrac{{x}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F3*sen(\\tetha_2) = {-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f}}}$
    #    ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F2*\\left(\\dfrac{{y}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)+F4*(3/5) = {-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f}}}$
    #    ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\tetha_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5) = {-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f}}}$
        
    #    De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{F}} = ({-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f})i + ({-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f})$ j +  ({-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f})$ k.
        
    #    $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

    #    ${{\hspace{{4mm}} |\\overrigtharrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)):.2f}}}$       
        
    #    $\\textbf{{\\small 3. Cálculo de los ángulos directores coordenados:}}$

    #    ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
    #    ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
    #    ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*calc['sin1']+f[1]*(d[2]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
    #    """, 
    #    respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #    respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
    #    calculos='operations'
    #    ),

    Questionary(#3_1
        code = 1230031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de F1 para que la componente Z de la fuerza resultante sea {f[0]:.0f} $\\text{{ N}}. Suponga que $F2 = {f[1]:.0f} \\text{{ N}}$ y se ubica en las coordenadas (-{d[0]:.0f}, -{d[3]:.0f}, -{d[6]:.0f}), $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud F1 [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)-f[0])/calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A44,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Sumatoria de fuerzas en Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\tetha_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5)}}$
        ${{\hspace{{4mm}} {f[0]:.0f} = -F1*sen(\\tetha_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5)}}$     

        $\\textbf{{\\small 2. Despejar la magnitudes de F1:}}$

        ${{\hspace{{4mm}} = F1*sen(\\tetha_1) = F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5)- {f[0]:.0f} }}$
        ${{\hspace{{4mm}} F1 = \\dfrac{{F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\tetha_2)-F4*(4/5)- {f[0]:.0f}}}{{sen(\\tetha_1)}} }}$

        F1 = {(f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)-f[0])/calc['sin1']:.2f}
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1230041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes en X, Y y Z de la fuerza resultante (FR) entre los vectores que inician en el origen: $F1 = {f[0]:.0f} \\text{{ N}} localizado en {d[0]},{d[1]},{d[2]}$, $F2 = {f[1]:.0f} \\text{{ N}} localizado en {d[3]},{d[4]},{d[5]}$ y $F3 = {f[2]:.0f} \\text{{ N}} localizado en {d[6]},{d[7]},{d[8]}$",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        ayuda1 = A43,
        ayuda2 = A45,
        ayuda3 = A46,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x + F3_x = F1*\\dfrac{{X_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{X_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{X_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}} = {f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y + F3_y = F1*\\dfrac{{Y_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Y_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Y_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z + F3_z = F1*\\dfrac{{Z_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Z_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Z_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = ({f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) i + ({f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) j + ({f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) k.
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1230051,
        no_pregunta = 5,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante (FR) entre los vectores que inician en el origen: $F1 = {f[0]:.0f} \\text{{ N}} localizado en {d[0]},{d[1]},{d[2]}$, $F2 = {f[1]:.0f} \\text{{ N}} localizado en {d[3]},{d[4]},{d[5]}$ y $F3 = {f[2]:.0f} \\text{{ N}} localizado en {d[6]},{d[7]},{d[8]} $.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        ayuda1 = A36,
        ayuda2 = A40,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x + F3_x = F1*\\dfrac{{X_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{X_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{X_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}} = {f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y + F3_y = F1*\\dfrac{{Y_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Y_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Y_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z + F3_z = F1*\\dfrac{{Z_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Z_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Z_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = ({f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) i + ({f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) j + ({f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) k.
       
        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario     ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil       ---------------------------------------------------
    #-------------------------------------------------     Code: 131##        ---------------------------------------------------

    Questionary(#1_1
        code = 1310011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: calc['cos1'],
        answer2 = lambda f, a, calc, c, d, m: calc['sin1'],
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El coseno del ángulo con respecto al eje X es ${calc['cos1']:.2f}$, y con respecto al eje Y es ${calc['sin1']:.2f}$. Note el signo; ¿qué quiere decir?",   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#1_2
        code = 1310012,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos2'],
        answer2=lambda f, a, calc, c, d, m: calc['sin2'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1=A47,
        ayuda2= A1,
        ayuda3= A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El coseno del ángulo con respecto al eje X es ${calc['cos2']:.2f}$, y con respecto al eje Y es ${calc['sin2']:.2f}$. Note el signo; ¿qué quiere decir?",   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_3
        code = 1310013,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos3'],
        answer2=lambda f, a, calc, c, d, m: calc['sin3'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El coseno del ángulo con respecto al eje X es ${calc['cos3']:.2f}$, y con respecto al eje Y es ${calc['sin3']:.2f}$. Note el signo; ¿qué quiere decir?",   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_4
        code = 1310014,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos4'],
        answer2=lambda f, a, calc, c, d, m: calc['sin4'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El coseno del ángulo con respecto al eje X es ${calc['cos4']:.2f}$, y con respecto al eje Y es ${calc['sin4']:.2f}$. Note el signo, ¿qué quiere decir?",   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1310021,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag1_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A49,
        ayuda2 = A50,
        ayuda3 = A51,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[0]:.0f}{{\\text{{°) = }}}}{calc['cos1']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{90-a[0]:.0f}{{\\text{{°) = }}}}{calc['sin1']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag1_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos1']:.2f} i + {calc['sin1']:.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_2
        code = 1310022,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag2_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1="En un triángulo con un ángulo recto, de lados a y b, la longitud de la hipotenusa se calcula como: $\\sqrt{a^2+b^2}$",
        ayuda2= "Considere que a y b corresponden a los cosenos direccionales",
        ayuda3= "La norma será: $|u| = \\sqrt{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}$.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[1]:.0f}{{\\text{{°) = }}}}{calc['cos2']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[1]-90:.0f}{{\\text{{°) = }}}}{calc['sin2']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag2_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos2']:.2f} i + {calc['sin2']:.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_3
        code = 1310023,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag3_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1=A49,
        ayuda2=A50,
        ayuda3=A51,
        respuesta_P1=lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[2]:.0f}{{\\text{{°) = }}}}{calc['cos3']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[2]-90:.0f}{{\\text{{°) = }}}}{calc['sin3']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag3_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos3']:.2f} i {calc['sin3']:.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_4
        code = 1310024,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag4_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A49,
        ayuda2 = A50,
        ayuda3 = A51,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[3]:.0f}{{\\text{{°) = }}}}{calc['cos4']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[3]-90:.0f}{{\\text{{°) = }}}}{calc['sin4']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag4_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos4']:.2f} i {calc['sin4']:.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1310031,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector F1 definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A son ({c[0]:.0f} , {c[1]:.0f}) y las del punto B son ({c[3]:.0f} , {c[4]:.0f}).",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A52,
        ayuda3 = A53,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[4]:.0f} {{\\text{{ - (}}}} {c[1]:.2f} {{\\text{{) = }}}} {c[4]-c[1]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   

        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[4]-c[1]:.0f}}} {{{math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[4]-c[1])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f} i + {(c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1310032,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector F1 definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A son ({c[3]:.0f} , {c[4]:.0f}) y las del punto B son ({c[0]:.0f} , {c[1]:.0f}).",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[0]:.0f} {{\\text{{ - (}}}} {c[3]:.2f} {{\\text{{) = }}}} {c[0]-c[3]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[0]-c[3]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[0]-c[3])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} i {(c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_3
        code = 1310033,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector F1 definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A son ({c[3]:.0f} , {c[1]:.0f}) y las del punto B son ({c[0]:.0f} , {c[4]:.0f}).",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[0]:.0f} {{\\text{{ - (}}}} {c[3]:.2f} {{\\text{{) = }}}} {c[0]-c[3]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[4]:.0f} {{\\text{{ - (}}}} {c[1]:.2f} {{\\text{{) = }}}} {c[4]-c[1]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[0]-c[3]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[0]-c[3])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[4]-c[1]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[4]-c[1])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} i + {(c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_4
        code = 1310034,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector F1 definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A son ({c[0]:.0f} , {c[4]:.0f}) y las del punto B son ({c[3]:.0f} , {c[1]:.0f}).",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} i {(c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} j$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_4
        code = 1310044,
        no_pregunta = 4,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el vector catersiano de $F1={f[0]} \\text{{  kN}}$ definido por los puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A son ({c[0]:.0f} , {c[4]:.0f}) y las del punto B son ({c[3]:.0f} , {c[1]:.0f}).",
        no_answers = 2,
        a1_name = "Componente en X $(i)$",
        a2_name = "Componente en Y $(j)$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]*((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))),2),
        answer2=lambda f, a, calc, c, d, m: np.round(f[0]*((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A54,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{dx^2 + dy^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de las componentes en X y Y:}}$

        ${{\hspace{{4mm}}\\text{{componente i = }} \\overrightarrow{{F1}}*\\dfrac{{dx}}{{AB}} \\text{{ = }}}} {f[0]:.0f}*{{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {f[0]*((c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f}$   
          
        ${{\hspace{{4mm}}\\text{{componente j = }} \\overrightarrow{{F1}}*\\dfrac{{dy}}{{AB}} \\text{{ = }}}} {f[0]:.0f}*{{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {f[0]*((c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f}$ 
        
        De acuerdo con lo anterior el vector cartesiano de $F1$ es = [{f[0]*((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))):.2f} i {f[0]*((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))):.2f} j]\\text{{ kN}}$.
        """,  
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",  
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1310051,
        no_pregunta = 5,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados del vector cartesiano $[({c[0]:.0f}) i + ({c[1]:.0f}) j + ({c[2]:.0f}) k] N$.",
        no_answers = 3,
        a1_name = "Ángulo respecto a X $(\\alpha)$ [°]",
        a2_name = "Ángulo respecto a Y $(\\beta)$ [°]",
        a3_name = "Ángulo respecto a Z $(\\gamma)$ [°]",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[0],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[1],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[2],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        ayuda1 = A42,
        ayuda2= A55,  
        ayuda3= A40,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la magnitud del vector cartesiano:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{F}}| = \\sqrt{{F_X^2 + F_Y^2 + F_Z^2}} = \\sqrt{{({c[0]})^2 + ({c[1]})^2 + ({c[2]})^2}} = {Calculations.magnitude3D(c[0],c[1],c[2]):.2f} \\text{{N}}}}$

        $\\textbf{{\\small 2. Cálculo de los ángulos:}}$

        Para el cálculo de los ángulos se determina el coseno inverso de cada una de las componentes del vector unitario en la dirección del vector $\\overrightarrow{{F}}$.

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[0],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[1],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[2],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario    ---------------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 132####    ---------------------------------------------------

    Questionary(#1_1
        code = 1320011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los cosenos direccionales de la fuerza F1, use el vector unitario. Considere $X_1={d[0]:0f}$ y $Y_1={d[3]:0f}$.",
        no_answers = 2,
        a1_name = CosX,
        a2_name = CosY,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: d[0]/Calculations.magnitude(d[0],d[3]),
        answer2=lambda f, a, calc, c, d, m: d[3]/Calculations.magnitude(d[0],d[3]),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A56,
        ayuda2 = A57,
        ayuda3 = A58,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Teniendo en cuenta que el vector unitario en el eje i o j es equivalente al coseno direccional en el mismo eje. Se calcula el vector unitario del vector F1:

        $\\textbf{{\\small 1. Cálculo del vector unitario:}}$

        ${{\hspace{{4mm}}|\\overrightarrow{{u}}| = \\dfrac{{(X_2-X_1) + (Y_2-Y_1)}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2}}}} = \\dfrac{{({d[0]:.0f}-0) i + ({d[3]:.0f}-0) j}}{{\\sqrt{{({d[0]:.0f}-0)^2 + ({d[3]:.0f}-0)^2}}}} }}$
    
        $\\textbf{{\\small 2. Cosenos direccionales de la fuerza F1:}}$
        
        ${{\hspace{{4mm}}|\\overrightarrow{{u_x}}| = cos(\\theta_x) = \\dfrac{{({d[0]:.0f}-0)}}{{\\sqrt{{({d[0]:.0f}-0)^2 + ({d[3]:.0f}-0)^2}}}}i = {d[0]/Calculations.magnitude(d[0],d[3]):.0f} i}}$
        ${{\hspace{{4mm}}|\\overrightarrow{{u_y}}| = cos(\\theta_y) = \\dfrac{{({d[3]:.0f}-0)}}{{\\sqrt{{({d[0]:.0f}-0)^2 + ({d[3]:.0f}-0)^2}}}}j = {d[3]/Calculations.magnitude(d[0],d[3]):.0f} j}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 1320021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza resultante del siguiente sistema de vectores, use el vector unitario. Considere $F1={f[0]:0f}$ kN, $F2={f[1]:0f}$ kN, $F3={f[2]:0f}$ kN, $F4={f[3]:0f}$ kN, $X_1={d[0]:0f}$, $Y_1={d[3]:0f}$, $X_2={d[6]:0f}$ y $Y_2={d[9]:0f}$.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A59,
        ayuda2 = A57,
        ayuda3 = A15,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x + F3_x + F4_x}}$
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = -F1 \\cdot \\dfrac{{(X1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(X2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} + F3}} }}$
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = {-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2]:.0f} }}$

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_y + F2_y + F3_y + F4_y}}$
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = -F1 \\cdot \\dfrac{{(Y1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(Y2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} - F4}} }}$
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = {-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]:.0f} }}$

       
        $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1320031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el vector unitario del cable AD, evaluado desde A hacia D. Considere que $D_X={d[0]:0f}$, $D_Y={d[3]:0f}$ y $A_Z={d[6]:0f}$.",
        no_answers = 2,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1=lambda f, a, calc, c, d, m: np.round(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        answer3=lambda f, a, calc, c, d, m: np.round(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        ayuda1 = A57,
        ayuda2 = A60,
        ayuda3 = A61,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la componente X $i$ del vector unitario:}}$

        ${{\hspace{{4mm}} u_x = \\dfrac{{-D_X-0}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$
        ${{\hspace{{4mm}} u_x = {d[0]/Calculations.magnitude3D(d[0],d[3],d[6]):.0f}}}
        
        $\\textbf{{\\small 2. Cálculo de la componente Y $j$ del vector unitario:}}$

        ${{\hspace{{4mm}} u_y = \\dfrac{{D_Y-0}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$
        ${{\hspace{{4mm}} u_y = {d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.0f}}}
       
        $\\textbf{{\\small 3. Cálculo de la componente Z $k$ del vector unitario:}}$

        ${{\hspace{{4mm}} u_z = \\dfrac{{0-A_Z}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$
        ${{\hspace{{4mm}} u_z = {d[6]/Calculations.magnitude3D(d[0],d[3],d[6]):.0f} }}
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
 
    Questionary(#4_1
        code = 1320041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La componente en Y del vector unitario del cable AD, evaluado desde A hacia D, es {calc['cos1']:.0f}. ¿Cuál es la distancia D_Y si $D_X={d[0]:0f}$ y $A_Z={d[3]:0f}?. Además, ¿cuál es la componente en Y de la fuerza, si la fuerza a lo largo del cable es {f[0]:.0f} kN$.",
        no_answers = 2,
        a1_name = "Distancia $D_Y$",
        a2_name = "Componente en y ($F_y$)",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt((d[0]**2+d[3]**2)/((1/(calc['cos1'])**2)-1)),2),
        answer2=lambda f, a, calc, c, d, m: np.round(calc['cos1']*f[0],2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A65,
        ayuda2 = "Despeje la distancia $D_Y$.",
        ayuda3 = A66,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Despeje de la distancia $D_Y$:}}$

        Para despejar la distancia $D_Y$ se plantea la ecuación de la componente Y $j$ del vector unitario:

        ${{\hspace{{4mm}} \\lambda_u_y = \\dfrac{{D_Y}}{{\\sqrt{{(D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$
        ${{\hspace{{4mm}} \\sqrt{{(D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} = \\dfrac{{D_Y}}{{\\lambda_u_y}} }}$
        ${{\hspace{{4mm}} (D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2 = \\left(\\dfrac{{D_Y}}{{\\lambda_u_y}}\\right)^2 }}$
        ${{\hspace{{4mm}} (D_X-0)^2 + (0-A_Z)^2 = \\left(\\dfrac{{D_Y}}{{\\lambda_u_y}}\\right)^2 - (D_Y-0)^2}}$
        ${{\hspace{{4mm}} (D_X-0)^2 + (0-A_Z)^2 = (D_Y-0)^2*\\left(\\dfrac{{1}}{{(\\lambda_u_y)^2}}-1\\right)}}$
        ${{\hspace{{4mm}} D_Y = \\sqrt{{\\left(\\dfrac{{D_X^2+A_Z^2}}{{\\left(\\dfrac{{1}}{{(\\lambda_u_y)^2}}-1}}\\right)}} }}$
        ${{\hspace{{4mm}} D_Y = {math.sqrt((d[0]**2+d[3]**2)/((1/(calc['cos1'])**2)-1)):.2f}}}$
        
        $\\textbf{{\\small 2. Cálculo de la componente Y $j$ de la fuerza que actúa en el cable AD:}}$

        ${{\hspace{{4mm}} F_y = F*\\lambda_u_y }}$
        ${{\hspace{{4mm}} u_y = {calc['cos1']*f[0]:.2f}}}        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1 
        code = 1320051, 
        no_pregunta = 5, 
        complexity = M, 
        topic = EQ, 
        subtopic = VU, 
        version = 1, 
        pregunta = lambda f, a, calc, c, d, m: f"Halle el vector cartesiano de la fuerza resultante (FR) entre los vectores que inician en el origen:  $F1 = {f[0]:.0f} \\text{{ N}} localizado en {c[0]},{c[1]},{c[2]}$ y $F2 = {f[1]:.0f} \\text{{ N}} localizado en {c[3]},{c[4]},{c[5]}$.", 
        no_answers = 3, 
        a1_name = Ci, 
        a2_name = Cj, 
        a3_name = Ck, 
        answer1=lambda f, a, calc, c, d, m: np.round((c[0]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        answer2=lambda f, a, calc, c, d, m: np.round((c[1]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        answer3=lambda f, a, calc, c, d, m: np.round((c[2]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        ayuda1 = A62, 
        ayuda2 = A63, 
        ayuda3 = A57, 
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo del vector cartesiano de las fuerzas F1 y F2:}}$

        $\\underline{{Vector cartesiano F1}}$ 

        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = \\dfrac{{(X_2-X_1) i + (Y_2-Y_1) j + (Z_2-Z_1) k}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2 + (Z_2-Z_1)^2}} }} }}$
        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = \\dfrac{{({c[0]:.0f}-0) i + ({c[1]:.0f}-0) j + ({c[2]:.0f}-0) k}}{{\\sqrt{{({c[0]:.0f}-0)^2 + ({c[1]:.0f}-0)^2 + ({c[2]:.0f}-0)^2}} }} }}$
        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = {c[0]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} i + {c[1]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} j + {c[2]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} k}}$

        $\\underline{{Vector cartesiano F2}}$ 

        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = \\dfrac{{(X_2-X_1) i + (Y_2-Y_1) j + (Z_2-Z_1) k}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2 + (Z_2-Z_1)^2}} }} }}$
        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = \\dfrac{{({c[3]:.0f}-0) i + ({c[4]:.0f}-0) j + ({c[5]:.0f}-0) k}}{{\\sqrt{{({c[3]:.0f}-0)^2 + ({c[4]:.0f}-0)^2 + ({c[5]:.0f}-0)^2}} }} }}$
        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = {(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} i + {(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} j + {(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} k}}$

        $\\textbf{{\\small 2. Cálculo del vector cartesiano de la fuerza resultante $F_R$:}}$
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = F_R_X i + F_R_Y j + F_R_Z k}}$
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = (F_1_X + F_2_X) i + (F_1_Y + F_2_Y) j + (F_1_Z + F_2_Z) k}}$
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = ({c[0]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) i + ({c[1]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} ) j + ({c[2]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) k}}$
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = {(c[0]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} i + {(c[1]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} j + {(c[2]/Calculations.magnitude3D(c[0],c[1],c[2]))+(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} k}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"", 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations' 
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario     ---------------------------------------------------
    #-------------------------------------------------       Nivel díficil      ---------------------------------------------------
    #-------------------------------------------------       Code: 133##      ---------------------------------------------------

    Questionary(#1_1
        code = 1330011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el vector cartesiano de la fuerza resultante ($F_R$) de las fuerzas que actuán en los cables mostrados en la figura. Considere que la fuerzas que actúan en los cables AB, AC y AD son: {f[0]:.0f} kN, {f[1]:.0f} kN y {f[2]:.0f} kN, respectivamente. También considere que $A_Z={d[0]:.0f}$, $B_X={d[3]:.0f}$, $B_Y={d[6]:.0f}$, $C_X={d[9]:.0f}$, $C_Y={d[12]:.0f}$, $D_X={d[15]:.0f}$ y $D_Y={d[18]:.0f}$.",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        ayuda1 = A64,
        ayuda2 = A62,
        ayuda3 = A63,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar el vector cartesiano de la fuerza resultante ($F_R$), se realiza la sumatoria de las fuerzas en X, Y, Z, para lo cual se usa el vector unitario de cada uno de los cables.

        $\\textbf{{\\small 1. Cálculo del vector unitario de los cables AB, AC y AD (Evaluados desde A a los puntos B, C, D):}}$

        ${{\hspace{{4mm}} \\Lambda_{{AB}} = \\dfrac{{\\overrightarrow{{AB}}}}{{|\\overrightarrow{{AB}}|}} = \\dfrac{{(B_X-0) i + (-B_Y-0) j + (0 - A_Z) k}}{{\\sqrt((B_X-0)^2 + (-B_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AC}} = \\dfrac{{\\overrightarrow{{AC}}}}{{|\\overrightarrow{{AC}}|}} = \\dfrac{{(C_X-0) i + (C_Y-0) j + (0 - A_Z) k}}{{\\sqrt((C_X-0)^2 + (C_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AD}} = \\dfrac{{\\overrightarrow{{AD}}}}{{|\\overrightarrow{{AD}}|}} = \\dfrac{{(-D_X-0) i + (D_Y-0) j + (0 - A_Z) k}}{{\\sqrt((-D_X-0)^2 + (D_Y-0)^2 + (0 - A_Z)^2}} }}$
    
        
        $\\textbf{{\\small 2. Sumatoria de fuerzas en X, Y, Z:}}$

        ${{\hspace{{4mm}} \\sum_X = F_R_X = F_{{AB}}*\\left(\\dfrac{{B_X}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_X}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-D_X}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} }}$
        
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = F_{{AB}}*\\left(\\dfrac{{-B_Y}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_Y}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{D_Y}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = F_{{AB}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z ={f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        
        De acuerdo con el anterior procedimiento el vector cartesiano de la fuerza resultante ($F_R$) es: {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} i + {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} j + {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} k. 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 1330021,
        no_pregunta = 2,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados de la fuerza resultante ($F_R$) de las fuerzas que actuán en los cables mostrados en la figura. Considere que la fuerzas que actúan en los cables AB, AC y AD son: {f[0]:.0f} kN, {f[1]:.0f} kN y {f[2]:.0f} kN, respectivamente. También considere que $A_Z={d[0]:.0f}$, $B_X={d[3]:.0f}$, $B_Y={d[6]:.0f}$, $C_X={d[9]:.0f}$, $C_Y={d[12]:.0f}$, $D_X={d[15]:.0f}$ y $D_Y={d[18]:.0f}$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        ayuda1 = A36,
        ayuda2 = A62,
        ayuda3 = A57,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar los ángulos directores coordeados, primero se halla el vector cartesiano de la fuerza resultante ($F_R$) y su magnitud. Luego, se calculan los arcocosenos de las componentes del vector divididas entre su magnitud:

        $\\textbf{{\\small 1. Cálculo del vector unitario de los cables AB, AC y AD (Evaluados desde A a los puntos B, C, D):}}$

        ${{\hspace{{4mm}} \\Lambda_{{AB}} = \\dfrac{{\\overrightarrow{{AB}}}}{{|\\overrightarrow{{AB}}|}} = \\dfrac{{(B_X-0) i + (-B_Y-0) j + (0 - A_Z) k}}{{\\sqrt((B_X-0)^2 + (-B_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AC}} = \\dfrac{{\\overrightarrow{{AC}}}}{{|\\overrightarrow{{AC}}|}} = \\dfrac{{(C_X-0) i + (C_Y-0) j + (0 - A_Z) k}}{{\\sqrt((C_X-0)^2 + (C_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AD}} = \\dfrac{{\\overrightarrow{{AD}}}}{{|\\overrightarrow{{AD}}|}} = \\dfrac{{(-D_X-0) i + (D_Y-0) j + (0 - A_Z) k}}{{\\sqrt((-D_X-0)^2 + (D_Y-0)^2 + (0 - A_Z)^2}} }}$
    
        
        $\\textbf{{\\small 2. Sumatoria de fuerzas en X, Y, Z:}}$

        ${{\hspace{{4mm}} \\sum_X = F_R_X = F_{{AB}}*\\left(\\dfrac{{B_X}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_X}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-D_X}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} }}$
        
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = F_{{AB}}*\\left(\\dfrac{{-B_Y}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_Y}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{D_Y}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = F_{{AB}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z ={f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        
        De acuerdo con el anterior procedimiento el vector cartesiano de la fuerza resultante ($F_R$) es: {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} i + {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} j + {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} k. 
        
        $\\textbf{{\\small 3. Calcular los ángulos con respecto a X, Y, Z:}}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_X}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = cos^{-1}\\left(\\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = {Calculations.arccosine(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f}}}$
        
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_Y}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = cos^{-1}\\left(\\dfrac{{{f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = {Calculations.arccosine(f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f} }}$

        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_Z}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = cos^{-1}\\left(\\dfrac{{{f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = {Calculations.arccosine(f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1330031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"En el cable AD actúa una fuerza de {f[0]:.0f} N. Si la longitud del cable es {Calculations.magnitude3D(d[0],d[3],d[6]):.2f} m, $A_Z = {d[6]:.0f}$ y la componente $y$ de la fuerza es $F_y = {f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}$ N. Determine la distancia $D_X$ y $D_Y$.",
        no_answers = 2,
        a1_name = "Distancia $D_X$",
        a2_name = "Distancia $D_Y$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: d[0],
        answer2 = lambda f, a, calc, c, d, m: d[3],
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A66,
        ayuda2 = "Despeje de la anterior ecuación la distancia en Y ($D_Y$)",
        ayuda3 = "Para hallar la distancia en X ($D_X$) plantee la ecuación de la longitud del cable y despeje. ¿Qué representa la longitud del cable?.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar las distancias $D_X$ y $D_Y$, primero se plantea la ecuación de la componente $y$ de la fuerza y a partir de ella se despeja la distancia en $y$. Luego se plantea la ecuación de la longitud de la cuerda y se despeja la distancia en $x$.
        
        $\\textbf{{\\small 1. Despeje de la distancia $D_Y$:}}$

        ${{\hspace{{4mm}} F_y = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{\\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{Longitud del cable}} }}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{F_y*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Y = {d[3]:.0f}}}$

        $\\textbf{{\\small 2. Despeje de la distancia $D_X$:}}$
        
        ${{\hspace{{4mm}} \\text{{Longitud de la cuerda}} = \\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}}$
        ${{\hspace{{4mm}} (\\text{{Longitud de la cuerda}})^2 = (-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}$
        ${{\hspace{{4mm}} (\\text{{Longitud de la cuerda}})^2 - (D_Y)^2 - (-A_Z)^2= (-D_X)^2}}$
        ${{\hspace{{4mm}} D_X = \\sqrt{{\\text{{Longitud de la cuerda}}-- (D_Y)^2 - (-A_Z)^2}}}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#4_1
        code = 1330041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere una cuerda en la que actúa una fuerza $\\overrightarrow{{F}}$ = ({f[0]*d[0]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f} i + {f[0]*d[3]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f} j + {f[0]*d[6]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f}) k N  con origen en 0 i + 0 j + 0 k. Si la longitud de la cuerda es {Calculations.magnitude3D(d[0],d[3],d[6]):.2f} determine las distancias en X, Y y Z de la cuerda.",
        no_answers = 2,
        a1_name = "Distancia en X ($D_X$)",
        a2_name = "Distancia en Y ($D_Y$)",
        a3_name = "Distancia en Z ($D_Z$)",
        answer1 = lambda f, a, calc, c, d, m: d[0],
        answer2 = lambda f, a, calc, c, d, m: d[3],
        answer3 = lambda f, a, calc, c, d, m: d[6],
        ayuda1 = A67,
        ayuda2 = A68,
        ayuda3 = A69,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar las distancias en X, Y y Z, se plantean las ecuaciones de cada una de las componentes de la fuerza como la multiplicación de la magnitud de la fuerza y el vector unitario en dicha componente.
        
        $\\textbf{{\\small 1. Despeje de la distancia en X ($D_X$):}}$

        ${{\hspace{{4mm}} F_x = |\\overrightarrow{{F}}|*dfrac{{D_X}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_X}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_X = \\dfrac{{F_x*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_X = \\dfrac{{{f[0]*d[0]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_X = {d[0]:.0f} }}$

        $\\textbf{{\\small 2. Despeje de la distancia en Y ($D_Y$):}}$

        ${{\hspace{{4mm}} F_y = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{F_y*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Y = {d[3]:.0f} }}$

        $\\textbf{{\\small 1. Despeje de la distancia en Z ($D_Z$):}}$

        ${{\hspace{{4mm}} F_z = |\\overrightarrow{{F}}|*dfrac{{D_Z}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Z}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_Z = \\dfrac{{F_x*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Z = \\dfrac{{{f[0]*d[6]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Z = {d[6]:.0f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Equilibrio 2D      ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil      ---------------------------------------------------
    #-------------------------------------------------       Code: 141##      ---------------------------------------------------

    Questionary(#1_1
        code = 1410011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de las fuerzas F1 y F2 para que la partícula esté en equilibrio. Considere $F3 = {f[0]:.0f} \\text{{kN}}$, $\\alpha_1={a[0]:.0f}$ y $\\alpha_2={a[4]:.0f}$.",
        no_answers = 2,
        a1_name = "Magnitud F1 [kN]",
        a2_name = "Magnitud F2 [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((-(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1']+f[0])/calc['cos5']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5'])),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A70,
        ayuda2 = A71,
        ayuda3 = A72,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
         Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        $\\underline{{Ecuación 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3= -F1*cos(\\alpha_2) - F2*cos(\\alpha_1) +F3 = 0}}$

        $\\underline{{Ecuación 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = F1*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        

        $\\textbf{{\\small 2. Despejar las magnitudes:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anteior, se despeja F1 de la Ecuación 1 y se reemplaza en la Ecuación 2 para despejar F2. Con el valor de F2 obtenido, se halla F1.

        De la ecuación 1 se despeja F1:  

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}}}$

        Se reemplaza F1 en la ecuación 2:

        ${{\hspace{{4mm}} \\left(\\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        ${{\hspace{{4mm}} -F2*cos(\\alpha_1)*tan(\\alpha_2) + F3*tan(\\alpha_2) - F2*sen(\\alpha_1) = 0}}$
        ${{\hspace{{4mm}} F3*tan(\\alpha_2) = F2*sen(\\alpha_1) + F2*cos(\\alpha_1)*tan(\\alpha_2)}}$
        ${{\hspace{{4mm}} F3*tan(\\alpha_2) = F2(sen(\\alpha_1) + cos(\\alpha_1)*tan(\\alpha_2))}}$  
        ${{\hspace{{4mm}} F2 = \\dfrac{{F3*tan(\\alpha_2)}}{{sen(\\alpha_1) + cos(\\alpha_1)*tan(\\alpha_2)}}}}$ 
        ${{\hspace{{4mm}} F2 = {(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5'])):.2f}}} \\text{{kN}}$

        Con el valor de F2 se calcula F1:  
        ${{\hspace{{4mm}} F1 = {((-(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1']+f[0])/calc['cos5']):.2f}}} \\text{{kN}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#2_1
        code = 1410021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de la F1 y el ángulo $\\alpha_2$ para que la partícula esté en equilibrio. Considere $F2 = {f[0]:.0f} \\text{{kN}}$, $F3 = {f[1]:.0f} \\text{{kN}}$ y $\\alpha_1={a[0]:.0f}$.",
        no_answers = 2,
        a1_name = "Magnitud F1 [kN]",
        a2_name = "Ángulo $\\alpha_2$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-f[0]*calc['cos1']+f[1])/Calculations.cosine(Calculations.define_angle((f[0]*calc['sin1']),(-f[0]*calc['cos1']+f[1]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((Calculations.define_angle((f[0]*calc['sin1']),(-f[0]*calc['cos1']+f[1]))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A70,
        ayuda2 = A71,
        ayuda3 = A72,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        $\\underline{{Ecuación 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3= -F1*cos(\\alpha_2) - F2*cos(\\alpha_1) +F3 = 0}}$

        $\\underline{{Ecuación 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = F1*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        

        $\\textbf{{\\small 2. Despeje de la magnitud de F1 y el ángulo $\\alpha_2$:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anteior, se despeja F1 de la Ecuación 1 y se reemplaza en la Ecuación 2 para despejar el ángulo $\\alpha_2$. Con el valor de $\\alpha_2$ obtenido, se halla F1.

        De la ecuación 1 se despeja F1:  

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}}}$

        Se reemplaza F1 en la ecuación 2:

        ${{\hspace{{4mm}} \\left(\\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        ${{\hspace{{4mm}} -F2*cos(\\alpha_1)*tan(\\alpha_2) + F3*tan(\\alpha_2) - F2*sen(\\alpha_1) = 0}}$
        ${{\hspace{{4mm}} tan(\\alpha_2)(-F2*cos(\\alpha_1) + F3) = F2*sen(\\alpha_1)}}$
        ${{\hspace{{4mm}} tan(\\alpha_2) = \\dfrac{{F2*sen(\\alpha_1)}}{{-F2*cos(\\alpha_1) + F3}}}}$
        ${{\hspace{{4mm}} \\alpha_2 = tan^{{-1}}\\left(\\dfrac{{F2*sen(\\alpha_1)}}{{-F2*cos(\\alpha_1) + F3}}\\right)}}$
        ${{\hspace{{4mm}} \\alpha_2 = {Calculations.define_angle((f[0]*calc['sin1']),(-f[0]*calc['cos1']+f[1])):.2f}}}$

        Con el valor de F2 se calcula F1:  
        ${{\hspace{{4mm}} F1 = {(-f[0]*calc['cos1']+f[1])/Calculations.cosine(Calculations.define_angle((f[0]*calc['sin1']),(-f[0]*calc['cos1']+f[1]))):.2f}}} \\text{{kN}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  

    Questionary(#3_1
        code = 1410031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de F para el siguiente sistema. Considere $W = {f[0]:.0f} N$.",
        no_answers = 2,
        a1_name = "Fuerza F [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]/2,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A73,
        ayuda2 = A74,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m: T3,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = W - 2F = 0}}$ 
        ${{\hspace{{4mm}} 2F = W}}$ 
        ${{\hspace{{4mm}} F = \\dfrac{{W}}{{2}}}}$ 
        ${{\hspace{{4mm}} F = {f[0]/2:.2f}}} N$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#4_1
        code = 1410041,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la fuerza de fricción necesaria para evitar que el bloque de peso $W={f[0]:.2f}$ N se desplace a lo largo del plano inclinado a {a[0]:.0f}° de la horizontal.",
        no_answers = 2,
        a1_name = "Fuerza de fricción ($f_r$) [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Defina un sistema de coordenadas arbitrario, donde el eje X' sea paralelo al plano inclinado y el eje Y' esté a 90° con respecto a la superficie del plano.",
        ayuda2 = A76,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Diagrama de cuerpo libre de la polea y sistema de coordenadas arbitrario:}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = f_r - W*sen(\\alpha_1) = 0}}$ 
        ${{\hspace{{4mm}} f_r = W*sen(\\alpha_1)}}$ 
        ${{\hspace{{4mm}} F = {f[0]*calc['sin1']:.2f}}} N$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  
    
    Questionary(#5_1
        code = 1410051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere una partícula sobre la que actúan las fuerzas $F_1=[({c[0]:.0f}) i + ({c[1]:.0f}) j] N$ y $F_2=[({c[2]:.0f}) i + ({c[3]:.0f}) j] N$. Determine el vector cartesiano de la fuerza que debe aplicarse para que la partícula esté en equilibrio.",
        no_answers = 2,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(-(c[0]+c[2]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(-(c[1]+c[3]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A71,
        ayuda2 = A77,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0}}$
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3_x}}$
        ${{\hspace{{4mm}} F3_x = -F1_x - F2_x }}$
        ${{\hspace{{4mm}} F3_x = {-(c[0]+c[2]):.2f}}} \\text{{N}}$  
       
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y + F3_y}}$
        ${{\hspace{{4mm}} F3_y = -F1_y - F2_y }}$
        ${{\hspace{{4mm}} F3_x = {-(c[1]+c[3]):.2f}}} \\text{{N}}$

        De acuerdo con lo anterior, el vector cartesiano de la fuerza que debe aplicar es ({-(c[0]+c[2]):.2f} i + {-(c[1]+c[3]):.2f} j) N.
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Equilibrio 2D      ---------------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 142##      ---------------------------------------------------

    Questionary(#1_1
        code = 1420011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de F para el siguiente sistema. Considere $W = {f[0]:.0f} N$",
        no_answers = 2,
        a1_name = "Fuerza F [N]",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]/8,2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A78,
        ayuda2 = A74,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m:T3, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Equilibrio en la polea 1:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_1 - W = 0}}$ 
        ${{\hspace{{4mm}} 2T_1 = W}}$ 
        ${{\hspace{{4mm}} T_1 = \\dfrac{{W}}{{2}}}}$ 
        ${{\hspace{{4mm}} F = {f[0]/2:.2f}}} N$ 

        $\\textbf{{\\small 3. Equilibrio en la polea 2:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_2 - T_1 = 0}}$ 
        ${{\hspace{{4mm}} 2T_2 = T_1}}$ 
        ${{\hspace{{4mm}} T_2 = \\dfrac{{T_1}}{{2}}}}$ 
        ${{\hspace{{4mm}} T_2 = \\dfrac{{W}}{{4}}}}$ 
        ${{\hspace{{4mm}} F = {f[0]/4:.2f}}} N$ 

        $\\textbf{{\\small 4. Equilibrio en la polea 3:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_3 - T_2 = 0}}$ 
        ${{\hspace{{4mm}} 2T_3 = T_2}}$ 
        ${{\hspace{{4mm}} T_3 = \\dfrac{{T_2}}{{2}}}}$ 
        ${{\hspace{{4mm}} T_3 = \\dfrac{{W}}{{8}}}}$ 
        ${{\hspace{{4mm}} F = {f[0]/8:.2f}}} N$ 

        $\\textbf{{\\small 5. Definición de la fuerza F:}}$

        Dado que la cuerda en la que actúa la tensión $T_3$ es la misma en la que actúa F, la fuerza F es equivalente a $T_3$, es decir, {f[0]/8:.0f} N.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    #========================================================MOMENTO============================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel fácil      ---------------------------------------------------
    #-------------------------------------------------       Code: 21100##    ---------------------------------------------------

    Questionary(#1_1
        code = 2110011,
        no_pregunta = 1,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de la fuerza F1 y F2. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Momento en A de la fuerza F1 [$lb \\cdot ft$]",
        a2_name = "Momento en A de la fuerza F2 [$lb \\cdot ft$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['sin1']*(d[0]+d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$    

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        En este caso los vectores posición solo tiene componente en X y es igual a la magnitud de las distancias de A al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}}}}$     

        Ahora solo es necesario operar utilizando la ecuación de momento segun las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Teniendo en cuenta que el vector posición y la fuerza F1 ya son perpendiculares entre sí, y que, por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Podemos evaluar de la siguiente manera: 

        ${{\hspace{{4mm}} M1 = - |\\overrightarrow{{r1}}| \\cdot |\\overrightarrow{{F1}}| = -{d[0]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb }}}}}}$     
        ${{\hspace{{4mm}} M1 = {-f[0]*d[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$     

        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_y4, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2 = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = -r2 \\cdot\\hspace{{1mm}} F2_y = - {(d[3]+d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M2 = {-(f[1]*calc['sin1']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ft}}}}}}$  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#1_2 

        code = 2110012, 
        no_pregunta = 1, 
        complexity = F, 
        topic = MO, 
        subtopic = M2D, 
        version = 2, 
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de la fuerza F1 y F2. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.", 
        no_answers = 2, 
        a1_name = "Momento en A de la fuerza F1 [$lb \\cdot ft$]", 
        a2_name = "Momento en A de la fuerza F2 [$lb \\cdot ft$]", 
        a3_name = "", 
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[0],2), 
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*(4/5)*(d[0]+d[3]),2), 
        answer3 = lambda f, a, calc, c, d, m: 0, 
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.", 
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",       
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.", 
        respuesta_P1 = lambda f, a, calc, c, d, m: f""" 
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Decomposición de las fuerzas F1 y F2:}}$ 

        $\\underline{{Fuerza  \\hspace{{2mm}} F1: }}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud.  

        $\\underline{{Fuerza  \\hspace{{2mm}} F2: }}$    

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\frac{3}{5} = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{(3/5):.2f} = {f[1]*(3/5):.2f}{{ \\text{{ lb}}}}}}$         
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\frac{4}{5} = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{(4/5):.2f} = {f[1]*(4/5):.2f}{{ \\text{{ lb}}}}}}$         

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        $\\underline{{Vector Posición \\hspace{{2mm}} r1: }}$ 

        ${{\hspace{{4mm}} r1_x =  X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$         
        ${{\hspace{{4mm}} r1_y =  x_3 = {d[6]:.0f}{{ \\text{{ ft}}}}}}$         
        
        $\\underline{{Vector Posición \\hspace{{2mm}} r2: }}$         

        En este caso el vector posición $\\overrightarrow{{r2}}$ solo tiene componente en X y es igual a la magnitud de la distancia de A al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r2 = X_1 + X_2 ={d[0]+d[3]:.0f}{{ \\text{{ ft}}}}}}$     

        Ahora solo es necesario operar utilizando la ecuación de momento segun las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Se tiene en cuenta $r1_x$ al ser perpendicular a la fuerza F1, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos evaluar de la siguiente manera: 

        ${{\hspace{{4mm}} M1 = -|\\overrightarrow{{r1}}| \\cdot |\\overrightarrow{{F1}}| = -{d[0]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb }}}}}}$       
        ${{\hspace{{4mm}} M1 = {-f[0]*d[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$ 

        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2 = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = -r2 \\cdot\\hspace{{1mm}} F2_y = -{(d[3]+d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*(4/5):.2f}{{\\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} M2 ={-(f[1]*(4/5)*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$ 
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"", 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations' 

        ), 
   
    Questionary(#1_3 
        code = 2110013, 
        no_pregunta = 1, 
        complexity = F, 
        topic = MO, 
        subtopic = M2D, 
        version = 3, 
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de la fuerza F1 y F2. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.", 
        no_answers = 2, 
        a1_name = "Momento en A de la fuerza F1 [$lb \\cdot ft$]", 
        a2_name = "Momento en A de la fuerza F2 [$lb \\cdot ft$]", 
        a3_name = "", 
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*d[6],2), 
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['sin1']*(d[0]),2), 
        answer3 = lambda f, a, calc, c, d, m: 0, 
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.", 
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",       
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.", 
        respuesta_P1 = lambda f, a, calc, c, d, m: f""" 
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Decomposición de las fuerzas F1 y F2:}}$ 

        $\\underline{{Fuerza \\hspace{{2mm}} F1: }}$ La fuerza F1 solo tiene componente en X y es igual a su magnitud.  

        $\\underline{{Fuerza \\hspace{{2mm}} F2: }}$    

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        $\\underline{{Vector Posición \\hspace{{2mm}} r1: }}$ 

        ${{\hspace{{4mm}} r1_x = X_1 + X_2 = {d[0]+d[3]:.0f}{{ \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} r1_y = x_3 = {d[6]:.0f}{{ \\text{{ ft}}}}}}$     

        $\\underline{{Vector Posición \\hspace{{2mm}} r2: }}$         

        En este caso el vector posición $\\overrightarrow{{r2}}$ solo tiene componente en X y es igual a la magnitud de la distancia de A al punto de acción de la fuerza. Considerando:         

        ${{\hspace{{4mm}} r2 = X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$       

        Ahora solo es necesario operar utilizando la ecuación de momento segun las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para la obtención de este momento vamos a tener solo en consideración $r1_y$, la cual es la componente perpendicular de la posición a la fuerza F1. Así mimsmo, por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos evaluar de la siguiente manera: 

        ${{\hspace{{4mm}} M1 = \\overrightarrow{{r1}} X \\overrightarrow{{F1}} = {d[6]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb.}}}}}}$       
        ${{\hspace{{4mm}} M1 = {f[0]*d[6]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft.}}}}}}$       

        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición r2 es $F2_y$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2 = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} =  -r2 \\cdot\\hspace{{1mm}} F2_y = {-(d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} M2 = {-(f[1]*calc['sin1']*(d[0])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$   
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"", 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations' 
        ),

    Questionary(#1_4 
        code = 12110014, 
        no_pregunta = 1, 
        complexity = F, 
        topic = MO, 
        subtopic = M2D, 
        version = 4, 
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto D de la fuerza F1 y F2. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.", 
        no_answers = 2, 
        a1_name = "Momento en D de la fuerza F1 [$lb \\cdot ft$]", 
        a2_name = "Momento en D de la fuerza F2 [$lb \\cdot ft$]", 
        a3_name = "", 
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*d[3],2), 
        answer2 = lambda f, a, calc, c, d, m: np.round(-((f[1]*calc['sin1']*(d[0]+d[6]))+(f[1]*calc['cos1']*d[3])),2), 
        answer3 = lambda f, a, calc, c, d, m: 0, 
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.", 
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",       
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.", 
        respuesta_P1 = lambda f, a, calc, c, d, m: f""" 
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Decomposición de las fuerzas F1 y F2:}}$ 

        $\\underline{{Fuerza \\hspace{{2mm}} F1: }}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud.  

        $\\underline{{Fuerza \\hspace{{2mm}} F2: }}$    

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$        
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$       

        $\\textbf{{\\small 2. Obtención del vector posición:}}$          

        $\\underline{{Vector Posición \\hspace{{2mm}} r1: }}$                 

        ${{\hspace{{4mm}} r1_x = X_2 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r1_y = x_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$      

        $\\underline{{Vector Posición \\hspace{{2mm}} r2: }}$            

        ${{\hspace{{4mm}} r2_x = X_2 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r2_y = x_1 + X_3 = {d[0] + d[6]:.0f}{{ \\text{{ ft}}}}}}$      

        Ahora solo es necesario operar utilizando la ecuación de momento según las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para la obtención de este momento vamos a tener solo en consideración $r1_x$, la cual es la componente perpendicular de la posición a la fuerza F1. Así mimsmo, por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos evaluar de la siguiente manera: 

        ${{\hspace{{4mm}} M1 = \\overrightarrow{{r1}} X \\overrightarrow{{F1}} = {d[6]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb }}}}}}$      
        ${{\hspace{{4mm}} M1 = {f[0]*d[3]:.2f}{{\\text{{ lb}} \\cdot\\text{{ft}}}}}}$      

        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        Para calcular el momento de la fuerza F2, vemos que podemos hacer la suma del momento en D que producen sus compenentes. Tal que: 

        $\\underline{{Momento \\hspace{{2mm}} F2_x: }}$        

        Con la componente en X de F2 es apreciable que la componente perpendicular del vector posicion seria $r2_y$. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento es negativo:          

        ${{\hspace{{4mm}} M2_1 = -r2_y \\cdot\\hspace{{1mm}} F2_x = - {(d[0]+d[6]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ lb}}}}}}$ 
        ${{\hspace{{4mm}} M2_1 = {-(f[1]*calc['sin1']*(d[0]+d[6])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$        

        $\\underline{{Momento \\hspace{{2mm}} F2_y: }}$ 

        Con la componente en Y de F2 es apreciable que la componente perpendicular del vector posicion seria $r2_x$. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento tambíen es negativo: 

        ${{\hspace{{4mm}} M2_2 = -r2_x \\cdot\\hspace{{1mm}} F2_y = -{(d[3]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} M2_2 = {-(f[1]*calc['cos1']*(d[3])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$       

        Finalmente el momento en el punto D de la fuerza F2 sería: 

        ${{\hspace{{4mm}} M2 = M2_1 + M2_2 = {(-f[1]*calc['sin1']*(d[0]+d[6])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft }}}}{(-f[1]*calc['cos1']*(d[3])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$       
        ${{\hspace{{4mm}} M2 = {-((f[1]*calc['sin1']*(d[0]+d[6]))+(f[1]*calc['cos1']*d[3])):.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$       
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"", 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations' 
        ), 

    Questionary(#2_1
        code = 2110021,
        no_pregunta = 2,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las fuerzas F1 y F2, si en el punto D: El momento de F1 debe ser de ${m[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$, y el momento de F2 debe ser de ${-m[1]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Fuerza F1 [lb]",
        a2_name = "Fuerza F2 [lb]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0])/(d[3]+d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(d[6]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular un momento en un punto en especifico, primero se obtiene las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, se identifica la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso los vectores posición solo tiene componente en X y es igual a la magnitud de las distancias de D al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r1 = X_2 + X_3 = {d[3] + d[6]:.0f}{{\\text{{ ft}}}}}}$       
        ${{\hspace{{4mm}} r2 = X_3 = {(d[6]):.0f}{{\\text{{ ft}}}}}}$      
        
        $\\textbf{{\\small 2. Descomposición de las fuerzas F1 y F2: }}$
       
        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1)}}$       
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1)}}$       
        
        $\\textbf{{\\small 3.1 Obtención de fuerza F1: }}$ 
        
        Definimos la ecuación de momento en D de la fuerza F1. También es necesario considerar que por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo, lo cual va acorde con el dato que nos dieron.
        
        ${{\hspace{{4mm}} M1_D  = \\overrightarrow{{r1}} X \\overrightarrow{{F1}} = |\\overrightarrow{{r1}}| \\cdot |\\overrightarrow{{F1}}|}}$     
        ${{\hspace{{4mm}} F1 = \\dfrac{{M1_D}}{{r}}}}$      
        ${{\hspace{{4mm}} F1 = ( \\dfrac{{{m[0]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[3]+d[6]:.0f}{{\\text{{ ft}}}}}} ) }}$      
        ${{\hspace{{4mm}} F1  = {(m[0])/(d[3]+d[6]):.2f}{{\\text{{ lb}}}}}}$      
        
        $\\textbf{{\\small 3.2 Obtención de fuerza F2: }}$ 
        
        Igual que con F1, definimos la ecuación de momento en D de la fuerza F2. También es necesario considerar que por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo, lo cual va acorde con el dato que nos dieron.
        
        ${{\hspace{{4mm}} M2_D  = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = |\\overrightarrow{{r2}}| \\cdot |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1)}}$      
        ${{\hspace{{4mm}} F2 = \\dfrac{{M2_D}}{{r2 \\cdot \\sin(\\alpha_1)}}}}$      
        ${{\hspace{{4mm}} F2 = -( \\dfrac{{{-m[1]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[6]*calc['sin1']:.2f}{{\\text{{ ft}}}}}} ) }}$      
        ${{\hspace{{4mm}} F2  = {(m[1])/(d[6]*calc['sin1']):.2f}{{\\text{{ lb}}}}}}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1610031,
        no_pregunta = 3,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto B de la fuerza F1 y F2, y el momento en C de la fuerza F2. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 3,
        a1_name = "Momento en B de la fuerza F1 [$lb \\cdot ft$]",
        a2_name = "Momento en B de la fuerza F2 [$lb \\cdot ft$]",
        a3_name = "Momento en C de la fuerza F2 [$lb \\cdot ft$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[3],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['cos1']*(d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-(f[1]*calc['cos1']*(d[0]+d[3])),2),
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 
        
        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$          
        
        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        En este caso los vectores posición solo tiene componente en X y es igual a la magnitud de las distancias desde el punto de consideración del momento al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r1_B = X_2 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r2_B = X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r2_C = X_1 + X_2 = {d[0] +d[3]:.0f}{{ \\text{{ ft}}}}}}$       

        Ahora solo es necesario operar utilizando la ecuación de momento segun las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento en B de la fuerza F1: }}$ 

        Teniendo en cuenta que el vector posición y la fuerza F1 ya son perpendiculares entre sí, y que, por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Podemos evaluar de la siguiente manera: 

        ${{\hspace{{4mm}} M1_B = -|\\overrightarrow{{r1_B}}| \\cdot |\\overrightarrow{{F1}}| = -{d[3]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} M1_B = {-f[0]*d[3]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$     

        $\\textbf{{\\small 3.2 Momento en B de la fuerza F2: }}$ 

        En el momento en B de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2_B = \\overrightarrow{{r2_B}} X \\overrightarrow{{F2}} = r2_B \\cdot\\hspace{{1mm}} F2_y = -{(d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M2_B = {-(f[1]*calc['cos1']*(d[0])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\textbf{{\\small 3.3 Momento en C de la fuerza F2: }}$
        De igual forma que en B, en el momento en C de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo. Tal que podemos considerar:  
        
        ${{\hspace{{4mm}} M2_C = \\overrightarrow{{r2_C}} X \\overrightarrow{{F2}} = r2_C \\cdot\\hspace{{1mm}} F2_y = -{(d[0]+d[3]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M2_C = {-(f[1]*calc['cos1']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        Igualmente, es importante aclarar que la fuerza F1 no genera momento en el punto C, dado que la linea de acción de esta fuerza corta o concuerda con el punto del cual estamos evaluando.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2110041,
        no_pregunta = 4,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza F1 y la distancia X1, si en el punto B: El momento de F1 debe ser de ${-m[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$, y el momento de F2 debe ser de ${-m[1]:.2f}{{\\text{{ ft}} \\cdot\\text{{ lb}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $F_2 = {f[1]:.0f} \\text{{ lb}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Fuerza F1 [lb]",
        a2_name = "Distancia X1 [ft]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((m[0])/d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(f[1]*calc['cos1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular un momento en un punto en especifico, primero se obtiene las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, se identifica la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para poder hallar la fuerza F1 vemos que esta se asocia a su propio momento que causa en B. Por otro lado, para obtener la distancia X1, vemos que esta asociada al momento de la fuerza F2. Tal que podremos seguir con la definición de momento:
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso los vectores posición solo tiene componente en X y es igual a la magnitud de las distancias de B al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r1 = X_2 = {d[3]:.0f}{{\\text{{ ft}}}}}}$ 
        ${{\hspace{{4mm}} r2 = X_1}}$
        
        $\\textbf{{\\small 2. Descomposición de las fuerzas F1 y F2: }}$
       
        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$     
        
        $\\textbf{{\\small 3.1 Obtención de fuerza F1: }}$ 
        
        Definimos la ecuación de momento en B de la fuerza F1. También es necesario considerar que por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo, lo cual va acorde con el dato que nos dieron.
        
        ${{\hspace{{4mm}} M1_B  = \\overrightarrow{{r1}} X \\overrightarrow{{F1}} = - |\\overrightarrow{{r1}}| \\cdot |\\overrightarrow{{F1}}| }}$      
        ${{\hspace{{4mm}} F1 = -\\dfrac{{M1_d}}{{r1}}}}$      
        ${{\hspace{{4mm}} F1 = -( \\dfrac{{{-m[0]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[3]:.0f}{{\\text{{ ft}}}}}} ) }}$     
        ${{\hspace{{4mm}} F1  = {(m[0])/d[3]:.2f}{{\\text{{ lb}}}}}}$     
        
        $\\textbf{{\\small 3.2 Obtención de fuerza F2: }}$ 
        
        Igual que con F1, definimos la ecuación de momento en B de la fuerza F2. También es necesario considerar que por la $\\textit{{Regla de la mano de derecha}}$ el momento es negativo, lo cual va acorde con el dato que nos dieron.
        
        ${{\hspace{{4mm}} M2_B  = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = - |\\overrightarrow{{r2}}| \\cdot |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1)}}$     
        ${{\hspace{{4mm}} X1 = r2 = - \\dfrac{{M2_B}}{{F2 \\cdot \\cos(\\alpha_1)}}}}$      
        ${{\hspace{{4mm}} X1 = -( \\dfrac{{{-m[1]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}} ) }}$     
        ${{\hspace{{4mm}} X1  = {(m[1])/(f[1]*calc['cos1']):.2f}{{\\text{{ ft}}}}}}$    
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    #=========================================================== Momento ========================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 2120011    ---------------------------------------------------

    Questionary(#1_1
        code = 2120011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de las tres fuerzas. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Momento en A de la fuerza F1 [$N \\cdot m$]",
        a2_name = "Momento en A de la fuerza F2 [$N \\cdot m$]",
        a3_name = "Momento en A de la fuerza F3 [$N \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(0,2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['sin1']*(d[0])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))),2),
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ N}}}}}}$     

        $\\underline{{Fuerza  \\hspace{{2mm}} F3 :}}$ 
        
        ${{\hspace{{4mm}} F3_x = |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[2]*calc['cos5']:.2f}{{ \\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} F3_y = |\\overrightarrow{{F3}}| \\cdot \\sin(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[2]*calc['sin5']:.2f}{{ \\text{{ N}}}}}}$     

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        $\\underline{{Vector Posición  \\hspace{{2mm}} r1: }}$ Desde aqui notamos como la linea de acción de la fuerza F1 conecta con el punto de evaluación tal que el Vector posición r1 seria igual a 0.

        $\\underline{{Vector Posición  \\hspace{{2mm}} r2: }}$         

        En este caso el vector posición $\\overrightarrow{{r2}}$ solo tiene componente en X y es igual a la magnitud de la distancia de A al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r2 =  X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        
        $\\underline{{Vector Posición \\hspace{{2mm}} r3: }}$ 

        ${{\hspace{{4mm}} r3_x = X_1 + X_2 \\cdot \\cos(\\beta) = {d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r3_y = x_2 \\cdot \\sin(\\beta) = {d[3]*calc['sin9']:.2f}{{ \\text{{ m}}}}}}$     

        Ahora solo es necesario operar utilizando la ecuación de momento segun las componentes necesarias y denotando el signo acorde a la $\\textit{{Regla de la mano de derecha}}$: 

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Como ya habiamos mencionado la fuerza F1 se ve aplicada directamente en A, tal que, por definición de momento, este sera igual a cero: 

        ${{\hspace{{4mm}} M1 = 0}}$    

        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2 = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_y = {(d[0]):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} M2 = {(f[1]*calc['sin1']*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 3.3 Momento de la fuerza F3: }}$ 

        Para calcular el momento de la fuerza F3, vemos que podemos hacer la suma de los momento en A que producen sus compenentes. Tal que: 

        $\\underline{{Momento \\hspace{{2mm}} F3_x: }}$        

        Con la componente en X de F3 es apreciable que la componente perpendicular del vector posicion seria $r3_y$. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento es negativo: 
        
        ${{\hspace{{4mm}} M3_1 = -r3_y \\cdot\\hspace{{1mm}} F3_x = -{(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['cos5']:.2f}{{\\text{{ N}}}}}}$           
        ${{\hspace{{4mm}} M3_1 = {-(f[2]*calc['cos5']*(d[3]*calc['sin9'])):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$                 

        $\\underline{{Momento \\hspace{{2mm}} F3_y: }}$ 

        Con la componente en Y de F3 es apreciable que la componente perpendicular del vector posicion seria $r3_x$. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento tambíen es negativo: 

        ${{\hspace{{4mm}} M3_2 = - r3_x \\cdot\\hspace{{1mm}} F3_y = -{d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['sin5']:.2f}{{\\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} M3_2 = {-(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$

        Finalmente el momento en el punto A de la fuerza F3 sería: 

        ${{\hspace{{4mm}} M3 = M3_1 + M3_2 = {-(f[2]*calc['cos5']*(d[3]*calc['sin9'])):.2f}{{\\text{{ N}} \\cdot\\text{{ m }}}}{-(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} M3 = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$ 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    
    Questionary(#2_1
        code = 1620021,
        no_pregunta = 2,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre el valor de F1 para que el momento que este causa en B sea igual al momento en B de F3. Considere que $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza F1 [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[2]*(d[3]/d[0])*Calculations.sine(a[4]+a[8]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:  

        A partir de esta definición vamos a buscar resolver el problema, igualando los momentos de ambas fuerzas en B y despejando F1.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas del problema:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F3 :}}$ 
        
        ${{\hspace{{4mm}} F3_x = |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[2]*calc['cos5']:.2f}{{ \\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} F3_y = |\\overrightarrow{{F3}}| \\cdot \\sin(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[2]*calc['sin5']:.2f}{{ \\text{{ N}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        $\\underline{{Vector Posición \\hspace{{2mm}} r1: }}$         

        En este caso el vector posición $\\overrightarrow{{r1}}$ solo tiene componente en X y es igual a la magnitud de la distancia de B al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r1 = X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        
        $\\underline{{Vector Posición \\hspace{{2mm}} r3: }}$ 

        ${{\hspace{{4mm}} r3_x = X_2 \\cdot \\cos(\\beta) = {d[3]*calc['cos9']:.2f}{{ \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} r3_y = x_2 \\cdot \\sin(\\beta) = {d[3]*calc['sin9']:.2f}{{ \\text{{ m}}}}}}$      

        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$
        
        Definimos la formula del momento en B de F1:  

        ${{\hspace{{4mm}} M1 = -r1  \\cdot F1}}$        
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F3: }}$ 

        Para el momento de la fuerza F3, vemos que podemos hacer la suma de los momento en B que producen sus compenentes. Tal que: 

        $\\underline{{Momento \\hspace{{2mm}} F3_x: }}$        

        Con la componente en X de F3 es apreciable que la componente perpendicular del vector posicion seria $r3_y4. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento es negativo: 
        
        ${{\hspace{{4mm}} M3_1 = -r3_y \\cdot\\hspace{{1mm}} F3_x = -{(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['cos5']:.2f}{{\\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} M3_1 = {-(f[2]*calc['cos5']*(d[3]*calc['sin9'])):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$                 

        $\\underline{{Momento \\hspace{{2mm}} F3_y: }}$ 

        Con la componente en Y de F3 es apreciable que la componente perpendicular del vector posicion seria $r3_x$. Además, notamos que por $\\textit{{Regla de la mano de derecha}}$ este momento tambíen es negativo: 

        ${{\hspace{{4mm}} M3_2 =  -r3_x \\cdot\\hspace{{1mm}} F3_y = -{(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['sin5']:.2f}{{\\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} M3_2 = {-(f[2]*calc['sin5']*((d[3]*calc['cos9']))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      

        Ahora, el momento en el punto B de la fuerza F3 sería: 

        ${{\hspace{{4mm}} M3 = M3_1 + M3_2 = {-(f[2]*calc['cos5']*(d[3]*calc['sin9'])):.2f}{{\\text{{ N}} \\cdot\\text{{ m }}}}{-(f[2]*calc['sin5']*((d[3]*calc['cos9']))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} M3 = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        
        $\\textbf{{\\small 4. Calculo de F1: }}$
        
        ${{\hspace{{4mm}} M1 = -r1  \\cdot F1 = M3}}$     
        ${{\hspace{{4mm}} {-d[0]:.0f}{{ \\text{{ m}}}} \\cdot F1 = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F1 = {(f[2]*(d[3]/d[0])*Calculations.sine(a[4]+a[8])):.2f}{{ \\text{{ N}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 1620031    ---------------------------------------------------

    Questionary(#3_1
        code = 1620031,
        no_pregunta = 3,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la magnitud y dirección de una cuarta fuerza F4 aplicada a ${(d[0]*(3/5)):.2f} \\text{{ m}}$ de A sobre el tramo AB, para que la suma de momentos en A sea igual a la suma de momentos en B. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza F4 [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[2]*calc['sin5']-f[0]-f[1]*calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, se presenta la solución sugerida para el ejercicio:  

        A partir de esta definición vamos a buscar resolver el problema, igualando los momentos que se causan en A y en B contando con F4, tal que, al final logremos despejar F4.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas del problema:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 
        
        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ N}}}}}}$       

        $\\underline{{Fuerza \\hspace{{2mm}} F3 :}}$ 
        
        ${{\hspace{{4mm}} F3_x = |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[2]*calc['cos5']:.2f}{{ \\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} F3_y = |\\overrightarrow{{F3}}| \\cdot \\sin(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[2]*calc['sin5']:.2f}{{ \\text{{ N}}}}}}$      
        
        $\\underline{{Fuerza \\hspace{{2mm}} F4 :}}$ En este ejercicio vamos a asumir que tiene dirección positiva en Y.
        
        Ahora vamos a expresar la sumatoria de momentos en A y en B
        
        $\\textbf{{\\small 2.1 Sumatoria de Momentos en A:}}$ 
        
        En A podemos encontrar que solo las fuerzas F4, F3 y la componente en Y de la fuerza F2 generan momento en el punto A. Tal que quedaria:
        
        ${{\hspace{{4mm}} M_A = F4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) \\cdot X_1 - |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) \\cdot x_2 \\cdot \\sin(\\beta) - |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) \\cdot (X_1 + X_2 \\cdot \\cos(\\beta))}}$     
        ${{\hspace{{4mm}} M_A = F4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + {f[1]*calc['sin1']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}} {(d[0]):.0f}{{ \\text{{ m}}}} - {f[2]*calc['cos5']:.2f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} - {f[2]*calc['sin5']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}}{d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} M_A = F4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + {(f[1]*calc['sin1']*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{m}}}} - {((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$    
        ${{\hspace{{4mm}} M_A = F4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + ( {((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}} ) }}$    
        
        $\\textbf{{\\small 2.2 Sumatoria de Momentos en B:}}$ 
        
        En B es evidente que solo las fuerzas F4, F3 y F1 generan momento. Tal que quedaria:
        
        ${{\hspace{{4mm}} M_B = -F4 \\cdot  ( X_1 - {(d[0]*(3/5)):.2f}) \\text{{ m}} - |\\overrightarrow{{F1}}| \\cdot X_1 - |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) \\cdot x_2 \\cdot \\sin(\\beta) - |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) \\cdot (X_2 \\cdot \\cos(\\beta))}}$     
        ${{\hspace{{4mm}} M_B = -F4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {f[0]:.0f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[0]):.0f}{{ \\text{{ m}}}}  {f[2]*calc['cos5']:.2f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} - {f[2]*calc['sin5']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}}{(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$    
        ${{\hspace{{4mm}} M_B = -F4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{m}}}} - {((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$        
        ${{\hspace{{4mm}} M_B = -F4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        
        $\\textbf{{\\small 3. Igualamos y despejamos para F4: }}$ 
        
        ${{\hspace{{4mm}} M_A = M_B }}
        ${{\hspace{{4mm}} F4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + ( {((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}} ) \\text{{ = }} -F4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F4 \\cdot  {(d[0]):.2f} \\text{{ m}} = {-((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))))-((f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F4 = {f[2]*calc['sin5']-f[0]-f[1]*calc['sin1']}}}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),




    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel dificil     ---------------------------------------------------
    #-------------------------------------------------       Code: 1630011    ---------------------------------------------------

    Questionary(#1_1
        code = 1630011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ lb}}$ sobre su cuerda, determine la magnitud de la fuerza F1 que debe aplicar el trabajador en C para evitar quer gire el poste.  $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$ y $X_2 = {d[3]:.0f}  \\text{{ ft}}$.",
        no_answers = 1,
        a1_name = "Fuerza F1 [lb]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['cos5']*(d[0]+d[3]))/(d[0]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, vamos a resolver el ejercicio usando esta definición:  

        Inicialmente, observamos que para que la condición del enunciado se cumpla es necesario que la suma de momentos en A sea igual a cero.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
        ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1)}}$       
        ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1)}}$       

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*calc['cos5']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*calc['sin5']:.2f}{{ \\text{{ lb}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}}}}$  
        
        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para calcular el momento de F1 en A vemos que la componente perpendicular al vector posición asociado r1 es $F1_x$, y que por la $\\textit{{Regla de la mano de derecha}}$ el momento sera negativo. Tal que: 

        ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F1}}| \\cdot {calc['sin1']:.2f}}}$
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_x$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_y = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} M2_A = {(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Hacemos sumatoria de momentos en A y la igualamos a cero: 
        
        ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
        ${{\hspace{{4mm}} - {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F1}}| \\cdot {calc['sin1']:.2f} + {(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = 0}}$         
        ${{\hspace{{4mm}} {d[0]*calc['sin1']:.2f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F1}}| = {(f[1]*calc['sin5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} |\\overrightarrow{{F1}}| = \\dfrac{{{(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{d[0]*calc['sin1']:.2f}{{ \\text{{ ft}}}}}}}}$     
        ${{\hspace{{4mm}} |\\overrightarrow{{F1}}| = {(f[1]*calc['cos5']*(d[0]+d[3]))/(d[0]*calc['sin1']):.2f}{{ \\text{{ lb}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel dificil     ---------------------------------------------------
    #-------------------------------------------------       Code: 1630021    ---------------------------------------------------

    Questionary(#2_1
        code = 1630011,
        no_pregunta = 2,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ lb}}$ sobre su cuerda, y el que está ubicado en C realiza otra fuerza $F_1 = {f[0]:.0f} \\text{{ lb}}$, determine la magnitud la distancia en la que la fuerza F1 se debe aplicar para evitar quer gire el poste.  $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$ y $X_2 = {d[3]:.0f}  \\text{{ ft}}$.",
        no_answers = 1,
        a1_name = "Distancia X1 [ft]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[1]*calc['cos5']*(d[3]))/(f[0]*calc['sin1']-f[1]*calc['cos5'])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, vamos a resolver el ejercicio usando esta definición:  

        Inicialmente, observamos que para que la condición del enunciado se cumpla es necesario que la suma de momentos en A sea igual a cero.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
        ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$             
        ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[0]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$            

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*calc['cos5']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*calc['sin5']:.2f}{{ \\text{{ lb}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 }}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = X_1 + {(d[3]):.0f}{{ \\text{{ ft}}}}}}$  
        
        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para calcular el momento de F1 en A vemos que la componente perpendicular al vector posición asociado r1 es $F1_x$, y que por la $\\textit{{Regla de la mano de derecha}}$ el momento sera negativo. Tal que: 

        ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - X_1 \\cdot {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_x$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_x = ( X_1 + {(d[3]):.0f} ){{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} M2_A = ( X_1 \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}} + {(f[1]*calc['cos5']*(d[3])):.2f} ) {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Hacemos sumatoria de momentos en A y la igualamos a cero: 
        
        ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
        ${{\hspace{{4mm}} - X_1 \\cdot {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}} + X_1 \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}} +{(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = 0}}$         
        ${{\hspace{{4mm}} X_1 \\cdot ({f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}} - {f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}) = {(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} X_1 = \\dfrac{{{(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{f[0]*calc['sin1']-f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}}}$     
        ${{\hspace{{4mm}} X_1 = {(f[1]*calc['cos5']*(d[3]))/(f[0]*calc['sin1']-f[1]*calc['cos5']):.2f}{{ \\text{{ ft}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    

]