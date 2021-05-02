import numpy as np
from numpy import linalg as LA

k=[10,50,100,200,500,1000]	#number of atoms
b=-2	#interaction term beta
E=-10	#Ground state energy E_0 when far away

A=np.zeros((k[0],k[0]))

for i in range(k[0]):
	A[i][i]=E
for i in range(k[0]-1):
		A[i][i+1]=b
		A[i+1][i]=b

A[0][k[0]-1]=A[k[0]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata1.txt", "w")
for i in range(k[0]):
	f.write("%5.5f\n" %(w[i]))
f.close()
############################################################################

A=np.zeros((k[1],k[1]))

for i in range(k[1]):
	A[i][i]=E
for i in range(k[1]-1):
		A[i][i+1]=b
		A[i+1][i]=b
A[0][k[1]-1]=A[k[1]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata2.txt", "w")
for i in range(k[1]):
	f.write("%5.5f\n" %(w[i]))
f.close()

#################################
A=np.zeros((k[2],k[2]))

for i in range(k[2]):
	A[i][i]=E
for i in range(k[2]-1):
		A[i][i+1]=b
		A[i+1][i]=b
A[0][k[2]-1]=A[k[2]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata3.txt", "w")
for i in range(k[2]):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
A=np.zeros((k[3],k[3]))

for i in range(k[3]):
	A[i][i]=E
for i in range(k[3]-1):
		A[i][i+1]=b
		A[i+1][i]=b
A[0][k[3]-1]=A[k[3]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata4.txt", "w")
for i in range(k[3]):
	f.write("%5.5f\n" %(w[i]))
f.close()
####################################

A=np.zeros((k[4],k[4]))

for i in range(k[4]):
	A[i][i]=E
for i in range(k[4]-1):
		A[i][i+1]=b
		A[i+1][i]=b
A[0][k[4]-1]=A[k[4]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata5.txt", "w")
for i in range(k[4]):
	f.write("%5.5f\n" %(w[i]))
f.close()
#################################
A=np.zeros((k[5],k[5]))

for i in range(k[5]):
	A[i][i]=E
for i in range(k[5]-1):
		A[i][i+1]=b
		A[i+1][i]=b
A[0][k[5]-1]=A[k[5]-1][0]=b
#print(A)
w=LA.eigvals(A)

f = open("ANdata6.txt", "w")
for i in range(k[5]):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
