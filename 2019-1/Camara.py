# CODIGO PRINCIPAL Version 00

import numpy as np
import cv2 
import Clasificar
import serial

def CamaraLearning():
    with serial.Serial('COM3', 9600) as ser:
        while 1: 
            line = ser.readline()
            if line is not None:
                TextoRecibido = line.decode('utf-8')
            break
    cap=cv2.VideoCapture(0) 
    
    while 1:
        _,frame = cap.read()
        cv2.imwrite(r'C:\Users\Asus\Desktop\MachineLearning\Residuo.png', frame)
        Clasificar.Clasificar(r'C:\Users\Asus\Desktop\MachineLearning\Residuo.png')
        break
    cap.release()
