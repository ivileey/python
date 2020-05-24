
import numpy as np
# 创建一个矩阵A
A = np.array([[0,1],[1,1],[1,0]])
# 对其进行SVD分解
u, s, vt = np.linalg.svd(A, full_matrices=True)
print(u.shape, s.shape, vt.shape)
print(u, s, vt.T)