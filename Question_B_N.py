import numpy as np
from numpy import linalg as LA

k=[10,50,100,200,500,1000]	#number of atoms
b=-2	#interaction term beta
E1=-10	#Ground state energy E_0 when far away(Diatomic chain)
E2=-12
#############################################################################
A=np.zeros((k[0],k[0]))

for i in range(k[0]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[0]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata1.txt", "w")
for i in range(k[0]):
	f.write("%5.5f\n" %(w[i]))
f.close()
############################################################################

A=np.zeros((k[1],k[1]))

for i in range(k[1]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[1]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata2.txt", "w")
for i in range(k[1]):
	f.write("%5.5f\n" %(w[i]))
f.close()

#################################
A=np.zeros((k[2],k[2]))

for i in range(k[2]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[2]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata3.txt", "w")
for i in range(k[2]):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
A=np.zeros((k[3],k[3]))

for i in range(k[3]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[3]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata4.txt", "w")
for i in range(k[3]):
	f.write("%5.5f\n" %(w[i]))
f.close()
####################################

A=np.zeros((k[4],k[4]))

for i in range(k[4]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[4]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata5.txt", "w")
for i in range(k[4]):
	f.write("%5.5f\n" %(w[i]))
f.close()
#################################
A=np.zeros((k[5],k[5]))

for i in range(k[5]):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k[5]-1):
		A[i][i+1]=b
		A[i+1][i]=b

#print(A)
w=LA.eigvals(A)

f = open("BNdata6.txt", "w")
for i in range(k[5]):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
