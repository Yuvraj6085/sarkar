import numpy as np
np.array([1,2,3])
np.arange(1,10,2)
np.zeros((2,3))
np.ones((3,3))
np.full((2,2), 5)
np.linspace(0, 10, 5)
np.eye(3)
np.identity(3)
a = np.array([[1,2,3],[4,5,6]])



a.ndim	
a.shape	
a.size	
a.dtype	
a.itemsize

a[0,1]
a[:,1]
a[1,:]
a[0:2,1:3]

a[a > 3]


a.reshape(3,2)
a.flatten()
a.T

a + b
a - b
a * b
a / b

np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)



mean()	
median()
sum()	
min() / max()	
std()	
var()
argmin() / argmax()

np.mean(a)
np.max(a)
np.std(a)

np.sum(a, axis=0)   # column wise
np.sum(a, axis=1)   # row wise

np.random.rand(3,3)
np.random.randn(3,3)
np.random.randint(1,100,10)
np.random.choice([1,2,3,4])
np.random.shuffle(a)
np.random.seed(10)


np.sort(a)
np.argsort(a)
np.where(a > 5)
np.unique(a)


np.vstack((a,b))
np.hstack((a,b))
np.concatenate((a,b))


np.split(a,2)
np.hsplit(a,2)
np.vsplit(a,2)


np.dot(a,b)
np.matmul(a,b)
np.linalg.det(a)
np.linalg.inv(a)
np.linalg.eig(a)
np.linalg.solve(a,b)

np.sin(a)
np.cos(a)
np.tan(a)
np.sqrt(a)
np.log(a)
np.exp(a)
np.abs(a)
np.power(a,2)


a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
a + b

b = a.copy()
c = a.view()


np.save("data.npy", a)
np.load("data.npy")

np.savetxt("data.csv", a, delimiter=",")
np.loadtxt("data.csv", delimiter=",")


a.astype(int)
a.astype(float)


%timeit a + b


np.isnan(a)
np.isinf(a)
np.nan_to_num(a)
