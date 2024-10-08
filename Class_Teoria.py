#class Concepts stores the information of each theory exercises
class Theory:
    def __init__(self, code, no_pregunta, topic, subtopic, enunciado, opcion_1, opcion_2, opcion_3, opcion_4, opcion_correcta, respuesta_P1,respuesta_P2):
        self.code = code #Tema #Subtema #Nivel de dificultad (0) #No. pregunta (001) #no_version (0)
        self.no_pregunta = no_pregunta
        self.topic = topic
        self.subtopic = subtopic
        self.enunciado = enunciado
        self.opcion_1 = opcion_1
        self.opcion_2 = opcion_2
        self.opcion_3 = opcion_3
        self.opcion_4 = opcion_4
        self.opcion_correcta = opcion_correcta
        self.respuesta_P1 = respuesta_P1
        self.respuesta_P2 = respuesta_P2

    #Function to filter the theory questions according to the user's selection
    def filtrar_preguntas_teoria(preguntas_teoria, topic=None, subtopic=None):
        preguntas_filtradas_teoria = [
            pregunta for pregunta in preguntas_teoria
            if (topic is None or pregunta.topic == topic) and
               (subtopic is None or pregunta.subtopic == subtopic)
        ]
        return preguntas_filtradas_teoria

conceptuales = [
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores         ---------------------------------------------------
    #-------------------------------------------------       11000##0         ---------------------------------------------------

    Theory(#1
        code = 1100010, 
        no_pregunta = 1,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere el vector $\\overrightarrow{{P}}$ que se encuentre a $\\alpha [°]$ del eje X. Determine la magnitud y dirección del vector $\\overrightarrow{{Q}}$ para que |$\\overrightarrow{{P}} + \\overrightarrow{{Q}}$| sea mínima:",
        opcion_1 = "$\\overrightarrow{{Q}} = -\\overrightarrow{{P}}$",
        opcion_2 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}} \\cdot cos(\\alpha)$",
        opcion_3 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}} \\cdot sin(\\alpha)$",
        opcion_4 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}}$",
        opcion_correcta = "$\\overrightarrow{{Q}} = -\\overrightarrow{{P}}$",
        respuesta_P1 = """
        Para que la magnitud de la suma sea mínima los vectores deben tener la misma magnitud y dirección pero sentidos opuestos. De esta manera se obtiene 0.

        |$\\overrightarrow{{P}} + \\overrightarrow{{Q}}$|= $\\overrightarrow{{P}} + \\overrightarrow{{Q}}$ =  $\\overrightarrow{{P}} + \\overrightarrow{{-P}}$ = 0"
        """,
        respuesta_P2 = "",
        ),
    
    Theory(#2
        code = 1100020, 
        no_pregunta = 2,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere los vectores $\overrightarrow{A}$ y $\overrightarrow{B}$, ¿Cuál es el ángulo ($\\alpha [°]$) entre ellos que minimiza la magnitud de su suma ($\overrightarrow{A} + \overrightarrow{B}$)?.",
        opcion_1 = "$0^\circ$",
        opcion_2 = "$180^\circ$",
        opcion_3 = "$90^\circ$",
        opcion_4 = "$45^\circ$",
        opcion_correcta = "$180^\circ$",
        respuesta_P1 = "Un ángulo de 180° implica que los vectores tienen misma dirección y sentidos opuestos lo cual minimiza la magnitud del vector resultante",
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 1100030, 
        no_pregunta = 3,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere los vectores $\overrightarrow{A}$ y $\overrightarrow{B}$, ¿Cuál es el ángulo ($\\alpha [°]$) entre ellos que maximiza la magnitud de su suma ($\overrightarrow{A} + \overrightarrow{B}$)?.",
        opcion_1 = "$0^\circ$",
        opcion_2 = "$180^\circ$",
        opcion_3 = "$90^\circ$",
        opcion_4 = "$45^\circ$",
        opcion_correcta = "$0^\circ$",
        respuesta_P1 = "Un ángulo de 0° implica que los vectores tienen misma dirección y sentido lo cual maximiza la magnitud del vector resultante.",
        respuesta_P2 = "",
        ),     
    
    Theory(#4
        code = 1100040,
        no_pregunta = 4,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "A partir del vector $\overrightarrow{F}$ mostrado en la figura, ¿Es correcto afirmar que un vector unitario con la misma dirección es: $\\overrightarrow{{u}} = \\dfrac{{3}}{{5}} \\hat{{i}} + \\dfrac{{4}}{{5}} \hat{{j}}$?",
        opcion_1 = "Sí, ya que el vector $\overrightarrow{F}$ tiene magnitud 5 y al dividir cada componente de $\overrightarrow{F}$ entre su magnitud se obtiene que su dirección es igual a $\overrightarrow{u}.$",
        opcion_2 = "No, ya que $\overrightarrow{F}$ y $\overrightarrow{u}$ tienen magnitudes diferentes y por ende, direcciones diferentes.",
        opcion_3 = "No, ya que $\overrightarrow{u}$ no es un vector unitario.",
        opcion_4 = "Sí, ya que $\overrightarrow{u}$ es un vector de magnitud 5 y al multiplicar su magnitud por $\\dfrac{{3}}{{5}} \\hat{i} + \\dfrac{4}{5} \\hat{j}$ se obtiene un vector de $\overrightarrow{F}.$",
        opcion_correcta = "Sí, ya que el vector $\overrightarrow{F}$ tiene magnitud 5 y al dividir cada componente de $\overrightarrow{F}$ entre su magnitud se obtiene que su dirección es igual a $\overrightarrow{u}.$",
        respuesta_P1 = "Un vector se expresa de la forma $\overrightarrow{V} = \|\overrightarrow{V}\|\overrightarrow{U}_v$ donde $\overrightarrow{U}_v$ es un vector unitario que se obtiene al calcular $\\dfrac{{\\overrightarrow{{V}}}}{{|\\overrightarrow{{V}}|}}$ y representa la dirección de un vector. Por ello, encontrar un vector unitario con la misma dirección a un vector $\overrightarrow{F}$ es equivalente a encontrar la dirección de $\overrightarrow{F}$ normalizándolo. Es decir, dividiendo sus componentes entre su magnitud para obtener un vector de magnitud 1.",
        respuesta_P2 = "",
        ),
    
    Theory(#5
        code = 1100050, 
        no_pregunta = 5,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "El vector unitario se utiliza para:",
        opcion_1 = "Representar la magnitud de un vector en una dirección específica.",
        opcion_2 = "Indicar la dirección de un vector.",
        opcion_3 = "Escalar vectores a una magnitud deseada.",
        opcion_4 = "Operar vectores.",
        opcion_correcta = "Indicar la dirección de un vector.",
        respuesta_P1 = "El vector unitario representa la dirección de un vector gracias a que su magnitud es 1. Esto permite que no se alteren los valores de las componentes de dirección de un vector.",
        respuesta_P2 = "",
        ),

    Theory(#6
        code = 1100060, 
        no_pregunta = 6,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        ¿Cuál(es) de las siguientes afirmaciones son ciertas respecto al vector unitario?:

        I. Siempre tiene magnitud 1.   
        II. Es un vector cuya magnitud puede ser cualquier número entero.    
        III. Se obtienen al dividir la magnitud de un vector entre sus componentes.      
        IV. Se obtiene al dividir las componentes de un vector entre su magnitud.     
        """,
        opcion_1 = "I, III",
        opcion_2 = "II, IV",
        opcion_3 = "I, IV",
        opcion_4 = "II, III",
        opcion_correcta = "I, IV",
        respuesta_P1 = """
        Por definición la magnitud de todo vector unitario es 1.

        Los vectores unitarios provienen de la acción de normalizar un vector; es decir, dividirlo entre su magnitud con el objetivo de obtener solo su dirección. Y, como un vector unitario representan la dirección de un vector, encontrar su dirección es equivalente a encontrar su vector unitario.
        """,
        respuesta_P2 = "",
        ),    
    
    Theory(#7
        code = 1100070, 
        no_pregunta = 7,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Los vectores $\overrightarrow{P}$ y $\overrightarrow{Q}$ pueden ser escritos de forma vectorial como:",
        opcion_1 = """ $\\overrightarrow{P} = cos(\\alpha) \\hat{i} + sen(\\alpha)\\hat{{j}}$ \\
        $\\overrightarrow{Q} = sin(\\theta) \\hat{i} + cos(\\theta)\\hat{{j}}$""",
        opcion_2 = """$\\overrightarrow{P} = sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}$ \\
        $\\overrightarrow{Q} = cos (\\theta) \\hat{i} + sin(\\theta) \\hat{j}$""",
        opcion_3 = """$\\overrightarrow{P} = (sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}) |\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (cos (\\theta) \\hat{i} + sen(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        opcion_4 = """$\\overrightarrow{P} = (cos(\\alpha) \\hat{i} + sen(\\alpha) \\overrightarrow{j}) |\\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (sen(\\theta) \\hat{i} + cos(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        opcion_correcta = """$\\overrightarrow{P} = (sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}) |\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (cos (\\theta) \\hat{i} + sen(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        respuesta_P1 = """
        El seno es la razón entre el lado opuesto al ángulo y la hipotenusa, mientras el coseno es la razón entre el lado adyacente al ángulo y la hipotenusa. De tal forma que el seno no siempre se relaciona con el eje y (componente j) y el coseno con el eje x (componente i). 
        Para determinar las componentes usando ángulos se recomienda identificar la ubicación del ángulo y aplicar las razones mencionadas.
        """,
        respuesta_P2 = "",
        ),
    
    Theory(#8
        code = 1100080, 
        no_pregunta = 8,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "¿Qué pasa con $\|\overrightarrow{V}\|$ cuando se multiplica por $a$?",
        opcion_1 = "Aumenta $a^2$ veces",
        opcion_2 = "Aumenta $a$ veces",
        opcion_3 = "Disminuye $a^2$ veces",
        opcion_4 = "Disminuye $a$ veces",
        opcion_correcta = "Aumenta $a$ veces",
        respuesta_P1 = """
        Esto ocurre porque como se trata de un entero positivo, al efectuar la multiplicación, se afecta únicamente la magnitud del vector en la misma proporción.
        Si, en cambio, se multiplica por $-a$ el resultado sería un cambio de dirección y de magnitud. Y, si $a$ es un número fraccionario,su magnitud podría disminuir.
        """,
        respuesta_P2 = "",
        ),

    Theory(#9
        code = 1100090, 
        no_pregunta = 9,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        El producto punto es útil ya que:    

        I. Encontrar el vector resultante entre 2 vectores.   
        II. Determinar el ángulo entre 2 vectores.   
        III. Calcular el área del paralelogramo formado entre 2 vectores.    
        IV. Encontrar la proyección de un vector sobre el otro.
        """,
        opcion_1 = "I, III",
        opcion_2 = "II, IV",
        opcion_3 = "I, IV",
        opcion_4 = "II, III",
        opcion_correcta = "II, IV",
        respuesta_P1 = """
        El producto punto (o producto escalar) permite determinar el ángulo entre dos vectores porque está directamente relacionado con el coseno del ángulo entre ellos. Y, al despejar el ángulo de la ecuación respectiva este puede conocerse.
        Así mismo, permite encontrar la proyección entre 2 vectores dado que relaciona la dirección entre ellos con sus magnitudes. De tal forma que, si se quiere encontrar la magnitud de un vector proyectado solo el otro basta con calcular la multiplicación entre la magnitud del vector que se quiere proyectar por el coseno del ángulo que tiene este con el vector sobre el cual quiere proyectarse.
        """,
        respuesta_P2 = "",
        ),    
    
    Theory(#10
        code = 11000100, 
        no_pregunta = 10,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        ¿Cuál(es) de las siguientes afirmaciones son ciertas respecto al producto punto entre vectores?:    
        
        $I. \\hspace{{2mm}} A \\cdot B = B \\cdot A$                       $\\hspace{{20mm}} IV. \\hspace{{2mm}} A \\cdot B \\text{{ es un escalar}}$        
        $II. \\hspace{{2mm}} A \\cdot B \\text{{ es un vector}}$           $\\hspace{{14mm}} V. \\hspace{{2mm}} \\text{{Cuando }}A \\cdot B = 0, \\text{{el ángulo entre A y B es 45°}}$    
        $III. \\hspace{{2mm}} A \\cdot B = -B \\cdot A$                    $\\hspace{{19mm}} VI. \\hspace{{2mm}} \\text{{Cuando }}A \\cdot B = 0, \\text{{el ángulo entre A y B es 90°}}$   
        """,
        opcion_1 = "$IV$",
        opcion_2 = "$I, III,IV$",
        opcion_3 = "$II, V, VI$",
        opcion_4 = "$I, IV, VI$",
        opcion_correcta = "$I, IV, VI$",
        respuesta_P1 = "Las caracteristicas principales del producto punto son: es conmutativo, da como resultado un número real, es 0 cuando los ángulos son perpendiculares  ya que el cos(90°)=0.",  
        respuesta_P2 = "",
        ),

    Theory(#11
        code = 11000110, 
        no_pregunta = 11,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "La dirección de los vectores puede expresarse por medio de cosenos directores ó ángulos en grados o radianes. Indique cuál de las siguientes es la forma correcta para pasar de grados a radianes:",
        opcion_1 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{\pi}{180}$",
        opcion_2 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{180}{\pi}$",
        opcion_3 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot \\pi$",
        opcion_4 = "$\\theta_{radianes}$ = $\\theta_{grados}\cdot 2\cdot\pi$",
        opcion_correcta = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{\pi}{180}$",
        respuesta_P1 = "Esta conversión se debe a que en 360° se recorren 2 \pi$ radianes de longitud",
        respuesta_P2 = "",
        ),  

    Theory(#12
        code = 11000120, 
        no_pregunta = 12,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "El producto punto se calcula a partir de las siguientes expresiones equivalentes:",
        opcion_1 = "A \\cdot B = ABcos(\\theta)$ = a_xb_x + a_yb_y + a_zb_z$",
        opcion_2 = "A \\cdot B = ABcos(\\theta)$ = a_xb_y - a_yb_x$",
        opcion_3 = "A \\cdot B = ABsen(\\theta)$ = a_xb_x + a_yb_y + a_zb_z$",
        opcion_4 = "A \\cdot B = ABsen(\\theta)$ = a_xb_y - a_yb_x$",
        opcion_correcta = "A \\cdot B = ABcos(\\theta)$ = a_xb_x + a_yb_y + a_zb_z$",
        respuesta_P1 = "El producto punto relaciona las magnitudes de los vectores con  el coseno del ángulo entre ellos",
        respuesta_P2 = "Cuando no se conoce el ángulo entre los dos vectores el producto punto puede calcularse como la suma de la multiplicación componente a componente",
        ), 
    
    Theory(#13
        code = 11000130, 
        no_pregunta = 13,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado ="El producto cruz es utilizado para:", 
        opcion_1 = "Permite determinar la magnitud de la suma entre dos vectores.",
        opcion_2 = "Permite determinar el ángulo entre 2 vectores.",
        opcion_3 = "Permite encontrar la proyección de un vector sobre el otro.",
        opcion_4 = "Permite calcular un vector perpendicular al plano formado por los dos vectores.",
        opcion_correcta = "Permite calcular un vector perpendicular al plano formado por los dos vectores.",
        respuesta_P1 = "El producto punto relaciona las magnitudes de los vectores con  el coseno del ángulo entre ellos",
        respuesta_P2 = "Al realizar producto cruz entre dos vectores se obtiene siempre un vector perpendicular al plano formado entre estos el cual es un indicador, por ejemplo, de la dirección del momento",
        ),     
]