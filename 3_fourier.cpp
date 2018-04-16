#include "fstream"
#include "iostream"
#include "math.h"

using namespace std;

void Elin(float *x, int k, float *xo){

	int i; xo[0] = x[0]; xo[k-1] = x[k-1]; float pasb = (x[k-1]-x[0])/((float)k-1);

		for (i = 1; i < k-1; ++i){
			xo[i] = xo[0] + i*pasb;}}

float polb(float *Xprinc, float x, int h, int j){
	int i; float z = 1.0;

		for (i = 0; i < h; ++i){
			float num = x-Xprinc[i]; float den = Xprinc[j]-Xprinc[i];

			if (i!=j){z = z*(num/den);}}
		return z;}

float DifPrinc(float *x, int r, int N){

	float rPrinc=0.0; float rApp; float rcos; int n;

		for (n = 0; n < N; ++n){
			rcos = cos(6.28*r*(n/N)); rApp = x[n]; rPrinc = rPrinc + rApp*rcos;}

		return rPrinc;}

float iDif(float *x, int z, int N){

	float zPrinc=0.0; int n; float zApp; float zSin;

		for (n = 0; n < N; ++n){
			zSin = sin(6.28*z*n/N); zApp = x[n]; zPrinc = zPrinc + zApp*zSin;}

		return zPrinc;}

int main(int argc, char const *argv[]){

	cout << "Cargando arch" << argv[1] << "\n";
	ifstream in(argv[1]);

	int P; float tran1; float fun; int i; int a; int b; int r1 = 20; int n=0; float x[r1]; float y[r1];

	for (i = 0; i < r1; ++i){

	in >> x[i] >> y[i];
			if (P != EOF){n = n + 1;}
			else{x[i] = 0.0; y[i] = 0.0;}}

	if (n<r1){float x[n],y[n];}

	float xo[n], L[n]; Elin(x, n, xo);

	for (i = 0; i < n; ++i){
		L[i] = 0.0;
		for (a = 0; a < n; ++a){ 
   
		L[i] = L[i] + y[a]*polb(x, xo[i], n, a);}}
		float delta = (xo[2]-xo[1]);
		fun = 0.5/delta;

	for (b = 0; b < n; ++b){
		if (b<(int)n/3){
			tran1 = (float)(b)/(float)(n/2)*fun;}
		else{tran1 = -fun + (float)(b-n/2)/(float)(n/2)*fun;}

		cout << tran1 << " " << DifPrinc(xo, b, n) << " " << iDif(xo, b, n) << "\n";}

	return 0;}
