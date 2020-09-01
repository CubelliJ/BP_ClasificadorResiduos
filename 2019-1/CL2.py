#Clasificado.py

import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras import applications
from tensorflow.python.keras.models import Sequential 
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation




largo=224
alto=224
modelo='Modelo/modelo.h5'
pesos='Modelo/pesos.h5'
#cnn.load_weights(pesos)

weights_model='Modelo/pesos.h5'  # my already trained weights .h5

vgg=applications.vgg16.VGG16()
cnn=Sequential()
for capa in vgg.layers:
    cnn.add(capa)
cnn.pop()
#for layer in cnn.layers:
#    layer.trainable=False
cnn.add(Dense(3,activation='softmax'))  

cnn.load_weights(weights_model)

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

x= Clasificar('t_19.jpg')
print(x)