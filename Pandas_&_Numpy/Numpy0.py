import numpy as np
a = np.array([[1,2,3],[3,2,1],[1,2,3],[1,2,3]])
# print(a[:,:])
# print(a[:,1:len(a)-1])
# print(a.ndim)
# print(a.itemsize)
# print(a.dtype)
# print(a.size)
# print(a.shape)
# print(np.ones((3,3)))
# print(np.arange(1,10,3))
# np.linspace(1,10,2)
# print(a.reshape((3,4)))
# print(a.ravel())
# print(a.sum(0))
# b = np.array([3,4,3])
# print(b)
# print(3*4)
# print(a.dot(b))
# for r in a:
#     print(r)
# for r in a.flat:
#     print(r)
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print(a)
print(b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
a = np.arange(30).reshape(2,15)
np.hsplit(a,3)
k = a>3
print(k)
print(a[k])