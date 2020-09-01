#Clasificado.py

import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

largo=100
alto=100
modelo='Modelo/modelo.h5'
pesos='Modelo/pesos.h5'
cnn=load_model(modelo)
cnn.load_weights(pesos)



def Clasificar(file):
    x=load_img(file, target_size=(largo,alto))
    x=img_to_array(x)
    x=np.expand_dims(x, axis=0)
    arreglo=cnn.predict(x)
    print(arreglo)
    resultado=arreglo[0]
    respuesta=np.argmax(resultado)
    if respuesta==0:
        clase = "Botella"
    elif respuesta==1:
        clase = "Lata"
    elif respuesta==2:
        clase = "Tetrapak"
    return clase

x=Clasificar('.png')
print(x)

#T02 - LATA
#T05 - LATA
#T06 - LATA