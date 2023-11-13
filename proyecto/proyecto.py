# import pandas lib as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importar las hojas de cálculo usando pandas

dataframe1 = pd.read_excel('Taller razonamiento 2023-2-1 (respuestas).xlsx', usecols = "E:M")
dataframe2 = pd.read_excel('Taller razonamiento 2023-2-2 (respuestas).xlsx')

# dataframe que se va a usar. Se puede cambiar luego

dataframe = dataframe1

# lista con los titulos de las columnas que se quieren analizar.

tit1 = dataframe1.columns.values.tolist()[1:9]
tit2 = dataframe2.columns.values.tolist()[1:9]

# lista que se va a usar. Se puede ambiar luego

tit = tit1

### filtro facultad

def filtro(nombre):
    if(nombre=="Enfermería"):
        facultad = dataframe["Seleccione la facultad a la que pertenece"]

        enferemeria = dataframe[facultad == "Enferemeria"]
        enfermeria = dataframe[facultad == "Enfermería"]

        enfe = pd.concat([enferemeria, enfermeria], ignore_index=True, sort=False)
        return enfe[tit].to_numpy()
    else:
        facultad = dataframe["Seleccione la facultad a la que pertenece"]
        facultad = dataframe[facultad == nombre]
        return facultad[tit].to_numpy()

# filtro() recibe un str con el nombre de la facultad que se desea filtrar. Retorna un arreglo de numpy de arreglos chiquitos, cada arreglo chiquito corresponde a las respuestas de un encuestado de la facultd seleccionada.

#Hay dos nombres para la facultad de enfermería en la hoja de cálculo, por eso se le debe brindar un tratamiento especial.

### filtro pregunta

def pregunta(n, array):
    rep = np.zeros(5)
    for ii in range (5):
        rep[ii] = np.sum(array[:, n] == ii+1)
    return rep

#El filtro de pregunta recibe un numero de pregunta y un arreglo de numpy con las respuestas. Retorna un arreglo de numpy de 5 elementos. Cada elemento es el número de veces que un encuestado dio esa respuesta a la pregunta seleccionada.

### Graficador

def graficador(n, nombre):
    rs = np.array([1,2,3,4,5])
  
    if(nombre=="Universidad"):
        plt.figure(figsize=(12, 16)) 
        plt.subplots_adjust(wspace=0.5, hspace=0.5)
        plt.suptitle("Respuestas Universidad", 
                     fontsize=18, y=0.95)

        for iii in range(8):
            ax = plt.subplot(4, 2, iii+1)
            ax.bar(rs, pregunta(iii, dataframe[tit].to_numpy()))
            ax.set(xlabel='Respuestas', ylabel='Número de respuestas', 
                   title='Pregunta '+str(iii+1))

        plt.savefig(str(n)+"_Universidad.pdf")

    else:
        plt.figure(figsize=(12, 16)) 
        plt.subplots_adjust(wspace=0.5, hspace=0.5)
        plt.suptitle("Respuestas facultad de "+str(nombre), 
                     fontsize=18, y=0.95)

        for iii in range(8):
            ax = plt.subplot(4, 2, iii+1)
            ax.bar(rs, pregunta(iii,filtro(nombre)))
            ax.set(xlabel='Respuestas', ylabel='Número de respuestas', 
                   title='Pregunta '+str(iii+1))
  
        plt.savefig(str(n)+"_"+nombre+".pdf")

#La función graficador(n,nombre) produce el .pdf con las gráficas correspondientes a las respuestas a cada pregunta. n es el tipo de encuesta, nombre es la facultad que se quiere filtrar. Si se usa nombre='Universidad', el graficador retornará gráficas correspondiente a todos los encuestados. 

graficador(1, "Universidad")
graficador(1, "Enfermería")

#filtro('Ciencias Económicas')


