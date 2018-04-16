import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def ifour(real1,imag1):

    Areal = np.zeros(np.shape(real1))
   
    shap = np.shape(Areal)

    Ao = shap[0]
    Bo = shap[1]
    
    grid1,grid2 = np.meshgrid(np.arange(Bo),np.arange(Ao))
    
    for i in range(Ao):
        for p in range(Bo):

	    arg = grid2*i/Ao+grid1*p/Bo
            numero_pi = np.pi
            doblepi = 2*numero_pi
	    matR = real1[:,:]
            matI = imag1[:,:]
            coseno = np.cos(doblepi*(arg))
            suma_cos = np.sum(matR*coseno,(0,1))
            seno = np.sin(doblepi*(arg))
            suma_sen = np.sum(matI*seno,(0,1))

            Areal[i,p] = suma_cos
            Areal[i,p] = Areal[i,p]- suma_sen
         
    return Areal

def four2(x):

    form = np.shape(x)
    real= np.zeros(form)
    imag = np.zeros(form)

    A = form[0]
    B = form[1]

    arrA = np.arange(A)
    arrB = np.arange(B)
    a,b = np.meshgrid(arrB,arrA)
    
    for i in range(A):
        for k in range(B):

	    numero_pi = np.pi
	    arg = b*i/A+a*k/B
            doblepi = -2*numero_pi

            Argcoseno = np.cos(doblepi*(arg))
	    Argsen = np.sin(doblepi*(arg))
	    
            matx = x[:,:]
	    
            suma_cos = np.sum(matx*Argcoseno, (0,1))
	    suma_sen = np.sum(matx*Argsen, (0,1))

            real[i,k] = suma_cos
            imag[i,k] = suma_sen
	    imaginario = 1j*imag

    return real + imaginario

def Giro(X):

    A,B = np.shape(X)

    Y = np.roll(X,int(A/2),0)
    X = np.roll(Y,int(B/2),1)

    return X

imagen_imput = argv[1]
Imagen = plt.imread(imagen_imput)
Imagen = Imagen[40:80,:160]
FourImagen = four2(Imagen)
tam1 = np.size(FourImagen,1)
tam2 = np.size(FourImagen,0)
m,n = np.meshgrid(np.arange(tam1)-tam1/2, np.arange(tam2)-tam2/2)

f = np.sqrt(m**2 + n**2)
F = np.zeros(np.shape(FourImagen))
F[f<15] = 1
ii = np.logical_and(f>15, f<25)

numero_pii=np.pi
argumf = 1-np.sin(numero_pii*(f[ii]-20)/(10))
F[ii] = 0.5*(argumf)
Fbajas = F
Faltas = 1.0-F

altas = argv[2]=='altas'

bajas = argv[2]=='bajas'

if altas:

	FI2altas = Giro(Giro(FourImagen)*Faltas)

	IFaltas = ifour(FI2altas.real, FI2altas.imag)

	plt.figure()
	plt.imshow(IFaltas,cmap='gray')

	plt.savefig('altas.png')
if bajas:

	FI2bajas = Giro(Giro(FourImagen)*Fbajas)

	IFbajas = ifour(FI2bajas.real, FI2bajas.imag)

	plt.figure()
	plt.imshow(IFbajas,cmap='gray')

	plt.savefig('bajas.png')

