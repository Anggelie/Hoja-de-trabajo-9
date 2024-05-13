
import networkx as nx

def crear_grafo():
    grafo = nx.Graph()
    with open("rutas.txt", "r") as file:
        for linea in file:
            origen, destino, costo = linea.strip().split(", ")
            grafo.add_edge(origen, destino, weight=int(costo))
    return grafo

def mostrar_destinos(grafo, estacion_salida):
    destinos = list(grafo.neighbors(estacion_salida))
    print(f"Posibles destinos desde {estacion_salida}:")
    for destino in destinos:
        costo = grafo[estacion_salida][destino]['weight']
        print(f"{destino} - Costo: {costo}")

def dijkstra(grafo, estacion_salida):
    rutas = nx.single_source_dijkstra_path(grafo, estacion_salida)
    costos = nx.single_source_dijkstra_path_length(grafo, estacion_salida)
    del rutas[estacion_salida]  # Eliminar la ruta desde la estación de salida hacia ella misma
    del costos[estacion_salida]  # Eliminar el costo de llegar a la estación de salida desde ella misma
    return rutas, costos

def main():
    grafo = crear_grafo()
    estacion_salida = input("Ingrese la estación de salida: ")
    mostrar_destinos(grafo, estacion_salida)
    rutas, costos = dijkstra(grafo, estacion_salida)
    print("\nMejores rutas:")
    for destino in rutas:
        ruta = " -> ".join(rutas[destino])
        print(f"{destino}: {ruta} - Costo total: {costos[destino]}")

if __name__ == "__main__":
    main()
