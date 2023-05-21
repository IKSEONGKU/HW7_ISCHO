import numpy as np
#eigenvalues, eigenvectors, determinant
#vec1 = [1,2,3]
#vec2 = [4,5,6]
def main():
    arr = np.array([[1,2],[3,4]])
    eig_val, eig_vec = np.linalg.eig(arr)
    print('Eigenvalue:', eig_val)
    print('Eigenvector:', eig_vec)
    print('Determinant:', np.linalg.det(arr))

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])

    product = np.cross(vec1,vec2)
    print('Cross product:', product)

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])

    x = np.linalg.solve(A,b)
    print('Solution:', x)

if __name__=='__main__':
    main()
