import numpy as np
#cria classe Tbit inicializando uma media M privada
class Tbit:
  def __init__( self, matriz):
    self.__M = np.average(matriz)
    self.matriz = matriz

#define o filtro da expressao 
#  255 se f(x,y) >  M 
#  0   se f(x,y) <= M   
  def FILTRO(self):
    for r in range(0,len(self.matriz)):
      for g in range(0,len(self.matriz[r])):
        for b in range(0,len(self.matriz[r][g])):
          if self.matriz[r][g][b] > self.getMedia():
            self.matriz[r][g][b] = 255
          else:
            self.matriz[r][g][b] = 0
    return self.matriz

 #get M privado 
  def getMedia(self):
    return self.__M
