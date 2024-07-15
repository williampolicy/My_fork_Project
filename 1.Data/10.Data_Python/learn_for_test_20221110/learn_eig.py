
import numpy as np
  
  
mat = np.mat("1 -2;1 3")
  
# Original matrix
print(mat)
print("")
evalue, evect = np.linalg.eig(mat)
  
# Eigenvalues of the said matrix"
print(evalue)
print("")
  
# Eigenvectors of the said matrix
print(evect)
