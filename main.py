# Practica ntkl analisis de frecuencia de palabras

# Importar librerias
import nltk
from nltk.tokenize import word_tokenize # Tokenizacion: divide el texto en palabras
from nltk.corpus import stopwords # Elimina los conectores
from nltk.probability import FreqDist # Calcula la frecuencia de las palabras

# Definir el texto en español
texto = """Los pricipios del Derecho
Los principios del derecho son las bases sólidas sobre las que se construye todo sistema jurídico. Son ideas 
fundamentales que guían la creación de leyes, la interpretación de normas y la resolución de conflictos. 
Estos principios, universales y atemporales, buscan garantizar la justicia, la igualdad y la convivencia 
pacífica en la sociedad.
Si bien pueden variar ligeramente entre diferentes sistemas jurídicos, algunos de los principios más 
destacados son la igualdad ante la ley, la justicia, la libertad, la seguridad y la dignidad humana. Estos 
principios no solo sirven como guía para los jueces y abogados, sino que también empoderan a los ciudadanos 
al brindarles un marco de referencia para exigir sus derechos y cumplir con sus deberes.
La importancia de estos principios radica en su capacidad para garantizar la estabilidad social, proteger 
los derechos individuales y promover el desarrollo de las sociedades. Al establecer un conjunto de reglas 
claras y justas, se reduce la incertidumbre y se fomenta la confianza en las instituciones."""

#Tokenizar el texto
palabras = word_tokenize(texto, language='spanish')
print(palabras)

# Eliminar conectores
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras que no estan en la lista de conectores
palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words and palabra.isalpha()]
#isalpha: tomar el texto y elimina los signos de puntuacion
print(palabras_filtradas) # Genera la lista de palabras filtradas

# Anallisis de frecuencia de las palabras
frecuencia_palabras = FreqDist(palabras_filtradas)

# Mostrar la frecuencia de las 10 palabras mas comunes
print(frecuencia_palabras.most_common(5))
