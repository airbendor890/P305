import numpy as np
from numpy import linalg as LA

k=300	#number of atoms
b=[-0.01,-0.1,-0.5,-1,-2,-3]	#interaction term beta
E1=-10	#Ground state energy E_0 when far away(Diatomic chain)
E2=-12

A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[0]
		A[i+1][i]=b[0]
A[0][k-1]=b[0]
A[k-1][0]=b[0]

#print(A)
w=LA.eigvals(A)

f = open("Bdata1.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()
############################################################################

A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[1]
		A[i+1][i]=b[1]
A[0][k-1]=b[1]
A[k-1][0]=b[1]

#print(A)
w=LA.eigvals(A)

f = open("Bdata2.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()

#################################
A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[2]
		A[i+1][i]=b[2]
A[0][k-1]=b[2]
A[k-1][0]=b[2]

#print(A)
w=LA.eigvals(A)

f = open("Bdata3.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[3]
		A[i+1][i]=b[3]
A[0][k-1]=b[3]
A[k-1][0]=b[3]

#print(A)
w=LA.eigvals(A)

f = open("Bdata4.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()
####################################

A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[4]
		A[i+1][i]=b[4]
A[0][k-1]=b[4]
A[k-1][0]=b[4]

#print(A)
w=LA.eigvals(A)

f = open("Bdata5.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()
#################################
A=np.zeros((k,k))

for i in range(k):
	if i%2==0:
		A[i][i]=E1
	else:
		A[i][i]=E2
for i in range(k-1):
		A[i][i+1]=b[5]
		A[i+1][i]=b[5]
A[0][k-1]=b[5]
A[k-1][0]=b[5]

#print(A)
w=LA.eigvals(A)

f = open("Bdata6.txt", "w")
for i in range(k):
	f.write("%5.5f\n" %(w[i]))
f.close()
################################
