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

imagen_imput = argv[1]
Imagen = plt.imread(imagen_imput)
Imagen = Imagen[40:80,:160]
FourImagen = four2(Imagen)

krnl = argv[2]
nk = float(krnl)

lin = np.linspace(-nk,nk,int(1.6*nk))
n = len(lin)
x1 = np.reshape(lin,(n,1))
x2 = np.reshape(lin,(1,n))
argk1 = -nk/2.35*x1**2
argk2 = -nk/4*x2**2
k = np.exp(argk1)*np.exp(argk2)

m0,n0 = np.shape(k)
K = np.zeros(np.shape(Imagen))
K[:m0,:n0] = k

K_ft = four2(K) 
gA = K_ft*FourImagen
gI = ifour(gA.real, gA.imag)

plt.figure(); plt.imshow(gI.real, cmap='gray')
plt.savefig('suave.png')
