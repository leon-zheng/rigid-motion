import numpy as np
from quaternion import Quaternion as Q

#初始坐标
pc = np.array([np.sqrt(2), np.sqrt(2), 0])

#旋转向量
n = np.array([0, 0, 1])

#旋转角度，逆时针为正方向
theta = np.pi/4

qRe = n * np.sin(theta/2)           #旋转四元数实部
qIm = np.cos(theta/2)               #旋转四元数虚部
q = Q(np.append(qRe, qIm))
p = Q(np.append(pc, 0))              #初始坐标四元数
result = q.rotate(p)                #旋转坐标四元数
result = np.array([result.x, result.y, result.z])
print(result,'is rotated',180*theta/np.pi,'degree around',n,'by',pc)