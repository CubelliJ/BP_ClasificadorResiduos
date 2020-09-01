# CODIGO PRINCIPAL Version 00

import numpy as np
import cv2 
#import Clasificar
import serial
from PIL import Image

import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

class TrashDetector:
    # Constructor
    def __init__(self, com='COM5', baudrate=9600, camPort=0):
        self.ser = serial.Serial(com, baudrate)
        self.camera = cv2.VideoCapture(camPort)
        self.receivedMsg = None # message received from the Arduino
        self.frame = None # Image read from the USB camera
        
        # calibration
        self.isCalibrated = False
        self.numImagesForCalibration = 2
        self.counterImagesForCalibration = 0
        self.backgroundModel = None
        self.backgroundStd = None
        self.listImagesCalibration = []
        
        # CNN parameters
        self.cnnWidth=100
        self.cnnHeight=100
        self.cnnModel='Modelo/basura_f.model'
        #self.cnnWeights='Modelo/pesos.h5'
        self.cnnNet=load_model(self.cnnModel)
        #self.cnnNet.load_weights(self.cnnWeights)
        self.cnnLabel = None # The predicted class
        
        self.cnnClasses={0: "Botella",
                         1: "Lata",
                         2: "Tetrapack"}
    def __del__(self):
        self.ser.close()
        self.camera.release()
        
    def run(self):
        while(True):
            #if not self.isCalibrated:
            #    self.captureImage()
            #    self.calibrateBackgroundModel()
            #else:
            #    print("CASO CALIBRADO")
            # Check if the Arduino detected something with the US sensor
            self.readSerial()    
            
            if self.receivedMsg is not None:
                # Capture image from USB
                self.captureImage()
                # Aca recortamos la imagen usando el modelo de fondo
                #self.cropObject()
                # Clasify object by using ML
                self.objectRecognition()
            
                # Send command back to arduino
                self.sendSerial()
        
    def readSerial(self):
        line = self.ser.readline()
        print("Read Serial: " + str(line) )
        if line is not None:
            self.receivedMsg = line.decode('utf-8')
        else:
            self.receiveMsg = None
   
    def captureImage(self):
         print("capturando imagen")
         cap=cv2.VideoCapture(0) 
         _,self.frame = cap.read()
    
    def objectRecognition(self):
        # cambiar tamaño de imagen
        #self.frameResized = self.frame
        cv2.imwrite(r'C:\Users\Asus\Desktop\MachineLearning\Residuo.png', self.frame)
        self.frameResized=load_img(r'C:\Users\Asus\Desktop\MachineLearning\Residuo.png', target_size=(self.cnnWidth,self.cnnHeight))        
        self.frameResized = img_to_array(self.frameResized)
        self.frameResized = np.expand_dims(self.frameResized, axis=0)
        out = self.cnnNet.predict(self.frameResized)
        print(out)
        classes = out[0]
        predictedClass=np.argmax(classes)
        
        self.cnnLabel = predictedClass
        print("Object Recognition: Detected a " + self.cnnClasses[self.cnnLabel])
    
    def sendSerial(self):
        self.ser.write(str(self.cnnLabel).encode())
        print(self.cnnLabel)

# Crear programa
detector = TrashDetector()
# Ejecutar 
detector.run()


