
import numpy as np
import os
from PIL import Image
from tqdm import tqdm
# 定义恢复函数，由分解后的矩阵恢复到原矩阵
def restore(u, s, v, K):
    m, n = len(u), len(v[0])
    a = np.zeros((m, n))
    for k in range(K):
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
# 前k个奇异值的加总
        a += s[k] * np.dot(uk, vk)
    a = a.clip(0, 255)
    return np.rint(a).astype('uint8')
A = np.array(Image.open("./ml_lab.jpg", 'r'))
# 对RGB图像进行奇异值分解
u_r, s_r, v_r = np.linalg.svd(A[:, :, 0])
u_g, s_g, v_g = np.linalg.svd(A[:, :, 1])
u_b, s_b, v_b = np.linalg.svd(A[:, :, 2])
# 使用前50个奇异值
K = 50
output_path = r'./svd_pic'
# 恢复图像
for k in tqdm(range(1, K+1)):
    R = restore(u_r, s_r, v_r, k)
    G = restore(u_g, s_g, v_g, k)
    B = restore(u_b, s_b, v_b, k)
    I = np.stack((R, G, B), axis=2)
    Image.fromarray(I).save('%s\\svd_%d.jpg' % (output_path, k))