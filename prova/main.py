from PIL import Image
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
from Tbit import *

#Leitura imagem
im = Image.open('Chaplin.jpg')
#atribuir imagem a uma matriz
matriz = array(im)
#camadas de cinza
im = np.array(Image.open('Chaplin.jpg').convert('L')) 
gr_im = Image.fromarray(im).save('gr_Chaplin.png')

#Cria objeto media da classe Tbit passando a matriz 
media = Tbit(matriz)
#Aplica metodo FILTRO da classe Tbit
matriz = media.FILTRO()

#Imprime nova matriz
print(matriz)
#Imprime nova imagem
plt.imshow(matriz)
#Salvando arquivo
plt.savefig('threshold.png', format='png')
#Plotando nova imagem
plt.show()
