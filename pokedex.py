import requests
import matplotlib.pyplot as plt
import matplotlib.image as img


pokemon = input("Introduce el nombre de un Pokemon: ")# Solicitamos al usuario el nombre de un pokemon
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon # buscamos en la api y concatenamos el nombre del pokemon 
res = requests.get(url)# obtenmos el resultado y lo guardamos en la variables

if res.status_code != 200: # nos aseguramos de que el pokemon ingresado sea verdadero y exista en la api (el status 200 significa que todo va bien) por ende todo lo que no sea un stattus code de 200 seria un error
    print("no se ha encontrado ningun pokemon")
    exit()

imagen = img.imread(res.json()['sprites']["front_default"])# imagen frintal 
plt.title(res.json()["name"]) #mostramos en un json el resultado obtenido a partir del nombre del pokemom y de titulo ponemos su nombre
imgplot= plt.imshow(imagen)#mostramos la igamen del pokemon 
plt.show()