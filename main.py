# Practica NLTK analisis de frecuencias de palabras

import nltk
from nltk.tokenize import word_tokenize #divide el texto en palabras
from nltk.corpus import stopwords # elimina los conectores
from nltk.probability import FreqDist  # calcula frecuencias
from collections import Counter # calcula frecuencias

texto = """Un párrafo es una unidad de un texto compuesta por una o varias oraciones, que comienza con una mayúscula y que termina con un punto y aparte. Los textos se organizan de manera tal que cada párrafo trata sobre una idea central. Generalmente, la primera oración de cada párrafo suele explicitar cuál es el punto principal que se desarrollará"""


# separa las palabras del texto - Tokeniza

palabras = word_tokenize(texto, language="spanish")
print(palabras)

# Elimina los conectores -- stopwords

stopwords = set(stopwords.words("spanish"))

# filtramos las palabras que no son stopwords

palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords and palabra.isalpha()]

print(palabras_filtradas) # genera lista de palabras filtradas

# Calcula las frecuencias de las palabras

frecuencia_palabras = FreqDist(palabras_filtradas)

# mostrar las frecuencias de las 5 palabras mas comunes

print(frecuencia_palabras.most_common(5)) 