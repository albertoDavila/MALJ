import glob
import math
from pathlib import Path
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import os

def transformCordinates(coordinates, wmax, hmax):
    #funcion que toma las coordenadas polares el ancho y el alto y las debe transformar a rectangulares
    return ()

def generateArray(file):
    with open(file, "r") as f:
        arr = f.read().splitlines()
    arr_len = len(arr)
    i = 0    
    # regex
    rg = re.compile("(\d)*_(\d)*_(\d)*_big")
    output = []
    while i != arr_len:
        val = arr[i] # nombre de la imagen
        mtch = rg.match(val)
        if mtch:
            try:
                di = dict() #diccionario
                val = "{}.jpg".format(val)
                di["name"] = val
                #  matplotlib
                img = mpimg.imread(os.path.join("dataset", val))
                fig,ax = plt.subplots(1)
                ax.imshow(img)               
                (h, w, _) = img.shape
                jumps = int(arr[i+1])
                temp = []
                for j in range(0, jumps):
                    coords = arr[i + j +2]
                    temp.append(coords)
                    # transformCordinates(string, w, h)
                    # rec = (x , y , width, height)
                    rect = patches.Rectangle(
                        (rec[0],rec[1]),rec[2],rec[3],
                        linewidth=1,
                        edgecolor='r',
                        facecolor='none')
                    ax.add_patch(rect)
                plt.show()
                di["annotations"] = temp
                output.append(di)
                # i = 
            except:
                print("{} not found...".format(val))
                i+=1
        else:
            i+=1
    return output        

def returnEllipseListFiles(path):
    return [str(f) for f in Path(path).glob('**/*-ellipseList.txt')]

folder = glob.glob("dataset/*.jpg")
folder = pd.Series(folder)
files = returnEllipseListFiles("labels")

#genera un arreglo por etiqueta .. total tendremos arreglos de arreglos 
directionary = [generateArray(f) for f in files]
