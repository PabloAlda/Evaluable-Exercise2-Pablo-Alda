#Este es un programa en Python para analizar y visualizar la población estelar de una galaxia. El programa permite a los usuarios ingresar datos de observación de estrellas (por ejemplo, luminosidad, temperatura, distancia), realizar análisis estadísticos y generar visualizaciones para obtener información sobre la composición estelar de la galaxia.
#Importamos las siguientes bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Mostramos en pantaña una pequeña explicación de lo que hace el programa.
print("Bienvenido, este programa se encarga de analizar y visualizar estrellas, permitiendo al usuario introducir los datos que desee.")
#Creamos la función llamada ingresar datos
def ingresar_datos_estelares():
#Pedimos al usuario que nos indique el número de estrellas que desa analizar.
    num_estrellas = int(input("Ingrese el número de estrellas que desea analizar: "))

#Cremos las variables sin darles ningun valor inicial
    luminosidades = []
    temperaturas = []
    distancias = []

#Con un for pedimos al usuario los datos de las variables, y los guardamos en su respectiba variable, luego mediante el uso de un return devolvemos estos valores.
    for i in range(num_estrellas):
        luminosidad = float(input(f"Ingrese la luminosidad de la estrella {i + 1} (en unidades solares): "))
        temperatura = float(input(f"Ingrese la temperatura de la estrella {i + 1} (en Kelvin): "))
        distancia = float(input(f"Ingrese la distancia de la estrella {i + 1} a la galaxia (en parsecs): "))

        luminosidades.append(luminosidad)
        temperaturas.append(temperatura)
        distancias.append(distancia)

    return np.array(luminosidades), np.array(temperaturas), np.array(distancias)

#Creamos la función analisis estadístico
def analisis_estadistico(temperaturas):
#Utilizando la librerias calculamos diferentes valores
    media = np.mean(temperaturas)
    mediana = np.median(temperaturas)
    desviacion_estandar = np.std(temperaturas)

#Usamos diferentes prints, para mostrar en pantalla los datos calculados
    print("\nAnálisis Estadístico de Temperaturas:")
    print(f"Media: {media} K")
    print(f"Mediana: {mediana} K")
    print(f"Desviación Estándar: {desviacion_estandar} K")

#Creamos la función visualización histograma
def visualizacion_histograma(temperaturas):
    plt.hist(temperaturas, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de Temperaturas Estelares')
    plt.xlabel('Temperatura (K)')
    plt.ylabel('Número de Estrellas')
    plt.show()

#Creamos la función main, la función principal
def main():
    print("Programa de Análisis de Población Estelar de una Galaxia")

    luminosidades, temperaturas, distancias = ingresar_datos_estelares()

    analisis_estadistico(temperaturas)

    visualizacion_histograma(temperaturas)

if __name__ == "__main__":
    main()