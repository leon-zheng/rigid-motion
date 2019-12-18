from sympy import sqrt, sin, cos, pi
from quaternion import Quaternion as Q

#初始坐标
p = [sqrt(2).evalf(), sqrt(2).evalf()]

#旋转角度，逆时针为正方向
theta = (pi/4).evalf()

r = [0, 0, sin(theta/2), cos(theta/2)]    #旋转四元数
rq = Q(r)
pq = Q(p)                                 #初始坐标四元数
result = rq.rotate(pq)                    #旋转坐标四元数
result = [result.x, result.y, result.z]
print(result[:2],'is rotated',(180*theta/pi).evalf(),'degree by',p)