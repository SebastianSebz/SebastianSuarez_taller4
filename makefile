All: altas.png transformada.txt suave.png

transformada.txt: fourier datos.txt
	./fourier datos.txt | tail -n +2  > transformada.txt
	cat transformada.txt

fourier: 3_fourier.cpp
	g++ 3_fourier.cpp -o fourier

altas.png: 2_filtro.py
	python 2_filtro.py monkey.png altas
	python 2_filtro.py monkey.png bajas

suave.png: 1_suave.py
	python 1_suave.py monkey.png 15

rm:
	rm altas.png bajas.png suave.png transformada.txt
