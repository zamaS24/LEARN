import dearpygui.dearpygui as dpg
import numpy as np
import pandas as pd
import math
from sklearn.datasets import make_blobs



import matplotlib.pyplot as plt



data = None
k = None
X = None

def show_plot1(X):
    plt.scatter(X[:, 0], X[:, 1], c='blue', s=10)
    plt.title('Objets')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def initialiser_centroids(k, data):
    n_dims = data.shape[1]
    centroid_min, centroid_max = np.min(data, axis=0), np.max(data, axis=0)
    centroids = np.random.uniform(centroid_min, centroid_max, size=(k, n_dims))
    centroids = pd.DataFrame(centroids, columns=data.columns)
    return centroids

def calculer_distance(x1, x2):
    
    distance = np.sum(np.square(x1-x2))
    return distance

def assigner_centroid(data, centroids):  
    n_objets = data.shape[0]
    centroid_assign = []
    centroid_distances = []
    k = centroids.shape[0]
    centroids_arr = centroids.iloc[:, :2].to_numpy()

    for objet in range(n_objets):
        # Cauculer les distances avec les centroids
        distances = np.sum(
            np.square(centroids_arr - data.iloc[objet, :2].to_numpy()), axis=1)
        # Calculer le centroid le plus proche et ca distance
        centroid_plus_proche = np.argmin(distances)
        centroid_distance = np.min(distances)

        # Assigner les les meilleurs centroids aux objets
        centroid_assign.append(centroid_plus_proche)
        centroid_distances.append(centroid_distance)

    # retourner les deux listes l'assignation avec index, et les distances
    return (centroid_assign, centroid_distances)

def kmeans(data, k):
    # Initialiser les centroids et les distances
    centroids = initialiser_centroids(k, data)
    distance = []
    compr = True        # pour tester la boucle
    i = 0
    while (compr):
        # calculer les centroids et la distance , et l'assignation
        data['centroid'], iter_distance = assigner_centroid(data, centroids)
        #Ajouter la somme des distances renvoyé par assigner_centroid pour voir si les centroids sont fix ou pas
        distance.append(sum(iter_distance))
        # Recalculer les centres des clusters et MAJ leur nouveaux coordonnes
        centroids = data.groupby('centroid').agg('mean').reset_index(drop=True)

        # Vérifier si on a changé ou pas
        if (len(distance) < 2):
            # Ici pour skiper la premiere iteratin car on ne peut pas comparer
            compr = True   
        else:
            if (round(distance[i], 3) != round(distance[i-1], 3)):
                compr = True
            else:
                # Cas de convergence
                compr = False
        i = i + 1
    data['centroid'], iter_distance = assigner_centroid(data, centroids)
    centroids = data.groupby('centroid').agg('mean').reset_index(drop=True)
    return (data['centroid'], iter_distance, centroids)

def kmeans_elbow(data):
    '''

    '''
    # Initialiser les variables
    distances = []
    max_k = min(len(data), 10)
    
    # processus iteratif sur les valeurs de K
    for k in range(1, max_k + 1):
        
        data['centroid'], iter_distance, centroids = kmeans(data, k)
        distance = sum(iter_distance)

        # Sauvegarder les distances
        distances.append(distance)

    # Plot elbow curve
    plt.plot(range(1, max_k + 1), distances)
    plt.title('Elbow Curve')
    plt.xlabel('Number of clusters')
    plt.ylabel('Sum of squared distances')
    plt.show()

    # Determiner le meilleur nombre de K
    elbow_index = np.argmin(np.diff(distances)) + 1
    meilleur_k = elbow_index + 1
    print("Meilleur K :", meilleur_k+1)

    # Perform K-means clustering with best k
    centroids = initialiser_centroids(meilleur_k, data)
    data['centroid'], iter_distance = assigner_centroid(data, centroids)
    centroids = data.groupby('centroid').agg('mean').reset_index(drop=True)

    return (data['centroid'], iter_distance, centroids)


# Callback functions 

def afficher_objets(sender, app_data, user_data):
    global k 

    k = dpg.get_value("input_k")
    n = dpg.get_value("input_n")

    X, _ = make_blobs(n_samples=n, centers=k, n_features=2,
                    shuffle=True, random_state=41)

    # Créer un DataFrame à partir de X
    global data
    data = pd.DataFrame(X, columns=['x', 'y'])

    # Afficher les données avec Matplotlib
    plt.scatter(X[:, 0], X[:, 1], c='blue', s=10)
    plt.title('Objets')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    

def execute_kmeans(sender, app_data, user_data):

    global data
    global k 

    data_centroids, _, centroids = kmeans(data, k)
    # data_centroids, _, centroids = knn_elbow(data)
    print(data_centroids)
    colors = {0: 'red', 1: 'blue', 2: 'green',
            3: 'purple', 4: 'orange', 5: 'gray', 6: 'pink'}
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1],  marker='o',
                c=data['centroid'].apply(lambda x: colors[x]), alpha=0.5)
    plt.scatter(centroids.iloc[:, 0], centroids.iloc[:, 1],  marker='o', s=100,
                c=centroids.index.map(lambda x: colors[x]))
    plt.show()


def execute_elbow(sender, app_data, user_data):
    global data
    dpg.configure_item("loading", show=True)
    kmeans_elbow(data) 
    dpg.configure_item("loading", show=False)



    



dpg.create_context()
       
dpg.set_global_font_scale(1.75)
with dpg.window(label="Kmeans", no_resize=True, no_close=True,no_open_over_existing_popup=True,
    width=1080, height=720, no_collapse=True, no_move=True ): 
    dpg.add_text('TP FD\nRéalisé par  OMARI Hamza\nHAMZAOUI Thameur')
    dpg.add_input_int(tag="input_k", label="Nomre de clusters")
    dpg.add_input_int(tag="input_n", label="Nombre d'objets")

    dpg.add_button(tag="btn_show_data", label="Afficher les objets", callback=afficher_objets)

    dpg.add_button(tag="btn_execute_kmeans", label="Executer K means", callback=execute_kmeans)        

    dpg.add_button(tag="btn_execute_kmeanselbow", label="Executer la méthode Elbow", callback = execute_elbow )
    
    dpg.add_loading_indicator(tag="loading", show=False)


# Dearpygui inits stuff: 


dpg.create_viewport(title='Apriori And close', width=1080, height=720, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
