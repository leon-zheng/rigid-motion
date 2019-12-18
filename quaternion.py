class Quaternion:
    def __init__(self, array):
        if len(array) == 4:
            self.z = array[2]
            self.w = array[3]
        elif len(array) == 3:
            self.z = array[2]
            self.w = 0
        elif len(array) == 2:
            self.z = 0
            self.w = 0
        else:
            raise ValueError('Unsupported array length.\n')
        self.x = array[0]
        self.y = array[1]
        self.array = [self.x, self.y, self.z, self.w]
    def toArray(self):
        return [self.x, self.y, self.z, self.w]
    def add(self, quaternion):
        result = Quaternion(self.array)
        result.w += quaternion.w
        result.x += quaternion.x
        result.y += quaternion.y
        result.z += quaternion.z
        return result
    def sub(self, quaternion):
        result = Quaternion(self.array)
        result.w -= quaternion.w
        result.x -= quaternion.x
        result.y -= quaternion.y
        result.z -= quaternion.z
        return result
    def mul(self, quaternion):
        result = Quaternion(self.array)
        result.w = self.w*quaternion.w - self.x*quaternion.x \
                 - self.y*quaternion.y - self.z*quaternion.z
        result.x = self.w*quaternion.x + self.x*quaternion.w \
                 + self.y*quaternion.z - self.z*quaternion.y
        result.y = self.w*quaternion.y - self.x*quaternion.z \
                 + self.y*quaternion.w + self.z*quaternion.x
        result.z = self.w*quaternion.z + self.x*quaternion.y \
                 - self.y*quaternion.x + self.z*quaternion.w
        return result
    def div(self, quaternion):
        result = Quaternion(self.array)
        return result.mul(quaternion.inverse())
    def mod(self):
        return pow((pow(self.x,2)+pow(self.y,2)+pow(self.z,2)+pow(self.w,2)),1/2)
    def star(self):
        result = Quaternion(self.array)
        result.w = self.w
        result.x = -self.x
        result.y = -self.y
        result.z = -self.z
        return result
    def inverse(self):
        result = Quaternion(self.array).star()
        mod = self.mod()
        deno = mod ** 2
        result.w /= deno
        result.x /= deno
        result.y /= deno
        result.z /= deno
        return result
    def rotate(self, quaternion):
        q = Quaternion(self.array)
        result = q.mul(quaternion).mul(q.inverse())
        return result
    def __str__(self):
        return str(self.x) + "i " + str(self.y) + "j " + \
               str(self.z) + "k " + str(self.w)