from numpy import array, sqrt, pi, sin, cos, append
from quaternion import Quaternion as Q

#初始坐标
pc = array([sqrt(2), sqrt(2), 0])

#旋转向量
n = array([0, 0, 1])

#旋转角度，逆时针为正方向
theta = pi/4

qRe = n * sin(theta/2)           #旋转四元数实部
qIm = cos(theta/2)               #旋转四元数虚部
q = Q(append(qRe, qIm))
p = Q(append(pc, 0))             #初始坐标四元数
result = q.rotate(p)                #旋转坐标四元数
result = array([result.x, result.y, result.z])
print(result,'is rotated',180*theta/pi,'degree around',n,'by',pc)