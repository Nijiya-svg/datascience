import numpy
matrix1=numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix2=numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("matrix1:\n",matrix1)
print("matrix2:\n",matrix2)
matrix3=numpy.add(matrix1,matrix2)
matrix4=numpy.subtract(matrix1,matrix2)
matrix5=numpy.matmul(matrix1,matrix2)
matrix6=numpy.transpose(matrix1)
print("matrix1+matrix2=\n",matrix3)
print("matrix1-matrix2=\n",matrix4)
print("matrix1*matrix2=\n",matrix5)
print("2*matrix1=\n",2*matrix1)
print("transpose of matrix1=\n",matrix6)




