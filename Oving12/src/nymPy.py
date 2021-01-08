import numpy as np


# axis = 0 follow down the rows
# axis = 1 follow across the rows

class numpyTest:

    def basics(self):
        # Initialize array
        a = np.array([1, 2, 3])  # single array
        print("Data for array a:")
        print(a)
        print("Dimension: " + str(a.ndim))  # dimension of a
        print("Shape of a: " + str(a.shape))  # Shape of a. Vector (3,)
        print("Type of data in memory: " + str(a.dtype))  # Type of data ("int32"). Memory it takes up
        a = np.array([1, 2, 3], dtype='int16')
        print("Type of data in memory after change: " + str(a.dtype))  # Type of data ("int16"). Memory it takes up
        print("Byte size of an item: " + str(a.itemsize))  # byte size of an item in array
        print("Total bytesize of array: " + str(a.nbytes))  # Total byte size array
        print()
        print("Data for array b:")
        b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])  # double array float
        print(b)
        print("Dimension: " + str(b.ndim))  # dimension of b
        print("Shape of b: " + str(b.shape))  # Shape of b. Vector (2,3) 2 rows, 3 columns

    def accessChangeArray(self):
        a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
        # Get specific element [Row, column]
        print(a)
        print("Get value at [1, 5]: " + str(a[1, 5]))  # [1, -2] = 13. Counts backwards
        print("Get specific row [0, :]: " + str(a[0, :]))
        print("Get specific column [:, 2]: " + str(a[:, 2]))
        # Getting a little more fancy
        # [Startindex:endindex:stepsize]
        print("Get every other number between start and stop: " + str(a[0, 1: 6: 2]))
        a[1, 5] = 20  # Change value
        print(a)
        a[:, 5] = [1, 2]  # Change column

        # 3D array
        b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print("3D array: ")
        print(b)
        print("Spesific element: " + str(b[0, 1, 1]))
        b[:, 1, :] = [[9, 9], [8, 8]]

    def difArrays(self):
        a = np.zeros((3, 3))
        print("All 0 matrix:\n " + str(a))
        print("All 1 matrix:\n " + str(np.ones((3, 3))))
        print("Other matrix ((shape), value): ")
        print(np.full((2, 2), 99))
        print("Other matrix. Use shape defined:")
        print(np.full_like(a, 99))
        print("Random decimal numbers:")
        print(np.random.rand(4, 2))
        print("Random int numbers:")
        print(np.random.randint(7, size=(3, 3)))
        print("Identity matrix:")
        print(np.identity(3))
        print("Repeat:")
        arr = np.array([[1, 2, 3]])
        r1 = np.repeat(arr, 3, axis=0)
        print(r1)

    # How to make a gven array showed on video
    def initArray(self):
        print("My soluton: ")
        a = np.ones((5, 5))
        a[1:-1, 1: -1] = 0
        a[2, 2] = 9
        print(a)

        print("His solution:")
        b = np.ones((5, 5))
        c = np.zeros((3, 3))
        c[1, 1] = 9
        b[1:4, 1:4] = c
        print(b)

    # Do operations on arrays
    def mathematics(self):
        print("Mathematics:")
        a = np.array([1, 2, 3, 4])
        print("a + 2: " + str(a + 2))
        print("a - 2: " + str(a - 2))
        print("a / 2: " + str(a / 2))
        print("a * 2: " + str(a * 2))
        b = np.array([1, 0, 1, 0])
        print("a*b" + str(a + b))
        print("a^2:" + str(a ** 2))
        print("sin():" + str(np.sin(a)))

    def linAlg(self):
        print("Matrix multiplication:")
        a = np.ones((2, 3))
        b = np.full((3, 2), 2)
        print(np.matmul(a, b))
        print("Determinant:")
        c = np.identity(3)
        print(np.linalg.det(c))

    def statistics(self):
        print("Statistics:")
        stats = np.array([[1, 2, 3], [4, 5, 6]])
        print("Min:" + str(np.min(stats)))
        print("Max:" + str(np.max(stats)))
        print("Min row:" + str(np.min(stats, axis=0)))
        print("Max row:" + str(np.max(stats, axis=0)))
        print("Min col:" + str(np.min(stats, axis=1)))
        print("Max col:" + str(np.max(stats, axis=1)))
        print("Sum:" + str(np.sum(stats)))

    def reorg(self):
        print("Reorganize array:")
        before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        print("Before:\n " + str(before))
        after = before.reshape((4, 2))
        print("After (4, 2): \n" + str(after))
        v1 = np.array([1, 2, 3, 4])
        v2 = np.array([5, 6, 7, 8])
        print("vstack:\n" + str(np.vstack([v1, v2])))
        print("hstack:\n" + str(np.hstack([v1, v2])))

    def loadData(self):
        print("Print from file:")
        a = np.genfromtxt('data.txt', delimiter=',')
        print("Float:\n" + str(a))
        a = a.astype('int32')
        print("Int:\n" + str(a))

    def advInd(self):
        print("Advanced methods from file:")
        a = np.genfromtxt('data.txt', delimiter=',')
        print("All values bigger than 5:\n" + str(a > 5))
        print("Index with a list:")
        b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(b[[1, 2, 8]])
        print("A value in a column is bigger:")
        print(np.any(a > 5, axis=0))
        print("All values in a column is bigger:")
        print(np.all(a > 2, axis=0))
        print("boolean check on values:")
        print((a < 5) & (a > 2))  # ~ = not

    def quiz(self):
        print("Quiz:")
        res = []
        for i in range(6):
            res.append(np.arange((5 * i) + 1, 5 * (i + 1) + 1))
        res = np.array(res)
        print(res)
        print("Answers:")
        print("1):\n" + str(res[2:4, 0:2]))
        print("2):\n" + str(res[[0, 1, 2, 3], [1, 2, 3, 4]]))
        print("3):\n" + str(res[[0, 4, 5], 3:]))


if __name__ == "__main__":
    num = numpyTest()
    num.basics()
    print()
    num.accessChangeArray()
    print()
    num.difArrays()
    print()
    num.initArray()
    print()
    num.mathematics()
    print()
    num.linAlg()
    print()
    num.statistics()
    print()
    num.reorg()
    print()
    num.loadData()
    print()
    num.advInd()
    print()
    num.quiz()
